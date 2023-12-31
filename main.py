from api_web import * 

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods = ['GET'])
def web_main(path):    
    v_apiurlsplit = [api_urlsplit(path, i) for i in range(10)]

    try:  
        v_datetimenow = datetime.now()      
        v_apiverifysession = api_verify_session()

        if v_apiverifysession == 0:
            return render_template("/auth/index.html", web_settings = web_settings)
       
        if v_apiurlsplit[0] == 'pos':
            v_userinfo = us_users_model().get_user(us_id=session['us_id'])
            v_usersession = sess_usersessions_model().get_session(sess_id=session['sess_id'])
            v_apipermissions = api_permissions(v_userinfo['mem_id'])
            
            if 111529 in v_apipermissions and v_userinfo['us_status'] == 1:
                return render_template("/pos/index.html", web_settings = web_settings, userinfo = v_userinfo, apipermissions = v_apipermissions) 
            else:
                return 'NO TIENES ACCESO'
        else:
            return redirect('/pos')       
    except Exception as e:        
        api_savelog('log/web-error.log', f'[E{sys.exc_info()[-1].tb_lineno}] {e}')
        return json.dumps({'success': False, 'msg': 'An error has occurred! Reported to all admins.'}), 500

@app.template_filter('format_currency')
def format_currency(value):
    locale.setlocale(locale.LC_ALL, '')
    formatted_value = '{:,.2f}'.format(value)
    return Markup(formatted_value)

@app.template_filter('getimgpr')
def getimgpr(value):
    return Markup(api_getimagedata(f'static/img/product/{value}.jpg'))

def task_onemin():
    with app.app_context():
        sess_usersessions_model().update_session(update='offline')        

scheduler = BackgroundScheduler()
scheduler.add_job(task_onemin, 'interval', minutes=1) #seconds=10 #minutes=1
scheduler.start()

if __name__ == '__main__':
    app.run(debug = app_debug)