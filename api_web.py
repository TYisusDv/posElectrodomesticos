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
        v_date = v_datetimenow.date()

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
                if 111529 in v_apipermissions and v_userinfo['us_status'] == 1:
                    #POS
                    if v_apiurlsplit[2] is None:
                        return json.dumps({'success': True, 'html': render_template('/pos/home.html')})
                    elif v_apiurlsplit[2] == 'app' and v_apiurlsplit[3] is None:
                        locations = lo_locations_model().get_locations(get='status', lo_status=1)
                        typessales = ts_typessales_model().get_typessales()
                        paymentmethods = pm_paymentmethods_model().get_paymentmethods(get='status', pm_status=1)
                        return json.dumps({'success': True, 'html': render_template('/pos/pos.html', locations = locations, typessales = typessales, paymentmethods = paymentmethods)})
                    elif v_apiurlsplit[2] == 'statistics' and v_apiurlsplit[5] is None:
                        date_1 = v_apiurlsplit[3]
                        date_2 = v_apiurlsplit[4]

                        if date_1 is None: 
                            date_1 = v_date
                        
                        if date_2 is None: 
                            date_2 = date_1

                        try:
                            date_1 = datetime.strptime(date_1, '%Y-%m-%d').date()
                        except:
                            date_1 = v_date

                        try:
                            date_2 = datetime.strptime(date_2, '%Y-%m-%d').date()
                        except:
                            date_2 = date_1
                        
                        sales = sa_sales_model().get_sales(get = 'table,statistics', date_1 = date_1, date_2 = date_2)
                        total_sales = sum(sale['sa_subtotal'] - sale['sa_discount'] for sale in sales if sale['sa_status'] == 1)

                        salepayments = sp_salepayments_model().get_salepayments(get = 'table,statistics', date_1 = date_1, date_2 = date_2)
                        total_salepayments = sum(salepayment['sp_pay'] for salepayment in salepayments if salepayment['sa_status'] == 1)
                       
                        return json.dumps({'success': True, 'html': render_template('/pos/statistics.html', date_1 = date_1, date_2 = date_2, sales = sales, total_sales = total_sales, salepayments = salepayments, total_salepayments = total_salepayments)})
                    
                    #MANAGE
                    elif v_apiurlsplit[2] == 'manage':
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
                        elif v_apiurlsplit[3] == 'cities' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/cities'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            cities = ci_cities_model().get_cities()
                            states = st_states_model().get_states(get='status', st_status=1)
                            hidden_count = sum(1 for city in cities if city["ci_status"] == 0)
                            visible_count = sum(1 for city in cities if city["ci_status"] == 1)
                            total_count = len(cities)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/cities.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count, states = states)})
                        elif v_apiurlsplit[3] == 'states' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/states'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            states = st_states_model().get_states()
                            hidden_count = sum(1 for state in states if state["st_status"] == 0)
                            visible_count = sum(1 for state in states if state["st_status"] == 1)
                            total_count = len(states)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/states.html', total_count = total_count, hidden_count = hidden_count, visible_count = visible_count)})
                        elif v_apiurlsplit[3] == 'addresses' and v_apiurlsplit[5] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/addresses'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            pe_id = v_apiurlsplit[4]
                            
                            if pe_persons_model().get_person(pe_id=pe_id):
                                addresses = ad_addresses_model().get_addresses(get='personstatus', pe_id = pe_id, ad_status = 1)
                                cities = ci_cities_model().get_cities(get='status', ci_status=1)
                                states = st_states_model().get_states(get='status', st_status=1)
                                addresstypes = at_addresstypes_model().get_addresstypes()                    
                                total_count = len(addresses)
                                
                                return json.dumps({'success': True, 'html': render_template('/pos/manage/addresses.html', pe_id = pe_id, total_count = total_count, cities = cities, states = states, addresstypes = addresstypes)})
                        elif v_apiurlsplit[3] == 'sales' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sales'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            sales = sa_sales_model().get_sales()  
                            salepayments = sp_salepayments_model().get_salepayments(get = 'limitdate')                  
                            canceled = sum(1 for sale in sales if sale["sa_status"] == 0)
                            total_sales = sum(1 for sale in sales if sale["sa_status"] == 1)
                            total_count = len(sales)
                            total_count_salepayments = len(salepayments)
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/sales.html', total_count = total_count, canceled = canceled, total_sales = total_sales, total_count_salepayments = total_count_salepayments)})
                        elif v_apiurlsplit[3] == 'sale':
                            sa_id = v_apiurlsplit[4] 
                            sa_sale = sa_sales_model().get_sale(get = 'sa_id>sa_status', sa_id = sa_id, sa_status = 1)
                            if sa_sale:
                                if v_apiurlsplit[5] == 'payments' and v_apiurlsplit[6] is None: 
                                    if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sale/payments'):
                                        return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                                    
                                    paymentmethods = pm_paymentmethods_model().get_paymentmethods(get='status', pm_status=1)
                                    salepayments = sp_salepayments_model().get_salepayments(get = 'sa_id', sa_id = sa_id)
                                    total_pay = sum(salepayment['sp_pay'] for salepayment in salepayments)
                                    remainingpayment = (sa_sale["sa_subtotal"] - sa_sale["sa_discount"]) - total_pay
                                    
                                    return json.dumps({'success': True, 'html': render_template('/pos/manage/salepayments.html', sale = sa_sale, remainingpayment = remainingpayment, paymentmethods = paymentmethods)})
                        elif v_apiurlsplit[3] == 'dbbackup' and v_apiurlsplit[4] is None: 
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/dbbackup'):
                                return json.dumps({'success': False, 'html': render_template('/pos/error.html', code = '403', msg = '¡Acceso denegado! No tienes permiso.')}), 403
                            
                            return json.dumps({'success': True, 'html': render_template('/pos/manage/dbbackup.html')})
                        
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
                    
                    if userinfo['us_status'] == 0:
                        return json.dumps({'success': False, 'msg': '¡Has sido bloqueado! Contacta con un administrador o soporte técnico.'})
                    
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
                if 111529 in v_apipermissions and v_userinfo['us_status'] == 1:
                    #ACCOUNT
                    if v_apiurlsplit[2] == 'account': 
                        if v_apiurlsplit[3] == 'info' and v_apiurlsplit[4] is None:    
                            sess_usersessions_model().update_session(update='online', sess_id=session['sess_id'], online=1)                        

                            account = {
                                'membership': v_userinfo['mem_name'],
                                'fullname': v_userinfo['pe_fullname'],
                                'email': v_userinfo['pe_email']
                            }
                            return json.dumps({'success': True, 'account': account}) 
                    
                    #APP
                    elif v_apiurlsplit[2] == 'app':
                        if v_apiurlsplit[3] == 'get':
                            if v_apiurlsplit[4] == 'customers' and v_apiurlsplit[5] is None:
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
                                    status = "<span class='badge bg-danger'>Prohibido<span>" 
                                    if customer['cu_status'] == 1:
                                        status = "<span class='badge bg-primary'>Activo<span>"

                                    response = {
                                        'cu_id': customer['cu_id'],
                                        'pe_fullname': customer['pe_fullname'],
                                        'pe_email': customer['pe_email'],
                                        'pe_phone': customer['pe_phone'],
                                        'cu_status': status,                        
                                    }

                                    table.append(response)

                                if not table:
                                    response = {
                                        'cu_id': 'N/A',
                                        'pe_fullname': '¡Sin resultados!',
                                        'pe_email': 'N/A',
                                        'pe_phone': 'N/A',
                                        'cu_status': "<span class='badge bg-danger'>N/A<span>",                        
                                    }

                                    table.append(response)
                                
                                customers_total = cu_customers_model().get_customers_count(get='table', search=search)
                                total_pages = math.ceil(customers_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/card-customers.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'products' and v_apiurlsplit[5] is None:
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
                                products = pr_products_model().get_products(get='tablestatus', pr_status = 1, page_start=page_start, quantity = quantity, search = search)
                                for product in products:
                                    response = {
                                        'pr_id': product['pr_id'],
                                        'pr_barcode': product['pr_barcode'],
                                        'pr_name': product['pr_name'],
                                        'pr_model': product['pr_model'],
                                        'pr_price': product['pr_price'],
                                        'br_name': product['br_name'],
                                    }

                                    table.append(response)

                                if not table:
                                    response = {
                                        'pr_id': 'N/A',
                                        'pr_barcode': 'N/A',
                                        'pr_name': '¡Sin resultados!',
                                        'pr_model': 'N/A',
                                        'pr_price': 'N/A',
                                        'br_name': 'N/A',
                                    }

                                    table.append(response)
                                
                                products_total = pr_products_model().get_products_count(get='tablestatus', pr_status = 1, search=search)
                                total_pages = math.ceil(products_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/card-products.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'info' and v_apiurlsplit[5] is None:
                                token = request.cookies.get('posinfo')
                                serializer = URLSafeSerializer(app.secret_key)
                                try:
                                    info = serializer.loads(token)
                                except:
                                    info = {
                                        'location': {
                                            'lo_id': 0,
                                            'lo_name': None,
                                        },
                                        'typesale': {
                                            'ts_id': 0,
                                            'ts_name': None,
                                            'ts_amountpayments': None,
                                            'ts_days': None,
                                            'ts_firstpayment': None,
                                            'ts_details': None,
                                            'ts_total': 0,
                                        },
                                        'paymentmethod': {
                                            'pm_id': 0,
                                            'pm_name': None,
                                        },                                        
                                        'customer': {
                                            'cu_id': 'N/A',
                                            'pe_id': None,
                                            'pe_fullname': None,
                                            'pe_email': None,
                                            'pe_phone': None,
                                        },
                                        'products': [],
                                        'subtotal': 0,
                                        'commission': 0,
                                        'commission_per': 0,
                                        'discount_per': 0,
                                        'discount': 0,
                                        'total': 0,
                                        'fin': False,
                                    }                                

                                subtotal = sum(product['total'] for product in info['products'])
                                commission = subtotal * (info['commission_per'] / 100)
                                total_full = (subtotal + commission)
                                discount = total_full * (info['discount_per'] / 100)
                                total = total_full - discount
                                
                                info['subtotal'] = subtotal
                                info['commission'] = commission
                                info['discount'] = discount
                                info['total'] = total

                                ts_total = 0
                                if info['typesale']['ts_id'] == 1001:
                                    ts_details = '1 solo pago'                                    
                                elif info['typesale']['ts_id'] == 1002 or info['typesale']['ts_id'] == 1004:
                                    ts_commission = info['typesale']['ts_firstpayment'] * (info['commission_per'] / 100)
                                    ts_total = (info['typesale']['ts_firstpayment'] + ts_commission)

                                    ts_details = f'{info["typesale"]["ts_amountpayments"]} pago(s) cada {info["typesale"]["ts_days"]} dia(s)'
                                    info['commission'] = ts_commission
                                elif info['typesale']['ts_id'] == 1003:
                                    ts_details = f'Se pagará en {info["typesale"]["ts_days"]} dia(s)'
                                else:
                                    ts_details = ''

                                info['typesale']['ts_details'] = ts_details
                                info['typesale']['ts_total'] = ts_total

                                if len(info['products']) > 0 and info['location']['lo_id'] > 0 and info['typesale']['ts_id'] > 0 and info['paymentmethod']['pm_id'] > 0:
                                    info['fin'] = True
                                else:
                                    info['fin'] = False

                                token = serializer.dumps(info) 
                                response = make_response(json.dumps({'success': True, 'info': info}))                         
                                response.set_cookie('posinfo', token) 
                                
                                return response
                        elif v_apiurlsplit[3] == 'set':
                            if v_apiurlsplit[4] == 'customer' and v_apiurlsplit[5] is None:
                                cu_id = v_requestform.get('cu_id')
                                if not cu_id:
                                    return json.dumps({'success': False, 'msg': '¡El cliente está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                cu_customer = cu_customers_model().get_customer(cu_id)
                                if cu_customer is None:
                                    return json.dumps({'success': False, 'msg': '¡El cliente no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif cu_customer['cu_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡El cliente esta prohibido! Por favor, corríjalo y vuelva a intentarlo.'})

                                token = request.cookies.get('posinfo')
                                serializer = URLSafeSerializer(app.secret_key)
                                info = None
                                try:
                                    info = serializer.loads(token)
                                except:
                                    return json.dumps({'success': False, 'msg': '¡No se creo la venta! Póngase en contacto con un soporte técnico.'})  
                                
                                info['customer']['cu_id'] = cu_customer['cu_id']
                                info['customer']['pe_id'] = cu_customer['pe_id']
                                info['customer']['pe_fullname'] = cu_customer['pe_fullname']
                                info['customer']['pe_email'] = cu_customer['pe_email']
                                info['customer']['pe_phone'] = cu_customer['pe_phone']

                                token = serializer.dumps(info) 
                                response = make_response(json.dumps({'success': True, 'msg': '¡Se guardó correctamente!'}))                         
                                response.set_cookie('posinfo', token) 

                                return response
                            elif v_apiurlsplit[4] == 'product' and v_apiurlsplit[5] is None:
                                pr_id = v_requestform.get('pr_id')
                                if not pr_id:
                                    return json.dumps({'success': False, 'msg': '¡El producto está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                pr_product = pr_products_model().get_product(pr_id)
                                if pr_product is None:
                                    return json.dumps({'success': False, 'msg': '¡El producto no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pr_product['pr_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡El producto está desactivado! Por favor, corríjalo y vuelva a intentarlo.'})

                                quantity = v_requestform.get('quantity')
                                if not quantity:
                                    return json.dumps({'success': False, 'msg': '¡La cantidad está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                elif not api_isFloat(quantity):
                                    return json.dumps({'success': False, 'msg': '¡La cantidad no es válida!  Por favor, corríjala y vuelva a intentarlo.'})
                                
                                pr_price = v_requestform.get('pr_price')
                                if not pr_price:
                                    return json.dumps({'success': False, 'msg': '¡El precio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_price):
                                    return json.dumps({'success': False, 'msg': '¡El precio no es válido!  Por favor, corríjalo y vuelva a intentarlo.'})

                                token = request.cookies.get('posinfo')
                                serializer = URLSafeSerializer(app.secret_key)
                                info = None
                                try:
                                    info = serializer.loads(token)
                                except:
                                    return json.dumps({'success': False, 'msg': '¡No se creó la venta! Póngase en contacto con un soporte técnico.'})

                                existing_product = None
                                for product in info['products']:
                                    if product['pr_id'] == pr_id:
                                        existing_product = product
                                        break

                                if existing_product is not None:
                                    existing_product['quantity'] = float(quantity)
                                    existing_product['pr_price'] = float(pr_price)
                                    if existing_product['quantity'] <= 0:
                                        info['products'].remove(existing_product)
                                    else:
                                        existing_product['total'] = existing_product['quantity'] * existing_product['pr_price']
                                        existing_product['html'] = render_template('/widget/card-products-cart.html', pr_id=existing_product['pr_id'], pr_img=f'/static/img/product/{existing_product["pr_id"]}.jpg', pr_name=existing_product['pr_name'], br_name=existing_product['br_name'], pr_barcode=existing_product['pr_barcode'], pr_model=existing_product['pr_model'], pr_price=existing_product['pr_price'], pr_price_2=existing_product['pr_price_2'], pr_cost=existing_product['pr_cost'], pr_pricetopayments=existing_product['pr_pricetopayments'], quantity=existing_product['quantity'], total=existing_product['total'])
                                
                                token = serializer.dumps(info)
                                response = make_response(json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}))
                                response.set_cookie('posinfo', token)

                                return response
                            elif v_apiurlsplit[4] == 'sale' and v_apiurlsplit[5] is None:
                                lo_id = v_requestform.get('lo_id')
                                if not lo_id:
                                    return json.dumps({'success': False, 'msg': '¡La sucursal está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                lo_location = lo_locations_model().get_location(lo_id)
                                if lo_location is None:
                                    lo_id = 0
                                elif lo_location['lo_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡La sucursal esta prohibida! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                ts_id = v_requestform.get('ts_id')
                                if not ts_id:
                                    return json.dumps({'success': False, 'msg': '¡El tipo de venta está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                ts_typesale = ts_typessales_model().get_typesale(ts_id)
                                if ts_typesale is None:
                                    ts_id = 0
                                                                
                                pm_id = v_requestform.get('pm_id')
                                if not pm_id:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pm_paymentmethod = pm_paymentmethods_model().get_paymentmethod(pm_id)
                                if pm_paymentmethod is None:
                                    pm_id = 0
                                elif pm_paymentmethod['pm_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡El método de pago esta prohibido! Por favor, corríjalo y vuelva a intentarlo.'})

                                discount_per = v_requestform.get('discount_per')
                                if not discount_per:
                                    discount_per = 0
                                elif discount_per.lower() == 'nan':
                                    return json.dumps({'success': False, 'msg': '¡El descuento no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(discount_per):
                                    return json.dumps({'success': False, 'msg': '¡El descuento no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif float(discount_per) > 100 or float(discount_per) < 0:
                                    return json.dumps({'success': False, 'msg': '¡El descuento no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                token = request.cookies.get('posinfo')
                                serializer = URLSafeSerializer(app.secret_key)
                                info = None
                                try:
                                    info = serializer.loads(token)
                                except:
                                    return json.dumps({'success': False, 'msg': '¡No se creo la venta! Póngase en contacto con un soporte técnico.'})                                 

                                ts_amountpayments = None
                                ts_days = None
                                ts_firstpayment = None
                                
                                if ts_id == '1002' or ts_id == '1004':
                                    ts_amountpayments = v_requestform.get('ts_amountpayments')
                                    if not ts_amountpayments:
                                        ts_amountpayments = 1
                                    elif not ts_amountpayments.isnumeric():
                                        ts_amountpayments = 1
                                    elif int(ts_amountpayments) <= 0:
                                        ts_amountpayments = 1

                                    ts_amountpayments = int(ts_amountpayments)

                                    ts_firstpayment = v_requestform.get('ts_firstpayment')
                                    if not ts_firstpayment:
                                        ts_firstpayment = 0
                                    elif not api_isFloat(ts_firstpayment):
                                        ts_firstpayment = 0
                                    elif float(ts_firstpayment) < 0:
                                        ts_firstpayment = 0

                                    ts_firstpayment = float(ts_firstpayment)

                                if ts_id == '1002' or ts_id == '1003' or ts_id == '1004':
                                    ts_days = v_requestform.get('ts_days')
                                    if not ts_days:
                                        ts_days = 0
                                    elif not ts_days.isnumeric():
                                        ts_days = 0
                                    elif int(ts_days) < 0:
                                        ts_days = 0
                                    
                                    ts_days = int(ts_days)
                                

                                if int(lo_id) <= 0:
                                    lo_name = ''
                                else:
                                    lo_name = lo_location['lo_name']

                                if int(ts_id) <= 0:
                                    ts_name = ''
                                else:
                                    ts_name = ts_typesale['ts_name']

                                if int(pm_id) <= 0:
                                    pm_name = ''
                                    pm_per = 0
                                else:
                                    pm_name = pm_paymentmethod['pm_name']
                                    pm_per = pm_paymentmethod['pm_per']

                                info['location']['lo_id'] = int(lo_id)
                                info['location']['lo_name'] = lo_name
                                info['typesale']['ts_id'] = int(ts_id)
                                info['typesale']['ts_name'] = ts_name
                                info['typesale']['ts_amountpayments'] = ts_amountpayments
                                info['typesale']['ts_days'] = ts_days
                                info['typesale']['ts_firstpayment'] = ts_firstpayment
                                info['paymentmethod']['pm_id'] = int(pm_id)
                                info['paymentmethod']['pm_name'] = pm_name
                                info['discount_per'] = float(discount_per)
                                info['commission_per'] = float(pm_per)

                                token = serializer.dumps(info) 
                                response = make_response(json.dumps({'success': True, 'msg': '¡Se guardó correctamente!'}))                         
                                response.set_cookie('posinfo', token) 

                                return response                           
                        elif v_apiurlsplit[3] == 'add':
                            if v_apiurlsplit[4] == 'product' and v_apiurlsplit[5] is None:
                                pr_id = v_requestform.get('pr_id')
                                if not pr_id:
                                    return json.dumps({'success': False, 'msg': '¡El producto está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                pr_product = pr_products_model().get_product(pr_id)
                                if pr_product is None:
                                    return json.dumps({'success': False, 'msg': '¡El producto no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif pr_product['pr_status'] == 0:
                                    return json.dumps({'success': False, 'msg': '¡El producto esta desactivado! Por favor, corríjalo y vuelva a intentarlo.'})

                                token = request.cookies.get('posinfo')
                                serializer = URLSafeSerializer(app.secret_key)
                                info = None
                                try:
                                    info = serializer.loads(token)
                                except:
                                    return json.dumps({'success': False, 'msg': '¡No se creo la venta! Póngase en contacto con un soporte técnico.'})  
                                
                                existing_product = None
                                for product in info['products']:
                                    if product['pr_id'] == pr_id:
                                        existing_product = product
                                        break

                                if existing_product is not None:
                                    existing_product['quantity'] += 1
                                    existing_product['total'] = existing_product['quantity'] * existing_product['pr_price']
                                    existing_product['html'] = render_template('/widget/card-products-cart.html', pr_id=existing_product['pr_id'], pr_img = f'/static/img/product/{existing_product["pr_id"]}.jpg', pr_name=existing_product['pr_name'], br_name=existing_product['br_name'], pr_barcode=existing_product['pr_barcode'], pr_model=existing_product['pr_model'], pr_price=existing_product['pr_price'], pr_price_2=existing_product['pr_price_2'], pr_cost=existing_product['pr_cost'], pr_pricetopayments=existing_product['pr_pricetopayments'], quantity=existing_product['quantity'], total=existing_product['total'])
                                else:
                                    new_product = {
                                        'pr_id': pr_product['pr_id'],
                                        'pr_img': f'/static/img/product/{pr_product["pr_id"]}.jpg',
                                        'pr_barcode': pr_product['pr_barcode'],
                                        'pr_name': pr_product['pr_name'],
                                        'pr_model': pr_product['pr_model'],
                                        'pr_price': pr_product['pr_price'],
                                        'pr_price_2': pr_product['pr_price'],
                                        'pr_cost': pr_product['pr_cost'],
                                        'pr_pricetopayments': pr_product['pr_pricetopayments'],
                                        'br_name': pr_product['br_name'],
                                        'quantity': 1,
                                        'total': pr_product['pr_price'],
                                        'html': render_template('/widget/card-products-cart.html', pr_id=pr_product['pr_id'], pr_img = f'/static/img/product/{pr_product["pr_id"]}.jpg', pr_name=pr_product['pr_name'], br_name=pr_product['br_name'], pr_barcode=pr_product['pr_barcode'], pr_model=pr_product['pr_model'], pr_price=pr_product['pr_price'], pr_price_2=pr_product['pr_price'], pr_cost=pr_product['pr_cost'], pr_pricetopayments=pr_product['pr_pricetopayments'], quantity=1, total=pr_product['pr_price'])
                                    }
                                    info['products'].append(new_product)

                                token = serializer.dumps(info)
                                response = make_response(json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}))
                                response.set_cookie('posinfo', token)

                                return response
                        elif v_apiurlsplit[3] == 'finalize' and v_apiurlsplit[4] is None:
                            sa_pay = v_requestform.get('pay')
                            if not sa_pay:
                                return json.dumps({'success': False, 'msg': '¡El pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                                
                            elif not api_isFloat(sa_pay) or float(sa_pay) < 0:
                                return json.dumps({'success': False, 'msg': '¡El pago no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                            sa_pay = float(sa_pay)

                            token = request.cookies.get('posinfo')
                            serializer = URLSafeSerializer(app.secret_key)
                            info = None
                            try:
                                info = serializer.loads(token)
                            except:
                                return json.dumps({'success': False, 'msg': '¡No se creó la venta! Póngase en contacto con un soporte técnico.'})

                            ts_amountpayments = info['typesale']['ts_amountpayments']
                            if not ts_amountpayments:
                                ts_amountpayments = 1

                            ts_firstpayment = info['typesale']['ts_firstpayment']
                            if not ts_firstpayment:
                                ts_firstpayment = 0

                            ts_days = info['typesale']['ts_days']
                            if not ts_days:
                                ts_days = 0

                            cu_id = info['customer']['cu_id']
                            if cu_id == 'N/A' or cu_id == 0:
                                cu_id = None

                            sa_id = str(uuid.uuid4())
                            lo_id = info['location']['lo_id']
                            ts_id = info['typesale']['ts_id']
                            pm_id = info['paymentmethod']['pm_id']
                            sp_no = 0
                            commission = float(info['commission'])
                            sp_limitdate = datetime.now()
                            sa_pay = sa_pay - commission

                            total = float(info['subtotal']) - float(info['discount'])

                            sa_regdate = v_datetimenow
                            if ts_id == 1003 or ts_id == 1004:
                                sa_no = None
                                sa_regdate = None
                            else:
                                sa_no = sa_sales_model().get_sale(get = 'max_sa_no')['max_sa_no'] + 1
                           
                            sa_sales_model().insert_sale(sa_id = sa_id, sa_no = sa_no, sa_subtotal = info['subtotal'], sa_discount = info['discount'], sa_amountpayments = ts_amountpayments, sa_days = ts_days, sa_regdate = sa_regdate, lo_id = lo_id, ts_id = ts_id, cu_id = cu_id, us_id = session['us_id'])

                            for product in info['products']:
                                sd_saledetails_model().insert_saledetail(sd_price = product['pr_price'], sd_cost = product['pr_cost'], sd_quantity = product['quantity'], pr_id = product['pr_id'], sa_id = sa_id)

                            if ts_id == 1002 or ts_id == 1004:
                                ts_ab_del = 0
                                if ts_firstpayment > 0:
                                    ts_ab_del = 1
                                    sp_no = sp_salepayments_model().get_salepayment(get = 'max_sp_no')['max_sp_no'] + 1
                                    total = total - ts_firstpayment
                                    sp_salepayments_model().insert_salepayment(sp_no = sp_no, sp_subtotal = ts_firstpayment, sp_commission = commission, sp_pay = ts_firstpayment, sp_limitdate = sp_limitdate, sp_regdate = sp_limitdate, pm_id = pm_id, us_id = session['us_id'], sa_id = sa_id)

                                ts_amountpayments = ts_amountpayments - ts_ab_del
                                sp_subtotal = math.floor(total / ts_amountpayments)
                                for i in range(ts_amountpayments - 1): 
                                    sp_limitdate = api_get_next_month_day(sp_limitdate, ts_days)

                                    sp_salepayments_model().insert_salepayment(sp_subtotal = sp_subtotal, sp_commission = 0, sp_pay = 0, sp_limitdate = sp_limitdate, sp_regdate = None, pm_id = None, us_id = None, sa_id = sa_id)
                                
                                sp_limitdate = api_get_next_month_day(sp_limitdate, ts_days)
                                sp_subtotal = total - (sp_subtotal * (ts_amountpayments - 1))
                                sp_salepayments_model().insert_salepayment(sp_subtotal = sp_subtotal, sp_commission = 0, sp_pay = 0, sp_limitdate = sp_limitdate, sp_regdate = None, pm_id = None, us_id = None, sa_id = sa_id)

                            else:
                                sp_regdate = sp_limitdate
                                sp_limitdate = api_get_next_month_day(sp_limitdate, ts_days)

                                new_pay = total + commission
                                us_id = session['us_id']
                                if ts_id == 1003:
                                    sp_no = None
                                    sp_regdate = None
                                    new_pay = 0
                                    commission = 0
                                    pm_id = None    
                                    us_id = None                                
                                else:
                                    sp_no = sp_salepayments_model().get_salepayment(get = 'max_sp_no')['max_sp_no'] + 1

                                sp_salepayments_model().insert_salepayment(sp_no = sp_no, sp_subtotal = total, sp_commission = commission, sp_pay = new_pay, sp_limitdate = sp_limitdate, sp_regdate = sp_regdate, pm_id = pm_id, us_id = us_id, sa_id = sa_id)

                            response = make_response(json.dumps({'success': True, 'msg': '¡Se finalizó correctamente!', 'sa_id': sa_id, 'sp_no': sp_no}))
                            response.delete_cookie('posinfo')

                            return response
                    
                    #MANAGE
                    elif v_apiurlsplit[2] == 'manage':
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
                                    status = "" 
                                    if user['us_status'] == 1:
                                        status = "checked"

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{user["us_id"]}</span>',
                                        'fullname': user['pe_fullname'],
                                        'email': user['pe_email'],
                                        'membership': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{user["mem_name"]}</span>',        
                                        'phone': user['pe_phone'], 
                                    }
                                    
                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" us_id="{user["us_id"]}" onclick="check_status_user(this)" {status}></div>'
                                    
                                    response['regdate'] = str(user['us_regdate'].strftime('%d/%m/%Y %H:%M'))

                                    response['actions'] = f'<button class="btn btn-primary" user="{escape(json.dumps(response))}" user_permissions="{user["us_permissions"]}" onclick="edit_user(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button> <a class="btn btn-light" href="/pos/manage/addresses/{user["pe_id"]}"><i data-acorn-icon="news" data-acorn-size="16"></i> Direcciones</a>'

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
                                
                                us_id = us_users_model().gen_user_id()
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
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                us_id = v_requestform.get('us_id')
                                if not us_id:
                                    return json.dumps({'success': False, 'msg': '¡El usuario está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif us_users_model().get_user(us_id=us_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El usuario no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                us_status = v_requestform.get('us_status')
                                if not us_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not us_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                us_users_model().update_user(update='status', us_status=us_status, us_id=us_id)
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
                                        'phone': customer['pe_phone'],
                                        'dpi': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{customer["cu_dpi"]}</span>',
                                        'email': customer['pe_email'],                                                             
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" cu_id="{customer["cu_id"]}" onclick="check_status_customer(this)" {status}></div>'
                                    response['regdate'] = str(customer['cu_regdate'].strftime('%d/%m/%Y %H:%M'))
                                    response['actions'] = f'<button class="btn btn-primary" customer="{escape(json.dumps(response))}" onclick="edit_customer(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button> <a class="btn btn-light" href="/pos/manage/addresses/{customer["pe_id"]}"><i data-acorn-icon="news" data-acorn-size="16"></i> Direcciones</a>'

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
                                
                                cu_dpi = v_requestform.get('cu_dpi')
                                if not cu_dpi:
                                    return json.dumps({'success': False, 'msg': '¡El DPI está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_id = cu_customers_model().gen_customer_id()

                                cu_customers_model().insert_customer(cu_id=cu_id, fullname=pe_fullname, email=pe_email, phone=pe_phone, cu_dpi=cu_dpi)
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

                                cu_dpi = v_requestform.get('cu_dpi')
                                if not cu_dpi:
                                    return json.dumps({'success': False, 'msg': '¡El DPI está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                cu_customers_model().update_customer(update='all', cu_id=cu_id, pe_fullname=pe_fullname, pe_email=pe_email, pe_phone=pe_phone, cu_dpi=cu_dpi)
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
                                        'pricetopayments': product['pr_pricetopayments'],
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" pr_id="{product["pr_id"]}" onclick="check_status_product(this)" {status}></div>'
                                    response['regdate'] = str(product['pr_regdate'].strftime('%d/%m/%Y %H:%M'))
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
                                
                                pr_pricetopayments = v_requestform.get('pr_pricetopayments')
                                if not pr_pricetopayments:
                                    return json.dumps({'success': False, 'msg': '¡El precio de abono está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_pricetopayments):
                                    return json.dumps({'success': False, 'msg': '¡El precio de abono no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
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

                                pr_products_model().insert_product(pr_id = pr_id, pr_barcode = pr_barcode, pr_name = pr_name, pr_model = pr_model, pr_description = pr_description, pr_cost = pr_cost, pr_price = pr_price, pr_pricetopayments = pr_pricetopayments, ca_id = ca_id, br_id = br_id, pv_id = pv_id)
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

                                pr_pricetopayments = v_requestform.get('pr_pricetopayments')
                                if not pr_pricetopayments:
                                    return json.dumps({'success': False, 'msg': '¡El precio de abono está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not api_isFloat(pr_pricetopayments):
                                    return json.dumps({'success': False, 'msg': '¡El precio de abono no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
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

                                pr_products_model().update_product(update='all', pr_id = pr_id, pr_barcode = pr_barcode, pr_name = pr_name, pr_model = pr_model, pr_description = pr_description, pr_cost = pr_cost, pr_price = pr_price, pr_pricetopayments = pr_pricetopayments, ca_id = ca_id, br_id = br_id, pv_id = pv_id)
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
                                    response['regdate'] = str(provider['pv_regdate'].strftime('%d/%m/%Y %H:%M'))
                                    response['actions'] = f'<button class="btn btn-primary" provider="{escape(json.dumps(response))}" onclick="edit_provider(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button> <a class="btn btn-light" href="/pos/manage/addresses/{provider["pe_id"]}"><i data-acorn-icon="news" data-acorn-size="16"></i> Direcciones</a>'

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
                        elif v_apiurlsplit[3] == 'cities':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/cities'):
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
                                cities = ci_cities_model().get_cities(get='table', page_start=page_start, quantity = quantity, search = search)
                                for city in cities:
                                    status = "" 
                                    if city['ci_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{city["ci_id"]}</span>',
                                        'name': city['ci_name'],
                                        'state': city['st_name']
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" ci_id="{city["ci_id"]}" onclick="check_status_city(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" city="{escape(json.dumps(response))}" onclick="edit_city(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                cities_total = ci_cities_model().get_cities_count(get='table', search=search)
                                total_pages = math.ceil(cities_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                ci_id = v_requestform.get('ci_id')
                                if not ci_id:
                                    return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif ci_cities_model().get_city(ci_id=ci_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El municipio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                ci_name = v_requestform.get('ci_name')
                                if not ci_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                ci_name = ci_name.strip().capitalize()
                                
                                st_name = v_requestform.get('st_name')
                                if not st_name:
                                    return json.dumps({'success': False, 'msg': '¡El estado está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                
                                st_name = st_name.strip().capitalize() 
                                
                                st_id = None
                                while not st_id:
                                    result = st_states_model().get_state(get='name', st_name=st_name)
                                    if result:
                                        st_id = result['st_id']
                                    else:
                                        st_states_model().insert_state(st_name=st_name)

                                ci_cities_model().update_city(update='all', ci_name=ci_name, ci_id=ci_id, st_id=st_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                ci_id = v_requestform.get('ci_id')
                                if not ci_id:
                                    return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif ci_cities_model().get_city(ci_id=ci_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El municipio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                ci_status = v_requestform.get('ci_status')
                                if not ci_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not ci_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                ci_cities_model().update_city(update='status', ci_status=ci_status, ci_id=ci_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'states':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/states'):
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
                                states = st_states_model().get_states(get='table', page_start=page_start, quantity = quantity, search = search)
                                for state in states:
                                    status = "" 
                                    if state['st_status'] == 1:
                                        status = "checked" 

                                    response = {
                                        'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{state["st_id"]}</span>',
                                        'name': state['st_name']
                                    }

                                    response['status'] =  f'<div class="form-check form-switch"><input class="form-check-input" type="checkbox" st_id="{state["st_id"]}" onclick="check_status_state(this)" {status}></div>'
                                    response['actions'] = f'<button class="btn btn-primary" state="{escape(json.dumps(response))}" onclick="edit_state(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button>'

                                    table.append(response)
                                
                                states_total = st_states_model().get_states_count(get='table', search=search)
                                total_pages = math.ceil(states_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                            elif v_apiurlsplit[4] == 'edit' and v_apiurlsplit[5] is None:
                                st_id = v_requestform.get('st_id')
                                if not st_id:
                                    return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif st_states_model().get_state(st_id=st_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El municipio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                st_name = v_requestform.get('st_name')
                                if not st_name:
                                    return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjalo y vuelva a intentarlo.'})

                                st_states_model().update_state(update='all', st_name=st_name, st_id=st_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                            elif v_apiurlsplit[4] == 'status' and v_apiurlsplit[5] is None:
                                st_id = v_requestform.get('st_id')
                                if not st_id:
                                    return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif st_states_model().get_state(st_id=st_id) is None:
                                    return json.dumps({'success': False, 'msg': '¡El municipio no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                st_status = v_requestform.get('st_status')
                                if not st_status:
                                    return json.dumps({'success': False, 'msg': '¡El estatus está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                elif not st_status.isnumeric():
                                    return json.dumps({'success': False, 'msg': '¡El estatus no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                st_states_model().update_state(update='status', st_status=st_status, st_id=st_id)
                                return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'addresses':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/brands'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            pe_id = v_apiurlsplit[4]
                            if pe_persons_model().get_person(pe_id=pe_id):                                
                                if v_apiurlsplit[5] == 'table' and v_apiurlsplit[6] is None:  
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
                                    addresses = ad_addresses_model().get_addresses(get='tableperson', pe_id=pe_id, page_start=page_start, quantity = quantity, search = search)
                                    for address in addresses:
                                        response = {
                                            'id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px; width: 100px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{address["ad_id"]}</span>',
                                            'type': address['at_name'],
                                            'dpi': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{address["ad_dpi"]}</span>',
                                            'fullname': address['ad_fullname'],
                                            'phone': address['ad_phone'],
                                            'address': address['ad_address'],
                                            'relationship': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{address["ad_relationship"]}</span>',
                                            'city': address['ci_name'],
                                            'state': address['st_name'],  
                                            'workaddress': address['ad_workaddress'],                                                                                      
                                        }
                                        
                                        response['actions'] = f'<button class="btn btn-primary" address="{escape(json.dumps(response))}" onclick="edit_address(this);"><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button> <button class="btn btn-danger" ad_id="{address["ad_id"]}" onclick="delete_address(this);"><i data-acorn-icon="close" data-acorn-size="16"></i> Eliminar</button>'

                                        table.append(response)
                                    
                                    addresses_total = ad_addresses_model().get_addresses_count(get='tableperson', pe_id=pe_id, search=search)
                                    total_pages = math.ceil(addresses_total / quantity)

                                    return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                                elif v_apiurlsplit[5] == 'add' and v_apiurlsplit[6] is None:  
                                    at_id = v_requestform.get('at_id')
                                    if not at_id:
                                        return json.dumps({'success': False, 'msg': '¡El tipo de dirección está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    elif not at_addresstypes_model().get_addresstype(at_id = at_id):
                                        return json.dumps({'success': False, 'msg': '¡El tipo de dirección no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                    ad_address = v_requestform.get('ad_address')
                                    if not ad_address:
                                        return json.dumps({'success': False, 'msg': '¡La dirección está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                    ad_relationship = v_requestform.get('ad_relationship')
                                    if not ad_relationship:
                                        return json.dumps({'success': False, 'msg': '¡El Parentesco está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    
                                    ad_relationship = ad_relationship.strip().capitalize() 

                                    st_name = v_requestform.get('st_name')
                                    if not st_name:
                                        return json.dumps({'success': False, 'msg': '¡El estado está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    ad_dpi = v_requestform.get('ad_dpi')
                                    if not ad_dpi:
                                        return json.dumps({'success': False, 'msg': '¡El DPI está vacío! Por favor, corríjala y vuelva a intentarlo.'})

                                    ad_fullname = v_requestform.get('ad_fullname')
                                    if not ad_fullname:
                                        return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    ad_fullname = ad_fullname.strip().title() 
                                    
                                    ad_phone = v_requestform.get('ad_phone')
                                    if not ad_phone:
                                        return json.dumps({'success': False, 'msg': '¡El telefono está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    ad_workaddress = v_requestform.get('ad_workaddress')
                                    if not ad_workaddress:
                                        return json.dumps({'success': False, 'msg': '¡La dirección laboral está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                    st_name = st_name.strip().capitalize() 
                                    
                                    st_id = None
                                    while not st_id:
                                        result = st_states_model().get_state(get='name', st_name=st_name)
                                        if result:
                                            st_id = result['st_id']
                                        else:
                                            st_states_model().insert_state(st_name=st_name)
                                    
                                    ci_name = v_requestform.get('ci_name')
                                    if not ci_name:
                                        return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    
                                    ci_name = ci_name.strip().capitalize() 
                                    
                                    ci_id = None
                                    while not ci_id:
                                        result = ci_cities_model().get_city(get='nameandstate', ci_name=ci_name, st_name=st_name)
                                        if result:
                                            ci_id = result['ci_id']
                                        else:
                                            ci_cities_model().insert_city(ci_name=ci_name, st_id=st_id)

                                    ad_address = ad_address.strip().capitalize()  
                                    ad_workaddress = ad_workaddress.strip().capitalize()

                                    ad_addresses_model().insert_address(at_id = at_id, ad_address = ad_address, ad_relationship = ad_relationship, ad_dpi = ad_dpi, ad_fullname = ad_fullname, ad_phone = ad_phone, ad_workaddress = ad_workaddress, ci_id = ci_id, pe_id = pe_id)
                                    return json.dumps({'success': True, 'msg': '¡Se agregó correctamente!'}) 
                                elif v_apiurlsplit[5] == 'edit' and v_apiurlsplit[6] is None:
                                    ad_id = v_requestform.get('ad_id')
                                    if not ad_id:
                                        return json.dumps({'success': False, 'msg': '¡El ID está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    if not ad_addresses_model().get_address(ad_id = ad_id, pe_id = pe_id):
                                        return json.dumps({'success': False, 'msg': '¡El ID no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                    
                                    at_id = v_requestform.get('at_id')
                                    if not at_id:
                                        return json.dumps({'success': False, 'msg': '¡El tipo de dirección está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    elif not at_addresstypes_model().get_addresstype(at_id = at_id):
                                        return json.dumps({'success': False, 'msg': '¡El tipo de dirección no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                             
                                    ad_address = v_requestform.get('ad_address')
                                    if not ad_address:
                                        return json.dumps({'success': False, 'msg': '¡La dirección está vacía! Por favor, corríjala y vuelva a intentarlo.'})

                                    ad_relationship = v_requestform.get('ad_relationship')
                                    if not ad_relationship:
                                        return json.dumps({'success': False, 'msg': '¡El Parentesco está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    
                                    ad_relationship = ad_relationship.strip().capitalize() 
                                    
                                    ad_dpi = v_requestform.get('ad_dpi')
                                    if not ad_dpi:
                                        return json.dumps({'success': False, 'msg': '¡El DPI está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    ad_fullname = v_requestform.get('ad_fullname')
                                    if not ad_fullname:
                                        return json.dumps({'success': False, 'msg': '¡El nombre está vacío! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    ad_fullname = ad_fullname.strip().title() 
                                    
                                    ad_phone = v_requestform.get('ad_phone')
                                    if not ad_phone:
                                        return json.dumps({'success': False, 'msg': '¡El telefono está vacío! Por favor, corríjala y vuelva a intentarlo.'})

                                    st_name = v_requestform.get('st_name')
                                    if not st_name:
                                        return json.dumps({'success': False, 'msg': '¡El estado está vacío! Por favor, corríjala y vuelva a intentarlo.'})

                                    ad_workaddress = v_requestform.get('ad_workaddress')
                                    if not ad_workaddress:
                                        return json.dumps({'success': False, 'msg': '¡La dirección laboral está vacía! Por favor, corríjala y vuelva a intentarlo.'})
                                    
                                    st_name = st_name.strip().capitalize() 
                                    
                                    st_id = None
                                    while not st_id:
                                        result = st_states_model().get_state(get='name', st_name=st_name)
                                        if result:
                                            st_id = result['st_id']
                                        else:
                                            st_states_model().insert_state(st_name=st_name)
                                    
                                    ci_name = v_requestform.get('ci_name')
                                    if not ci_name:
                                        return json.dumps({'success': False, 'msg': '¡El municipio está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    
                                    ci_name = ci_name.strip().capitalize() 
                                    
                                    ci_id = None
                                    while not ci_id:
                                        result = ci_cities_model().get_city(get='nameandstate', ci_name=ci_name, st_name=st_name)
                                        if result:
                                            ci_id = result['ci_id']
                                        else:
                                            ci_cities_model().insert_city(ci_name=ci_name, st_id=st_id)

                                    ad_address = ad_address.strip().capitalize()
                                    ad_workaddress = ad_workaddress.strip().capitalize()

                                    ad_addresses_model().update_address(update = 'all', at_id = at_id, ad_address = ad_address, ad_relationship = ad_relationship, ad_dpi = ad_dpi, ad_fullname = ad_fullname, ad_phone = ad_phone, ad_workaddress = ad_workaddress, ci_id = ci_id, ad_id = ad_id)
                                    return json.dumps({'success': True, 'msg': '¡Se editó correctamente!'}) 
                                elif v_apiurlsplit[5] == 'delete' and v_apiurlsplit[6] is None:
                                    ad_id = v_requestform.get('ad_id')
                                    if not ad_id:
                                        return json.dumps({'success': False, 'msg': '¡El ID está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    if not ad_addresses_model().get_address(ad_id = ad_id, pe_id = pe_id):
                                        return json.dumps({'success': False, 'msg': '¡El ID no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                    ad_addresses_model().update_address(update='status', ad_status=0, ad_id=ad_id)
                                    return json.dumps({'success': True, 'msg': '¡Se eliminó correctamente!'}) 
                        elif v_apiurlsplit[3] == 'sales':
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sales'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            if (v_apiurlsplit[4] == 'table' and v_apiurlsplit[5] is None) or (v_apiurlsplit[4] == 'late' and v_apiurlsplit[5] == 'table' and v_apiurlsplit[6] is None) or (v_apiurlsplit[4] == 'cancel' and v_apiurlsplit[5] == 'table' and v_apiurlsplit[6] is None):
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

                                if v_apiurlsplit[4] == 'late':
                                    sales = []
                                    salepayments = sp_salepayments_model().get_salepayments(get = 'limitdate')
                                    for salepayment in salepayments:
                                        sales.append(sa_sales_model().get_sale(get = 'sa_id', sa_id = salepayment['sa_id']))
                                elif v_apiurlsplit[4] == 'cancel':
                                    sales = sa_sales_model().get_sales(get='table,status', sa_status = 0, page_start=page_start, quantity = quantity, search = search)
                                else:
                                    sales = sa_sales_model().get_sales(get='table', page_start=page_start, quantity = quantity, search = search)

                                for sale in sales:
                                    customer = f'({sale["cu_id"]})<br>{sale["cu_pe_fullname"]}'
                                    if not sale["cu_id"]:
                                        customer = 'N/A' 

                                    salepayments = sp_salepayments_model().get_salepayments(get = 'sa_id', sa_id = sale['sa_id'])
                                                                   
                                    sp_limitdates = []
                                    days_difference = 0
                                    for salepayment in salepayments:
                                        if salepayment['sp_pay'] < salepayment['sp_subtotal']:
                                            sp_limitdates.append(salepayment['sp_limitdate'])                                                                                
                                    
                                    sp_limitdate = None
                                    if sp_limitdates:
                                        sp_limitdate = min(sp_limitdates)

                                    if sp_limitdate:
                                        difference_date = sp_limitdate - v_date
                                        days_difference = difference_date.days
                                    
                                    total_pay = sum(salepayment['sp_pay'] for salepayment in salepayments)
                                    remainingpayment = (sale["sa_subtotal"] - sale["sa_discount"]) - total_pay
                                    if not sale["sa_status"]:
                                        alert = f'<span class="badge bg-dark fw-bold" style="font-size: 12px;">Cancelada</span>'
                                    elif sale["ts_id"] == 1001:
                                        alert = f'<span class="badge bg-white text-black fw-bold" style="font-size: 12px;">Pagado</span>'
                                    elif remainingpayment <= 0:
                                        alert = f'<span class="badge bg-white text-black fw-bold" style="font-size: 12px;">Pagado</span>'
                                    elif days_difference < 0:
                                        alert = f'<span class="badge bg-danger fw-bold" style="font-size: 12px;">Alerta ({days_difference})</span>'
                                    elif days_difference < 6:
                                        alert = f'<span class="badge bg-warning fw-bold text-black" style="font-size: 12px;">Medio ({days_difference})</span>'
                                    else:
                                        alert = f'<span class="badge bg-success fw-bold" style="font-size: 12px;">Bajo ({days_difference})</span>'
                                    
                                    sa_regdate = "N/A"
                                    if sale['sa_regdate']:
                                        sa_regdate = str(sale['sa_regdate'].strftime('%d/%m/%Y %H:%M'))

                                    response = {
                                        'alert': alert,
                                        'sa_no': sale['sa_no'],
                                        'remainingpayment': remainingpayment,
                                        'lo_name': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{sale["lo_name"]}</span>',
                                        'sa_regdate': sa_regdate,
                                        'ts_name': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{sale["ts_name"]}</span>',
                                        'sa_subtotal': f'Q{sale["sa_subtotal"]}',
                                        'sa_discount': f'-Q{sale["sa_discount"]}',
                                        'total': f'Q{sale["sa_subtotal"] - sale["sa_discount"]}',
                                        'customer': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{customer}</span>',
                                        'sa_amountpayments': sale['sa_amountpayments'],
                                        'sa_days': sale['sa_days'],
                                        'user': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">({sale["us_id"]})<br>{sale["us_pe_fullname"]}</span>',
                                    }

                                    actions = ''
                                    if sale["sa_status"]:
                                        actions = f'<a class="btn btn-primary mb-1" href="/pos/manage/sale/{sale["sa_id"]}/payments"><i data-acorn-icon="dollar" data-acorn-size="16"></i> Pago(s)</a>'
                                        
                                        actions = actions + f' <button class="btn btn-danger mb-1" sa_id="{sale["sa_id"]}" onclick="cancel_sale(this);"><i data-acorn-icon="close" data-acorn-size="16"></i> Cancelar</button>'
                                        actions = actions + f' <a class="btn btn-dark text-white mb-1" href="/api/web/pos/app/ticket/{sale["sa_id"]}" lv="1"><i data-acorn-icon="link" data-acorn-size="16"></i> Ticket</a>'
                                        actions = actions + f' <a class="btn btn-light text-black mb-1" href="/api/web/pos/app/invoice/{sale["sa_id"]}" lv="1"><i data-acorn-icon="link" data-acorn-size="16"></i> Factura</a>'
                                    
                                    response['actions'] = actions

                                    table.append(response)
                                
                                if v_apiurlsplit[4] == 'late':
                                    sales_total = 10
                                else:
                                    sales_total = sa_sales_model().get_sales_count(get='table', search=search)
                                
                                total_pages = math.ceil(sales_total / quantity)

                                return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages})
                            elif v_apiurlsplit[4] == 'cancel' and v_apiurlsplit[5] is None:
                                    sa_id = v_requestform.get('sa_id')
                                    if not sa_id:
                                        return json.dumps({'success': False, 'msg': '¡El ID está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                    sa_sale = sa_sales_model().get_sale(get = 'sa_id', sa_id = sa_id)
                                    if not sa_sale:
                                        return json.dumps({'success': False, 'msg': '¡El ID no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                    salepayments = sp_salepayments_model().get_salepayments(get = 'sa_id', sa_id = sa_id)
                                    total_pay = sum(salepayment['sp_pay'] for salepayment in salepayments)
                                    remainingpayment = sa_sale["sa_subtotal"] - total_pay

                                    sa_sales_model().update_sale(update='sa_status', sa_status=0, sa_id=sa_id)
                                    return json.dumps({'success': True, 'msg': '¡Se canceló correctamente!'})                        
                        elif v_apiurlsplit[3] == 'sale':
                            sa_id = v_apiurlsplit[4] 
                            sa_sale = sa_sales_model().get_sale(get = 'sa_id>sa_status', sa_id = sa_id, sa_status = 1)
                            if sa_sale:
                                if v_apiurlsplit[5] == 'payments':
                                    if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sale/payments'):
                                        return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 

                                    if v_apiurlsplit[6] == 'table' and v_apiurlsplit[7] is None: 
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
                                        payments = sp_salepayments_model().get_salepayments(get='table-sa_id', sa_id = sa_id, page_start=page_start, quantity = quantity, search = search)
                                        for payment in payments:
                                            sp_regdate = payment['sp_regdate']
                                            if not sp_regdate:
                                                sp_regdate = 'N/A'
                                            else:
                                                sp_regdate = payment['sp_regdate'].strftime("%d/%m/%Y %H:%M")
                                                

                                            sp_limitdate = payment['sp_limitdate']
                                            days_difference = 99                                 
                                            
                                            if sp_limitdate:
                                                difference_date = sp_limitdate - v_date
                                                days_difference = difference_date.days
                                            
                                            remainingpayment = payment['sp_subtotal'] - payment['sp_pay']
                                            if remainingpayment <= 0:
                                                color = 'dark'
                                            elif days_difference < 0:
                                                color = 'danger'
                                            elif days_difference < 6:
                                                color = f'warning text-black'
                                            else:
                                                color = f'success '
                                            
                                            paymentmethod = payment['pm_name']
                                            if not payment['pm_id']:
                                                paymentmethod = 'N/A'

                                            user = f'({payment["us_id"]})<br>{payment["pe_fullname"]}'
                                            if not payment['us_id']:
                                                user = 'N/A'
                                            
                                            sp_no = payment['sp_no']
                                            if not payment['sp_no']:
                                                sp_no = 'N/A'

                                            total_pay = sum(salepayment['sp_pay'] for salepayment in payments)
                                            remainingpayment = (sa_sale["sa_subtotal"] - sa_sale["sa_discount"]) - total_pay

                                            response = {
                                                'sp_id': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{payment["sp_id"]}</span>',
                                                'sp_no': sp_no,
                                                'sp_subtotal': f'Q{payment["sp_subtotal"]}',
                                                'sp_commission': f'Q{payment["sp_commission"]}',
                                                'total': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">Q{payment["sp_subtotal"] + payment["sp_commission"]}</span>',
                                                'sp_pay': f'Q{payment["sp_pay"]}',
                                                'totalremaining': f'<span class="badge bg-{color} fw-bold" style="font-size: 12px;">Q{(payment["sp_subtotal"]) - payment["sp_pay"]}</span>',
                                                'sp_limitdate':  f'<span>{payment["sp_limitdate"].strftime("%d/%m/%Y")}</span><br>({days_difference} días)',
                                                'pm_name': paymentmethod,
                                                'user': f'<span class="badge bg-primary fw-bold" style="font-size: 12px;">{user}</span>',
                                                'sp_regdate': str(sp_regdate),
                                            }
                                            
                                            if remainingpayment <= 0:
                                                actions = ''
                                            else:
                                                btn_disabled = ''
                                                if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sale/payments/edit'):
                                                    btn_disabled = 'disabled'

                                                actions = f'<button class="btn btn-primary mb-1" payment="{escape(json.dumps(response))}" onclick="edit_payment(this);" {btn_disabled}><i data-acorn-icon="edit" data-acorn-size="16"></i> Editar</button> <button class="btn btn-light mb-1" sp_id="{payment["sp_id"]}" onclick="split_payment(this);" {btn_disabled}><i data-acorn-icon="arrow-right" data-acorn-size="16"></i> Dividir</button>'
                                            
                                            actions = actions + f' <a class="btn btn-dark text-white mb-1" href="/api/web/pos/app/ticket/{sa_id}?no={payment["sp_no"]}" lv="1"><i data-acorn-icon="link" data-acorn-size="16"></i> Ticket</a>'
                                            response['actions'] = actions
                                            table.append(response)
                                        
                                        payments_total = sp_salepayments_model().get_salepayments_count(get='table-sa_id', sa_id = sa_id, search=search)
                                        total_pages = math.ceil(payments_total / quantity)

                                        return json.dumps({'success': True, 'html': render_template('/widget/table.html', table = table), "total_pages": total_pages}) 
                                    elif v_apiurlsplit[6] == 'add' and v_apiurlsplit[7] is None:
                                        amount = v_requestform.get('amount')
                                        if not amount:
                                            return json.dumps({'success': False, 'msg': '¡El abono está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                                
                                        elif not api_isFloat(amount) or float(amount) < 0:
                                            return json.dumps({'success': False, 'msg': '¡El abono no es válido! Por favor, corríjalo y vuelva a intentarlo.'})

                                        amount = float(amount)

                                        pay = v_requestform.get('pay')
                                        if not pay:
                                            return json.dumps({'success': False, 'msg': '¡El pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})                                
                                        elif not api_isFloat(pay) or float(pay) < 0:
                                            return json.dumps({'success': False, 'msg': '¡El pago no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                        
                                        pay = float(pay)

                                        pm_id = v_requestform.get('pm_id')
                                        if not pm_id:
                                            return json.dumps({'success': False, 'msg': '¡El método de pago está vacío! Por favor, corríjalo y vuelva a intentarlo.'})
                                        
                                        pm_paymentmethod = pm_paymentmethods_model().get_paymentmethod(pm_id)
                                        if pm_paymentmethod is None:
                                            return json.dumps({'success': False, 'msg': '¡El método de pago no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                        elif pm_paymentmethod['pm_status'] == 0:
                                            return json.dumps({'success': False, 'msg': '¡El método de pago esta prohibido! Por favor, corríjalo y vuelva a intentarlo.'})
                                        
                                        commission = amount * (pm_paymentmethod['pm_per'] / 100)

                                        salepayments = sp_salepayments_model().get_salepayments(get = 'where_sa_id,order_sp_limitdate_ASC', sa_id = sa_id)
                                        total_pay = sum(salepayment['sp_pay'] for salepayment in salepayments)
                                        remainingpayment = (sa_sale["sa_subtotal"] - sa_sale["sa_discount"]) - total_pay
                                        if remainingpayment <= 0:
                                            return json.dumps({'success': False, 'msg': '¡Esta venta ya fue abonada en su totalidad!'})       
                                        elif amount > remainingpayment:
                                            return json.dumps({'success': False, 'msg': '¡Pasa de la totalidad de deuda!'})     

                                        sp_no = 0
                                        dif_pay = 0
                                        rep = False
                                        ult = 1
                                        while True:                                            
                                            for index, salepayment in enumerate(salepayments):
                                                if not rep:
                                                    if salepayment['sp_pay'] < salepayment['sp_subtotal'] and amount > 0:
                                                        new_pay = salepayment['sp_pay'] + amount
                                                        if new_pay >= salepayment['sp_subtotal']:
                                                            dif_pay = amount - (salepayment['sp_subtotal'] - salepayment['sp_pay'])
                                                            sp_no = salepayment['sp_no']
                                                            if not sp_no:
                                                                sp_no = sp_salepayments_model().get_salepayment(get = 'max_sp_no')['max_sp_no'] + 1
                                                            
                                                            sp_salepayments_model().update_salepayment(update='pay', sp_no = sp_no, sp_subtotal = new_pay, sp_commission = commission, sp_pay = new_pay, pm_id = pm_id, us_id = session['us_id'], sp_id = salepayment['sp_id'])
                                                            amount = 0
                                                        else:
                                                            sp_no = salepayment['sp_no']
                                                            if not sp_no:
                                                                sp_no = sp_salepayments_model().get_salepayment(get = 'max_sp_no')['max_sp_no'] + 1
                                                            
                                                            sp_salepayments_model().update_salepayment(update='pay', sp_no = sp_no, sp_subtotal = salepayment['sp_subtotal'], sp_commission = commission, sp_pay = new_pay, pm_id = pm_id, us_id = session['us_id'], sp_id = salepayment['sp_id'])
                                                            amount = amount - new_pay
                                                    
                                                if (index == len(salepayments) - ult) and dif_pay > 0:
                                                    sp_subtotal = salepayment['sp_subtotal'] - dif_pay
                                                    if sp_subtotal > 0:
                                                        sp_salepayments_model().update_salepayment(update='pay', sp_no = salepayment['sp_no'], sp_subtotal = sp_subtotal, sp_commission = salepayment['sp_commission'], sp_pay = salepayment['sp_pay'], pm_id = salepayment['pm_id'], us_id = None, sp_id = salepayment['sp_id'])
                                                        dif_pay = 0
                                                    else:
                                                        sp_salepayments_model().update_salepayment(update='pay', sp_no = salepayment['sp_no'], sp_subtotal = 0, sp_commission = salepayment['sp_commission'], sp_pay = salepayment['sp_pay'], pm_id = salepayment['pm_id'], us_id = None, sp_id = salepayment['sp_id'])  
                                                        ult += 1   
                                                        rep = True
                                                        dif_pay = abs(salepayment['sp_subtotal'] - dif_pay)
                                            
                                            if dif_pay <= 0:
                                                break
                                        
                                        if sa_sale['ts_id'] == 1003 or sa_sale['ts_id'] == 1004:
                                            sa_no = sa_sale['sa_no']
                                            sa_regdate = sa_sale['sa_regdate']
                                            if not sa_no:
                                                sa_no = sa_sales_model().get_sale(get = 'max_sa_no')['max_sa_no'] + 1
                                            
                                            if not sa_regdate:
                                                sa_regdate = v_datetimenow

                                            sa_sales_model().update_sale(update='sa_no,sa_regdate', sa_no = sa_no, sa_regdate = sa_regdate, sa_id=sa_id)
                                        
                                        return json.dumps({'success': True, 'msg': '¡Se abonó correctamente!', 'sp_no': sp_no, 'dif_pay': dif_pay})
                                    elif v_apiurlsplit[6] == 'edit' and v_apiurlsplit[7] is None:
                                        if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sale/payments/edit'):
                                            return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                                    
                                        sp_id = v_requestform.get('sp_id')
                                        if not sp_id:
                                            return json.dumps({'success': False, 'msg': '¡El ID está vacío! Por favor, corríjalo y vuelva a intentarlo.'}) 
                                        
                                        sp_salepayment = sp_salepayments_model().get_salepayment(get = 'sp_id', sp_id = sp_id)
                                        if sp_salepayment is None:
                                            return json.dumps({'success': False, 'msg': '¡La ID no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                        sp_pay = v_requestform.get('sp_pay')
                                        if not sp_pay:
                                            return json.dumps({'success': False, 'msg': '¡El abono está vacío! Por favor, corríjalo y vuelva a intentarlo.'})   
                                        elif not api_isFloat(sp_pay) or float(sp_pay) < 0:
                                            return json.dumps({'success': False, 'msg': '¡El abono no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                        
                                        sp_pay = float(sp_pay)

                                        sp_limitdate = v_requestform.get('sp_limitdate')
                                        if not sp_limitdate:
                                            return json.dumps({'success': False, 'msg': '¡La fecha limite está vacía! Por favor, corríjala y vuelva a intentarlo.'})                                

                                        if sp_pay > sp_salepayment['sp_subtotal']:
                                            return json.dumps({'success': False, 'msg': '¡El abono supera el limite! Por favor, corríjalo y vuelva a intentarlo.'})   

                                        sp_salepayments_model().update_salepayment(update='edit', sp_pay = sp_pay, us_id = sp_salepayment['us_id'], sp_id = sp_id, sp_limitdate = sp_limitdate)

                                        return json.dumps({'success': True, 'msg': '¡Se abonó correctamente!'})
                                    elif v_apiurlsplit[6] == 'split' and v_apiurlsplit[7] is None:
                                        if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/sale/payments'):
                                            return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                                    
                                        sp_id = v_requestform.get('sp_id')
                                        if not sp_id:
                                            return json.dumps({'success': False, 'msg': '¡El ID está vacío! Por favor, corríjalo y vuelva a intentarlo.'}) 
                                        
                                        sp_salepayment = sp_salepayments_model().get_salepayment(get = 'sp_id', sp_id = sp_id)
                                        if sp_salepayment is None:
                                            return json.dumps({'success': False, 'msg': '¡La ID no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                
                                        sp_amount = v_requestform.get('sp_amount')
                                        if not sp_amount:
                                            return json.dumps({'success': False, 'msg': '¡El abono está vacío! Por favor, corríjalo y vuelva a intentarlo.'})   
                                        elif not api_isFloat(sp_amount) or float(sp_amount) < 0:
                                            return json.dumps({'success': False, 'msg': '¡El abono no es válido! Por favor, corríjalo y vuelva a intentarlo.'})
                                        
                                        sp_amount = float(sp_amount)

                                        sp_limitdate = v_requestform.get('sp_limitdate')
                                        if not sp_limitdate:
                                            return json.dumps({'success': False, 'msg': '¡La fecha limite está vacía! Por favor, corríjala y vuelva a intentarlo.'})                                

                                        if sp_amount > sp_salepayment['sp_subtotal']:
                                            return json.dumps({'success': False, 'msg': '¡El abono supera el limite! Por favor, corríjalo y vuelva a intentarlo.'})
                                        elif (sp_salepayment['sp_subtotal'] - sp_amount) < sp_salepayment['sp_pay']:
                                            return json.dumps({'success': False, 'msg': '¡El abono supera el limite! Por favor, corríjalo y vuelva a intentarlo.'})   
                                        
                                        sp_salepayments_model().insert_salepayment(sp_subtotal = sp_amount, sp_commission = 0, sp_pay = 0, sp_limitdate = sp_limitdate, sp_regdate = None, pm_id = None, us_id = None, sa_id = sa_id)

                                        new_subtotal = sp_salepayment['sp_subtotal'] - sp_amount
                                        sp_salepayments_model().update_salepayment(update='split', sp_subtotal = new_subtotal, sp_id = sp_id)

                                        return json.dumps({'success': True, 'msg': '¡Se abonó correctamente!'})
                        elif v_apiurlsplit[3] == 'dbbackup' and v_apiurlsplit[4] is None:
                            if not api_permissions_access(v_userinfo['us_permissions'], '/pos/manage/dbbackup'):
                                return json.dumps({'success': False, 'msg': '¡Acceso denegado! No tienes permiso.'}), 403 
                            
                            v_apidbbackup = api_dbbackup()
                            if not v_apidbbackup:
                                return json.dumps({'success': False, 'msg': 'No se pudo completar la copia de seguridad y la descarga.'}) 
                            
                            v_uuid = str(uuid.uuid4())
                            session[v_uuid] = 'mihogar-backup.sql'
                            return json.dumps({'success': True, 'url': f'/api/web/download/{v_uuid}'})  
                                 
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

@app.route('/api/web/pos/app/ticket/<sa_id>', methods = ['GET'])
def api_web_pos_app_ticket(sa_id):
    sa_sale = sa_sales_model().get_sale(get = 'sa_id', sa_id = sa_id)
    if sa_sale:
        sd_saledetails = sd_saledetails_model().get_saledetails(get = 'sa_id', sa_id = sa_id)
        sp_salepayments = sp_salepayments_model().get_salepayments(get = 'where_sa_id,order_sp_no_ASC', sa_id = sa_id)
        if sa_sale['ts_id'] == 1002 or  sa_sale['ts_id'] == 1004:            
            total_pay = sum(salepayment['sp_pay'] for salepayment in sp_salepayments)
            remainingpayment = (sa_sale["sa_subtotal"] - sa_sale["sa_discount"]) - total_pay
            
            return render_template('/pos/ticketpayments.html', sa_sale = sa_sale, sd_saledetails = sd_saledetails, sp_salepayments = sp_salepayments, remainingpayment = remainingpayment, total_pay = total_pay)
        
        return render_template('/pos/ticket.html', sa_sale = sa_sale, sd_saledetails = sd_saledetails, sp_salepayments = sp_salepayments)
    return json.dumps({'success': False, 'msg': 'Página no encontrada.'}), 404

@app.route('/api/web/pos/app/invoice/<sa_id>', methods = ['GET'])
def api_web_pos_app_invoice(sa_id):
    sa_sale = sa_sales_model().get_sale(get = 'sa_id', sa_id = sa_id)
    if sa_sale:
        sd_saledetails = sd_saledetails_model().get_saledetails(get = 'sa_id', sa_id = sa_id)
        sp_salepayments = sp_salepayments_model().get_salepayments(get = 'where_sa_id,order_sp_no_ASC', sa_id = sa_id)
        address = ad_addresses_model().get_addresses(get = 'person,ad_dpi', pe_id = sa_sale['cu_pe_id'], ad_dpi = sa_sale['cu_dpi'])
        if address:
            address = address[0]
        
         # Opciones de PDFKit
        options = {
            'encoding': 'UTF-8',
            'page-size': 'Letter',      
            'page-height': '14cm',      
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
            "enable-local-file-access": ""
        }

        # Generar el PDF como una cadena de bytes
        pdf_bytes = pdfkit.from_string(render_template('/pos/invoicepayments.html', sa_sale = sa_sale, sd_saledetails = sd_saledetails, sp_salepayments = sp_salepayments, address = address), False, options=options)

        # Crear la respuesta con el archivo PDF
        response = make_response(pdf_bytes)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename=factura-{sa_id}.pdf'

        return response
    return json.dumps({'success': False, 'msg': 'Página no encontrada.'}), 404

@app.route('/api/web/download/<download_uuid>', methods = ['GET'])
def api_web_download(download_uuid):
    try:
        if download_uuid not in session:
            return json.dumps({'success': False, 'msg': 'Descarga no encontrada.'}), 404
        
        fileName = session[download_uuid]

        backup_path = os.path.join('downloads', fileName)    
                        
        return send_file(backup_path, as_attachment=True)
    except:
        return json.dumps({'success': False, 'msg': 'Archivo no encontrado.'}), 404

@app.route('/auth/logout', methods = ['GET'])
def api_web_authlogout():  
    if 'sess_id' in session:
        sess_usersessions_model().remove_session(sess_id=session['sess_id'])
    
    response = make_response(redirect('/'))    
    response.delete_cookie('pos')
    response.delete_cookie('posinfo')
    session.clear()
    return response