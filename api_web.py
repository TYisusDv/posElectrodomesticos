from config import *
from models import *
#from tools import *
#from tasks import *

@app.route('/api/web/', defaults={'path': ''})
@app.route('/api/web/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def api_web(path):
    v_apiurlsplit = [api_urlsplit(path, i) for i in range(10)]

    try:
        if request.method in ['GET', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']:
            return json.dumps({'success': False, 'msg': 'Method not allowed.'}), 405
        
        device_name = api_getdevice(str(request.user_agent))
        ip_address = request.headers.get('CF-Connecting-IP')
        
        v_apiverifysession = api_verify_session()        
        v_requestform = request.form
        v_datetimenow = datetime.now()

        v_userinfo = None
        v_usersession = None
        v_apipermissions = [665590]
        if v_apiverifysession == 1:
            v_userinfo = us_users_model().get_user(us_id=session['us_id'])
            v_usersession = sess_usersessions_model().get_session(sess_id=session['sess_id'])
            v_apipermissions = api_permissions(v_userinfo['mem_id'])

        #VIEW
        if v_apiurlsplit[0] == 'view':
            #AUTH
            if v_apiurlsplit[1] == 'auth' and v_apiverifysession == 0: 
                if v_apiurlsplit[2] == 'sign-in' and v_apiurlsplit[3] is None: 
                    return json.dumps({'success': True, 'html': render_template('/auth/sign-in.html')})
            
            #POS
            if v_apiurlsplit[1] == 'pos':  
                #EMPLEADO
                if 111529 in v_apipermissions:
                    if v_apiurlsplit[2] == 'manage':
                        if v_apiurlsplit[3] == 'users' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/users'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            memberships = mem_memberships_model().get_memberships()
                            total_count = us_users_model().get_users_count()             
                            sessions_online = sess_usersessions_model().get_sessions(get='online', online=1)      
                            
                            total_online_count = len(sessions_online)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/users.html', total_count = total_count, total_online_count = total_online_count, memberships = memberships)})
                        elif v_apiurlsplit[3] == 'customers' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/customers'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            customers = cu_customers_model().get_customers()                    
                            hidden_count = sum(1 for customer in customers if customer["cu_status"] == 0)
                            visible_count = sum(1 for customer in customers if customer["cu_status"] == 1)
                            total_count = len(customers)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/customers.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'paymentmethods' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/paymentmethods'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            paymentmethods = pm_paymentmethods_model().get_paymentmethods()                    
                            hidden_count = sum(1 for paymentmethod in paymentmethods if paymentmethod["pm_status"] == 0)
                            visible_count = sum(1 for paymentmethod in paymentmethods if paymentmethod["pm_status"] == 1)
                            total_count = len(paymentmethods)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/paymentmethods.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'locations' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/locations'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            locations = lo_locations_model().get_locations()                    
                            hidden_count = sum(1 for location in locations if location["lo_status"] == 0)
                            visible_count = sum(1 for location in locations if location["lo_status"] == 1)
                            total_count = len(locations)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/locations.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'products' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/products'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            products = pr_products_model().get_products()
                            brands = br_brands_model().get_brands(get='status', br_status=1)  
                            categories = ca_categories_model().get_categories(get='status', ca_status=1)
                            providers = pv_providers_model().get_providers(get='status', pv_status=1)    

                            hidden_count = sum(1 for product in products if product["pr_status"] == 0)
                            visible_count = sum(1 for product in products if product["pr_status"] == 1)
                            total_count = len(products)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/products.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count, brands = brands, categories = categories, providers = providers)})
                        elif v_apiurlsplit[3] == 'providers' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/providers'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            providers = pv_providers_model().get_providers()                    
                            hidden_count = sum(1 for provider in providers if provider["pv_status"] == 0)
                            visible_count = sum(1 for provider in providers if provider["pv_status"] == 1)
                            total_count = len(providers)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/providers.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'categories' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/categories'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            categories = ca_categories_model().get_categories()                    
                            hidden_count = sum(1 for category in categories if category["ca_status"] == 0)
                            visible_count = sum(1 for category in categories if category["ca_status"] == 1)
                            total_count = len(categories)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/categories.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'brands' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/brands'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            brands = br_brands_model().get_brands()                    
                            hidden_count = sum(1 for brand in brands if brand["br_status"] == 0)
                            visible_count = sum(1 for brand in brands if brand["br_status"] == 1)
                            total_count = len(brands)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/brands.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        
                #ERROR 404
                if v_apiverifysession == 1: 
                    return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '404', msg = 'Página no encontrada.')}), 404                
            
            return json.dumps({'success': False, 'html': render_template('/auth/error.html', code = '404', msg = 'Página no encontrada.')}), 404
        
        #DATA
        elif v_apiurlsplit[0] == 'data':
            #AUTH
            if v_apiurlsplit[1] == 'auth' and v_apiverifysession == 0: 
                if v_apiurlsplit[2] == 'sign-in' and v_apiurlsplit[3] is None: 
                    email = v_requestform.get('email')
                    if not email:
                        return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})             
                    
                    passw = v_requestform.get('password')
                    if not passw:
                        return json.dumps({'success': False, 'msg': '¡La contraseña está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                    
                    userinfo = us_users_model().get_user(get='emailornumid', us_id=email, email=email)
                    if userinfo is None:
                        return json.dumps({'success': False, 'msg': '¡Correo, número de identificación o contraseña incorrectos! Por favor, corríjalo y vuelva a intentarlo.'})                   
                    
                    passw_db = userinfo['us_password']

                    try:
                        if not passw_db or not api_verifybcrypt(passw.encode('utf-8'), passw_db.encode('utf-8')):
                            return json.dumps({'success': False, 'msg': '¡Correo, número de identificación o contraseña incorrectos! Por favor, corríjalo y vuelva a intentarlo.'})                    
                    except:
                        password_1 = hashlib.md5(passw.encode('utf-8')).hexdigest()
                        password_2 = hashlib.md5(password_1.encode('utf-8')).hexdigest()

                        if passw_db != password_2:
                            return json.dumps({'success': False, 'msg': '¡Correo, número de identificación o contraseña incorrectos! Por favor, corríjalo y vuelva a intentarlo.'})
                        
                        hash = api_hashbcrypt(passw)
                        us_users_model().update_user(update='password', us_id=userinfo['us_id'], password=hash)
                    
                    us_id = userinfo['us_id']
                    sess_id = str(uuid.uuid4())

                    sess_usersessions_model().insert_session(sess_id, request.user_agent, us_id)

                    email = escape(email.strip().lower())

                    serializer = URLSafeSerializer(app.secret_key)                  
                    token = serializer.dumps({'us_id': us_id, 'sess_id': sess_id})                  
                    response = make_response(json.dumps({'success': True, 'msg': '¡El inicio de sesión se ha realizado correctamente! Bienvenido/a.'}))
                    max_age = 90 * 24 * 60 * 60
                    response.set_cookie('pos', token, max_age = max_age) 

                    session['us_id'] = us_id
                    session['sess_id'] = sess_id

                    return response

            #POS
            if v_apiurlsplit[1] == 'pos':  
                #EMPLEADO
                if 111529 in v_apipermissions:
                    if v_apiurlsplit[2] == 'account': 
                        if v_apiurlsplit[3] == 'info' and v_apiurlsplit[4] is None:    
                            sess_usersessions_model().update_session(update='online', sess_id=session['sess_id'], online=1)                        

                            account = {
                                'membership': v_userinfo['mem_name'],
                                'fullname': v_userinfo['pe_fullname'],
                                'email': v_userinfo['pe_email']
                            }
                            return json.dumps({'success': True, 'account': account}) 
                
                    #MANAGE
                    if v_apiurlsplit[2] == 'manage':
                        if v_apiurlsplit[3] == 'users':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/users'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                users = us_users_model().get_users(get='table', page_start=page_start, quantity = quantity, search = search)
                                for user in users:
                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{user["us_id"]}</span>',
                                        'fullname': user['pe_fullname'],
                                        'email': user['pe_email'],
                                        'membership': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{user["mem_name"]}</span>',        
                                        'phone': user['pe_phone'],                        
                                        'regdate': str(user['us_regdate']),
                                    }

                                    response['actions'] = f'<button class="btn btn-primary" user="{escape(json.dumps(response))}" user_permissions="{user["us_permissions"]}" onclick="edit_user(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                users_total = us_users_model().get_users_count(get='table', search=search)
                                total_pages = math.ceil(users_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_fullname = pe_fullname.strip().title()
                                pe_email = escape(pe_email.strip().lower())    
                                
                                if us_users_model().get_user(get='email', email=pe_email) is not None:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})

                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                us_password = v_requestform.get('us_password')
                                if not us_password:
                                    return json.dumps({'success': False, 'msg': '¡La contraseña está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                mem_id = v_requestform.get('mem_id')
                                if not mem_id:
                                    return json.dumps({'success': False, 'msg': '¡La membresía está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif mem_memberships_model().get_membership(mem_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La membresía no es válida! Por favor, corríjala y vuelva a intentarlo.'})                  
                                
                                us_id = api_genuniqueid()
                                us_password = api_hashbcrypt(us_password) 

                                us_users_model().insert_user(us_id=us_id, fullname=pe_fullname, email=pe_email, password=us_password, phone=pe_phone, mem_id=mem_id)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                us_id = v_requestform.get('us_id')
                                if not us_id:
                                    return json.dumps({'success': False, 'msg': '¡El usuario está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                v_userinfo_other = us_users_model().get_user(us_id=us_id)
                                if v_userinfo_other is None:
                                    return json.dumps({'success': False, 'msg': '¡El usuario no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_fullname = pe_fullname.strip().title()

                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_email = escape(pe_email.strip().lower())

                                pe_email_verify = us_users_model().get_user(get='email', email=pe_email) 
                                if pe_email_verify is not None and pe_email_verify['pe_email'] != v_userinfo_other['pe_email']:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                us_password = v_requestform.get('us_password')
                                if not us_password:
                                    us_password = None

                                mem_id = v_requestform.get('mem_id')
                                if not mem_id:
                                    return json.dumps({'success': False, 'msg': '¡La membresía está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif mem_memberships_model().get_membership(mem_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La membresía no es válida! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                us_permissions = v_requestform.getlist('manage-users-permissions')
                                if not us_permissions:
                                    us_permissions = None
                                else:
                                    us_permissions_list = []
                                    for permission in us_permissions:
                                        us_permissions_list.append(permission)
                                    
                                    us_permissions = str(us_permissions_list)
                            
                                if us_password is None:
                                    us_password = v_userinfo_other['us_password']
                                else:
                                    us_password = api_hashbcrypt(us_password) 

                                us_users_model().update_user(update='all', us_id=us_id, fullname=pe_fullname, email=pe_email, password=us_password, phone=pe_phone, permissions = us_permissions, mem_id=mem_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'customers':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/customers'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                customers = cu_customers_model().get_customers(get='table', page_start=page_start, quantity = quantity, search = search)
                                for customer in customers:
                                    status = "" 
                                    if customer['cu_status'] == 1:
                                        status = "checked"

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{customer["cu_id"]}</span>',
                                        'fullname': customer['pe_fullname'],
                                        'email': customer['pe_email'],
                                        'phone': customer['pe_phone'],                        
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" cu_id="{customer["cu_id"]}" onclick="check_status_customer(this)" {status}></div>'
                                    response['regdate'] = str(customer['cu_regdate'])
                                    response['actions'] = f'<button class="btn btn-primary" customer="{escape(json.dumps(response))}" onclick="edit_customer(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                customers_total = cu_customers_model().get_customers_count(get='table', search=search)
                                total_pages = math.ceil(customers_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_fullname = pe_fullname.strip().title()
                                pe_email = escape(pe_email.strip().lower())    
                                
                                if pe_persons_model().get_person(get='email', pe_id=pe_email) is not None:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})

                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_id = cu_customers_model().gen_customer_id()

                                cu_customers_model().insert_customer(cu_id=cu_id, fullname=pe_fullname, email=pe_email, phone=pe_phone)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                cu_id = v_requestform.get('cu_id')
                                if not cu_id:
                                    return json.dumps({'success': False, 'msg': '¡El cliente está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                cu_customer = cu_customers_model().get_customer(cu_id)
                                if cu_customer is None:
                                    return json.dumps({'success': False, 'msg': '¡El cliente no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_person = pe_persons_model().get_person(pe_id=cu_customer['pe_id'])
                                
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_fullname = pe_fullname.strip().title()
                                pe_email = escape(pe_email.strip().lower())    
                                
                                pe_email_verify = pe_persons_model().get_person(get='email', pe_id=pe_email) 
                                if pe_email_verify is not None and pe_email_verify['pe_email'] != pe_person['pe_email']:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})

                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_customers_model().update_customer(update='all', cu_id=cu_id, pe_fullname=pe_fullname, pe_email=pe_email, pe_phone=pe_phone)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                cu_id = v_requestform.get('cu_id')
                                if not cu_id:
                                    return json.dumps({'success': False, 'msg': '¡El cliente está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif cu_customers_model().get_customer(cu_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El cliente no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_status = v_requestform.get('cu_status')
                                if not cu_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not cu_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_customers_model().update_customer(update='status', status=cu_status, cu_id=cu_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'})                        
                        elif v_apiurlsplit[3] == 'paymentmethods':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/paymentmethods'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None: 
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                paymentmethods = pm_paymentmethods_model().get_paymentmethods(get='table', page_start=page_start, quantity = quantity, search = search)
                                for paymentmethod in paymentmethods:
                                    status = "" 
                                    if paymentmethod['pm_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{paymentmethod["pm_id"]}</span>',
                                        'name': paymentmethod['pm_name'],
                                        'per': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{paymentmethod["pm_per"]}</span>',
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" pm_id="{paymentmethod["pm_id"]}" onclick="check_status_paymentmethod(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" paymentmethod="{escape(json.dumps(response))}" onclick="edit_paymentmethod(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                paymentmethods_total = pm_paymentmethods_model().get_paymentmethods_count(get='table', search=search)
                                total_pages = math.ceil(paymentmethods_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                pm_name = v_requestform.get('pm_name')
                                if not pm_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                      

                                pm_name = pm_name.strip().capitalize()

                                pm_per = v_requestform.get('pm_per')
                                if not pm_per:
                                    return json.dumps({'success': False, 'msg': '¡El porcentaje está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pm_per.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El porcentaje no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pm_paymentmethods_model().insert_paymentmethod(pm_name, pm_per)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                pm_id = v_requestform.get('pm_id')
                                if not pm_id:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pm_paymentmethods_model().get_paymentmethod(pm_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pm_name = v_requestform.get('pm_name')
                                if not pm_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                      

                                pm_name = pm_name.strip().capitalize()

                                pm_per = v_requestform.get('pm_per')
                                if not pm_per:
                                    return json.dumps({'success': False, 'msg': '¡El porcentaje está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pm_per):
                                    return json.dumps({'success': False, 'msg': '¡El porcentaje no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pm_paymentmethods_model().update_paymentmethod(update='all', name=pm_name, per=pm_per, pm_id=pm_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                pm_id = v_requestform.get('pm_id')
                                if not pm_id:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pm_paymentmethods_model().get_paymentmethod(pm_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pm_status = v_requestform.get('pm_status')
                                if not pm_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pm_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pm_paymentmethods_model().update_paymentmethod(update='status', status=pm_status, pm_id=pm_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'locations':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/locations'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                locations = lo_locations_model().get_locations(get='table', page_start=page_start, quantity = quantity, search = search)
                                for location in locations:
                                    status = "" 
                                    if location['lo_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{location["lo_id"]}</span>',
                                        'name': location['lo_name']
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" lo_id="{location["lo_id"]}" onclick="check_status_location(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" location="{escape(json.dumps(response))}" onclick="edit_location(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                locations_total = lo_locations_model().get_locations_count(get='table', search=search)
                                total_pages = math.ceil(locations_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                lo_name = v_requestform.get('lo_name')
                                if not lo_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                lo_name = lo_name.strip().capitalize()

                                lo_locations_model().insert_location(lo_name)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                lo_id = v_requestform.get('lo_id')
                                if not lo_id:
                                    return json.dumps({'success': False, 'msg': '¡La ubicación está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif lo_locations_model().get_location(lo_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La ubicación no es válida! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                lo_name = v_requestform.get('lo_name')
                                if not lo_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                      

                                lo_name = lo_name.strip().capitalize()

                                lo_locations_model().update_location(update='all', name=lo_name, lo_id=lo_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                lo_id = v_requestform.get('lo_id')
                                if not lo_id:
                                    return json.dumps({'success': False, 'msg': '¡La ubicación está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif lo_locations_model().get_location(lo_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La ubicación no es válida! Por favor, corríjala y vuelva a intentarlo.'})

                                lo_status = v_requestform.get('lo_status')
                                if not lo_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not lo_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                lo_locations_model().update_location(update='status', status=lo_status, lo_id=lo_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'products':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/products'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                products = pr_products_model().get_products(get='table', page_start=page_start, quantity = quantity, search = search)
                                for product in products:
                                    status = "" 
                                    if product['pr_status'] == 1:
                                        status = "checked" 

                                    pr_img = api_getimagedata(f'static/img/product/{product["pr_id"]}.jpg')
                                    response = {
                                        'image': f'<img class="rounded-xl border border-separator-light border-4 sw-8 sh-8" alt="profile" src="{pr_img}">',
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{product["pr_id"]}</span>',
                                        'barcode': product['pr_barcode'],
                                        'name': product['pr_name'],
                                        'model': product['pr_model'],
                                        'brand': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{product["br_name"]}</span>',
                                        'description': product['pr_description'],
                                        'category': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{product["ca_name"]}</span>',
                                        'cost': product['pr_cost'],
                                        'provider': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{product["pe_fullname"]}</span>',
                                        'price': product['pr_price'],
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" pr_id="{product["pr_id"]}" onclick="check_status_product(this)" {status}></div>'
                                    response['regdate'] = str(product['pr_regdate'])
                                    response['actions'] = f'<button class="btn btn-primary" product="{escape(json.dumps(response))}" onclick="edit_product(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                products_total = pr_products_model().get_products_count(get='table', search=search)
                                total_pages = math.ceil(products_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                pr_barcode = v_requestform.get('pr_barcode')
                                if not pr_barcode:
                                    return json.dumps({'success': False, 'msg': '¡El código de barras está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_name = v_requestform.get('pr_name')
                                if not pr_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                pr_model = v_requestform.get('pr_model')
                                if not pr_model:
                                    return json.dumps({'success': False, 'msg': '¡El modelo está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                br_name = v_requestform.get('br_name')
                                if not br_name:
                                    return json.dumps({'success': False, 'msg': '¡La marca está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                br_name = br_name.strip().capitalize()

                                br_brand = br_brands_model().get_brand(get='name', br_name=br_name)
                                if br_brand and br_brand['br_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡La marca está desactivada! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                pr_description = v_requestform.get('pr_description')
                                if not pr_description:
                                    return json.dumps({'success': False, 'msg': '¡La descripcion está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                ca_name = v_requestform.get('ca_name')
                                if not ca_name:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                ca_name = ca_name.strip().capitalize()
                                
                                ca_category = ca_categories_model().get_category(get='name', ca_name=ca_name)
                                if ca_category and ca_category['ca_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está desactivada! Por favor, corríjala y vuelva a intentarlo.'})

                                pr_cost = v_requestform.get('pr_cost')
                                if not pr_cost:
                                    return json.dumps({'success': False, 'msg': '¡El costo está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_cost):
                                    return json.dumps({'success': False, 'msg': '¡El costo no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_id = v_requestform.get('pv_id')
                                if not pv_id:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pv_providers_model().get_provider(pv_id):
                                    return json.dumps({'success': False, 'msg': '¡El proveedor no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_price = v_requestform.get('pr_price')
                                if not pr_price:
                                    return json.dumps({'success': False, 'msg': '¡El precio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_price):
                                    return json.dumps({'success': False, 'msg': '¡El precio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_img = v_requestform.get('pr_img')
                                if not pr_img:
                                    return json.dumps({'success': False, 'msg': '¡La imagen está vacía! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pr_img.startswith('data:image/jpeg') and not pr_img.startswith('data:image/jpg'):
                                    return json.dumps({'success': False, 'msg': '¡La imagen no es válida! Solo se permite JPG, JPEG. Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_id = api_genuniqueid()
                                
                                br_id = None
                                while not br_id:
                                    result = br_brands_model().get_brand(get='name', br_name=br_name)
                                    if result:
                                        br_id = result['br_id']
                                    else:
                                        br_brands_model().insert_brand(name=br_name)
                                
                                ca_id = None
                                while not ca_id:
                                    result = ca_categories_model().get_category(get='name', ca_name=ca_name)
                                    if result:
                                        ca_id = result['ca_id']
                                    else:
                                        ca_categories_model().insert_category(name=ca_name)
                                
                                filename = secure_filename(pr_id + '.jpg')    
                                path_file = os.path.join(app.root_path, 'static/img/product', filename)                                
                                with open(path_file, 'wb') as f:
                                    imagen_bytes = base64.b64decode(pr_img.split(',')[1])
                                    f.write(imagen_bytes)

                                pr_products_model().insert_product(pr_id = pr_id, pr_barcode = pr_barcode, pr_name = pr_name, pr_model = pr_model, pr_description = pr_description, pr_cost = pr_cost, pr_price = pr_price, ca_id = ca_id, br_id = br_id, pv_id = pv_id)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                pr_id = v_requestform.get('pr_id')
                                if not pr_id:
                                    return json.dumps({'success': False, 'msg': '¡El producto está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pr_products_model().get_product(pr_id=pr_id):
                                    return json.dumps({'success': False, 'msg': '¡El producto no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_barcode = v_requestform.get('pr_barcode')
                                if not pr_barcode:
                                    return json.dumps({'success': False, 'msg': '¡El código de barras está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_name = v_requestform.get('pr_name')
                                if not pr_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                pr_model = v_requestform.get('pr_model')
                                if not pr_model:
                                    return json.dumps({'success': False, 'msg': '¡El modelo está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                br_name = v_requestform.get('br_name')
                                if not br_name:
                                    return json.dumps({'success': False, 'msg': '¡La marca está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                br_name = br_name.strip().capitalize()

                                br_brand = br_brands_model().get_brand(get='name', br_name=br_name)
                                if br_brand and br_brand['br_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡La marca está desactivada! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                pr_description = v_requestform.get('pr_description')
                                if not pr_description:
                                    return json.dumps({'success': False, 'msg': '¡La descripcion está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                ca_name = v_requestform.get('ca_name')
                                if not ca_name:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                ca_name = ca_name.strip().capitalize()
                                
                                ca_category = ca_categories_model().get_category(get='name', ca_name=ca_name)
                                if ca_category and ca_category['ca_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está desactivada! Por favor, corríjala y vuelva a intentarlo.'})

                                pr_cost = v_requestform.get('pr_cost')
                                if not pr_cost:
                                    return json.dumps({'success': False, 'msg': '¡El costo está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_cost):
                                    return json.dumps({'success': False, 'msg': '¡El costo no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_id = v_requestform.get('pv_id')
                                if not pv_id:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pv_providers_model().get_provider(pv_id):
                                    return json.dumps({'success': False, 'msg': '¡El proveedor no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_price = v_requestform.get('pr_price')
                                if not pr_price:
                                    return json.dumps({'success': False, 'msg': '¡El precio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_price):
                                    return json.dumps({'success': False, 'msg': '¡El precio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_img = v_requestform.get('pr_img')
                                if not pr_img:
                                    return json.dumps({'success': False, 'msg': '¡La imagen está vacía! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pr_img.startswith('data:image/jpeg') and not pr_img.startswith('data:image/jpg'):
                                    return json.dumps({'success': False, 'msg': '¡La imagen no es válida! Solo se permite JPG, JPEG. Por favor, corríjalo y vuelva a intentarlo.'})
                                                                
                                br_id = None
                                while not br_id:
                                    result = br_brands_model().get_brand(get='name', br_name=br_name)
                                    if result:
                                        br_id = result['br_id']
                                    else:
                                        br_brands_model().insert_brand(name=br_name)
                                
                                ca_id = None
                                while not ca_id:
                                    result = ca_categories_model().get_category(get='name', ca_name=ca_name)
                                    if result:
                                        ca_id = result['ca_id']
                                    else:
                                        ca_categories_model().insert_category(name=ca_name)
                                
                                filename = secure_filename(pr_id + '.jpg')    
                                path_file = os.path.join(app.root_path, 'static/img/product', filename)                                
                                with open(path_file, 'wb') as f:
                                    imagen_bytes = base64.b64decode(pr_img.split(',')[1])
                                    f.write(imagen_bytes)

                                pr_products_model().update_product(update='all', pr_id = pr_id, pr_barcode = pr_barcode, pr_name = pr_name, pr_model = pr_model, pr_description = pr_description, pr_cost = pr_cost, pr_price = pr_price, ca_id = ca_id, br_id = br_id, pv_id = pv_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                pr_id = v_requestform.get('pr_id')
                                if not pr_id:
                                    return json.dumps({'success': False, 'msg': '¡El producto está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pr_products_model().get_product(pr_id=pr_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La producto no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pr_status = v_requestform.get('pr_status')
                                if not pr_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pr_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pr_products_model().update_product(update='status', pr_status=pr_status, pr_id=pr_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'providers':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/providers'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                providers = pv_providers_model().get_providers(get='table', page_start=page_start, quantity = quantity, search = search)
                                for provider in providers:
                                    status = "" 
                                    if provider['pv_status'] == 1:
                                        status = "checked"

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{provider["pv_id"]}</span>',
                                        'fullname': provider['pe_fullname'],
                                        'email': provider['pe_email'],
                                        'phone': provider['pe_phone'],                        
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" pv_id="{provider["pv_id"]}" onclick="check_status_provider(this)" {status}></div>'
                                    response['regdate'] = str(provider['pv_regdate'])
                                    response['actions'] = f'<button class="btn btn-primary" provider="{escape(json.dumps(response))}" onclick="edit_provider(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                providers_total = pv_providers_model().get_providers_count(get='table', search=search)
                                total_pages = math.ceil(providers_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_fullname = pe_fullname.strip().title()
                                pe_email = escape(pe_email.strip().lower())    
                                
                                if pe_persons_model().get_person(get='email', pe_id=pe_email) is not None:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})

                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_id = pv_providers_model().gen_provider_id()

                                pv_providers_model().insert_provider(pv_id=pv_id, fullname=pe_fullname, email=pe_email, phone=pe_phone)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                pv_id = v_requestform.get('pv_id')
                                if not pv_id:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pv_provider = pv_providers_model().get_provider(pv_id)
                                if pv_provider is None:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_person = pe_persons_model().get_person(pe_id=pv_provider['pe_id'])
                                
                                pe_fullname = v_requestform.get('pe_fullname')
                                if not pe_fullname:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                       
                                
                                pe_email = v_requestform.get('pe_email')
                                if not pe_email:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_emailvalid(pe_email.lower()):
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico es invalido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pe_fullname = escape(pe_fullname)
                                pe_fullname = pe_fullname.strip().title()
                                pe_email = escape(pe_email.strip().lower())    
                                
                                pe_email_verify = pe_persons_model().get_person(get='email', pe_id=pe_email) 
                                if pe_email_verify is not None and pe_email_verify['pe_email'] != pe_person['pe_email']:
                                    return json.dumps({'success': False, 'msg': '¡El correo electrónico ya existe! Por favor, corríjalo y vuelva a intentarlo.'})

                                pe_phone = v_requestform.get('pe_phone')
                                if not pe_phone:
                                    return json.dumps({'success': False, 'msg': '¡El número telefónico está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_providers_model().update_provider(update='all', pv_id=pv_id, pe_fullname=pe_fullname, pe_email=pe_email, pe_phone=pe_phone)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                pv_id = v_requestform.get('pv_id')
                                if not pv_id:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pv_providers_model().get_provider(pv_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El proveedor no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_status = v_requestform.get('pv_status')
                                if not pv_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not pv_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                pv_providers_model().update_provider(update='status', status=pv_status, pv_id=pv_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'})                        
                        elif v_apiurlsplit[3] == 'categories':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/categories'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                categories = ca_categories_model().get_categories(get='table', page_start=page_start, quantity = quantity, search = search)
                                for category in categories:
                                    status = "" 
                                    if category['ca_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{category["ca_id"]}</span>',
                                        'name': category['ca_name']
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" ca_id="{category["ca_id"]}" onclick="check_status_category(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" category="{escape(json.dumps(response))}" onclick="edit_category(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                categories_total = ca_categories_model().get_categories_count(get='table', search=search)
                                total_pages = math.ceil(categories_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                ca_name = v_requestform.get('ca_name')
                                if not ca_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                ca_name = ca_name.strip().capitalize()

                                ca_categories_model().insert_category(ca_name)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                ca_id = v_requestform.get('ca_id')
                                if not ca_id:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif ca_categories_model().get_category(ca_id=ca_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La categoría no es válida! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                ca_name = v_requestform.get('ca_name')
                                if not ca_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                      

                                ca_name = ca_name.strip().capitalize()

                                ca_categories_model().update_category(update='all', name=ca_name, ca_id=ca_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                ca_id = v_requestform.get('ca_id')
                                if not ca_id:
                                    return json.dumps({'success': False, 'msg': '¡La categoría está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif ca_categories_model().get_category(ca_id=ca_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La categoría no es válida! Por favor, corríjala y vuelva a intentarlo.'})

                                ca_status = v_requestform.get('ca_status')
                                if not ca_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not ca_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                ca_categories_model().update_category(update='status', status=ca_status, ca_id=ca_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'brands':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/brands'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None:
                                page = v_requestform.get('page')
                                if not page or not page.isnumeric():
                                    page = 1
                                
                                search = v_requestform.get('search')
                                if not search:
                                    search = ''

                                page = int(page)
                                quantity = 10
                                page_start = (page - 1) * quantity 

                                table = []
                                brands = br_brands_model().get_brands(get='table', page_start=page_start, quantity = quantity, search = search)
                                for brand in brands:
                                    status = "" 
                                    if brand['br_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{brand["br_id"]}</span>',
                                        'name': brand['br_name']
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" br_id="{brand["br_id"]}" onclick="check_status_brand(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" brand="{escape(json.dumps(response))}" onclick="edit_brand(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                brands_total = br_brands_model().get_brands_count(get='table', search=search)
                                total_pages = math.ceil(brands_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'add' and v_apiurlsplit[5] is None:
                                br_name = v_requestform.get('br_name')
                                if not br_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                br_name = br_name.strip().capitalize()

                                br_brands_model().insert_brand(br_name)
                                return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                br_id = v_requestform.get('br_id')
                                if not br_id:
                                    return json.dumps({'success': False, 'msg': '¡La marca está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif br_brands_model().get_brand(br_id=br_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La marca no es válida! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                br_name = v_requestform.get('br_name')
                                if not br_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                      

                                br_name = br_name.strip().capitalize()

                                br_brands_model().update_brand(update='all', name=br_name, br_id=br_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                br_id = v_requestform.get('br_id')
                                if not br_id:
                                    return json.dumps({'success': False, 'msg': '¡La marca está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif br_brands_model().get_brand(br_id=br_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡La marca no es válida! Por favor, corríjala y vuelva a intentarlo.'})

                                br_status = v_requestform.get('br_status')
                                if not br_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not br_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                br_brands_model().update_brand(update='status', status=br_status, br_id=br_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 

            return json.dumps({'success': False, 'msg': 'Página no encontrada.'}), 404
    except Exception as e:
        api_savelog('log/api-web-error.log', f'[E{sys.exc_info()[-1].tb_lineno}] {e}')
        if v_apiurlsplit[0] == 'view':
            return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '500', msg = 'An error has occurred! Reported to all admins.')}), 500        
        
        return json.dumps({'success': False, 'msg': 'An error has occurred! Reported to all admins.'}), 500

@app.route('/api/web/token/csrf', methods = ['GET'])
@csrf.exempt
def api_web_token():
    return json.dumps({'success': True, 'token':  generate_csrf()}), 200

@app.route('/auth/logout', methods = ['GET'])
def api_web_authlogout():  
    if 'sess_id' in session:
        sess_usersessions_model().remove_session(sess_id=session['sess_id'])
    
    response = make_response(redirect('/'))    
    response.delete_cookie('pos')
    session.clear()
    return response