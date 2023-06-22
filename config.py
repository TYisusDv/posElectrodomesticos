from flask import Flask, render_template, request, redirect, url_for, session, escape, make_response, send_file
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect, generate_csrf
from datetime import datetime, timedelta
from passlib.hash import bcrypt
from itsdangerous import URLSafeSerializer
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
import json, uuid, requests, re, math, time, sys, hashlib, random, shutil, os, base64, subprocess, psutil, glob, arrow, socket

csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

app_local = False
hostname = socket.gethostname()

if hostname == "fedora":
    app_local = True

if app_local:
    db_user = 'root'
    db_password = '123456789'
    db_db = 'pos'
    app_link = 'http://127.0.0.1:5000'
    app_debug = True
else:
    db_user = 'enigmatm'
    db_password = 'eNigMAtm01TM@19#ByJNigHt&21'
    db_db = 'enigmatm'
    app_link = 'https://enigmatm.pro'
    app_debug = False

app.secret_key = "sEcrEr&#kEy@1902#TyIsusDv$#q12"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = db_user
app.config["MYSQL_PASSWORD"] = db_password
app.config["MYSQL_DB"] = db_db
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # URL de Redis
app.config['result_backend'] = 'redis://localhost:6379/0'  # URL de Redis
mysql = MySQL(app)

web_settings = {
    'name': 'Mi Hogar',
    'version': '1.0.0',
    'icon': '/static/img/icon.jpg',
    'logo': 'DevsFlex',
    'developer': 'DevsFlex',
    'description': 'Punto de venta desarrollado por Ing. Jesús Navarro Salcido.'
}

def api_verify_session():
    #0 = Not Logged
    #1 = Logged

    token = request.cookies.get('pos')
    serializer = URLSafeSerializer(app.secret_key)
    
    try:
        data = serializer.loads(token)
        session["us_id"] = data['us_id']
        session["sess_id"] = data['sess_id']
    except:
        pass

    if "us_id" not in session:
        session.clear()
        return 0
    
    if "sess_id" not in session:
        session.clear()
        return 0
    
    from models import sess_usersessions_model
    
    v_sess = sess_usersessions_model().get_session(id=session["sess_id"])
    if v_sess is None or v_sess["us_id"] != session["us_id"]:
        session.clear()
        return 0
    
    return 1
  
def api_urlsplit(path, n):
    try:
        return path.split("/")[n] if len(path.split("/")) > n else None
    except:
        return None

def api_emailvalid(email):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email) is not None

def api_savelog(name, text):
    try:
        folder_path = os.path.dirname(name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        with open(name, "a+") as f:
            f.write(f"{text}\n")
            
        return True
    except:
        return False

def api_hashbcrypt(passw):
    return bcrypt.hash(passw)

def api_verifybcrypt(passw, hash):
    return bcrypt.verify(passw, hash)

def api_genuniqueid():
    unique_id = str(uuid.uuid4().hex)[:16]
    return unique_id.upper()

def api_permissions(mem_id):
    #NORMAL
    listAccess = [665590]
    
    #EMPELADO
    if mem_id == 111529:
        listAccess = [111529, 665590]

    return listAccess

def api_permissions_access(permissions, module):
    if permissions:
        user_permissions = eval(permissions)
        if module not in user_permissions:
            return False
        
        return True
    else:
        return False

def api_isFloat(num):
    try:
        float(num)
        return True
    except:
        return False
    
def api_isBoolean(num):
    try:
        bool(num)
        return True
    except:
        return False

def api_getdevice(user_agent):
    regex = r'\((.*?)\)'
    match = re.search(regex, user_agent)
    if match:
        device_info = match.group(1)
        device_name = device_info.split(';')[0]
        try:
            device_name_1 = device_info.split(';')[1]
            device_name = f'{device_name_1}; {device_name}'
        except:
            pass
    else:
        device_name = 'Other'

    return device_name