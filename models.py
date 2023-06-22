from config import *

class us_users_model():
    def __init__(self):
        pass
    
    def get_user(self, select = None, id = None):
        cur = mysql.connection.cursor()
        
        if select == 'email':        
            cur.execute('SELECT us_users.*, pe_person.pe_email, pe_person.pe_fullname, pe_person.pe_phone FROM us_users INNER JOIN pe_person ON pe_person.pe_id = us_users.pe_id WHERE pe_person.pe_email = %s', (id,))
        elif select == 'emailornumid':        
            cur.execute('SELECT us_users.*, pe_person.pe_email, pe_person.pe_fullname, pe_person.pe_phone FROM us_users INNER JOIN pe_person ON pe_person.pe_id = us_users.pe_id WHERE pe_person.pe_email = %s OR us_users.us_id = %s', (id, id,))
        else:
            cur.execute('SELECT us_users.*, mem_memberships.mem_name, pe_person.pe_email, pe_person.pe_fullname, pe_person.pe_phone FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_person ON pe_person.pe_id = us_users.pe_id WHERE us_users.us_id = %s', (id,))

        data = cur.fetchone()
        cur.close()
        return data
    
    def get_users(self, select = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT us_users.*, pe_person.pe_email, pe_person.pe_fullname, pe_person.pe_phone, mem_memberships.mem_name FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_person ON pe_person.pe_id = us_users.pe_id WHERE us_users.us_id LIKE %s OR pe_person.pe_fullname LIKE %s OR pe_person.pe_email LIKE %s OR pe_person.pe_phone LIKE %s OR us_users.us_regdate LIKE %s OR mem_memberships.mem_name LIKE %s ORDER BY us_users.mem_id ASC LIMIT %s, %s',(like, like, like, like, like, like, page_start, quantity,))
        else:
            cur.execute('SELECT us_users.*, mem_memberships.mem_name FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_users_count(self, select = None, search = None):       
        cur = mysql.connection.cursor()

        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_person ON pe_person.pe_id = us_users.pe_id WHERE us_users.us_id LIKE %s OR pe_person.pe_fullname LIKE %s OR pe_person.pe_email OR pe_person.pe_phone LIKE %s LIKE %s OR us_users.us_regdate LIKE %s OR mem_memberships.mem_name LIKE %s',(like, like, like, like, like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_user(self, id = None, fullname = None, email = None, password = None, phone = None, mem_id = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO pe_person(pe_fullname, pe_email, pe_phone) VALUES(%s, %s, %s)', (fullname, email, phone,))
        pe_id = cur.lastrowid
        cur.execute('INSERT INTO us_users(us_id, us_password, mem_id, pe_id) VALUES(%s, %s, %s, %s)', (id, password, mem_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_user(self, update = None, id = None, fullname = None, email = None, password = None, phone = None, permissions = None, mem_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'password':        
            cur.execute('UPDATE us_users SET us_password = %s WHERE us_id = %s', (password, id,))
        elif update == 'all':  
            pe_id = us_users_model().get_user(id=id)['pe_id']
            cur.execute('UPDATE pe_person SET pe_fullname = %s, pe_email = %s, pe_phone = %s WHERE pe_id = %s', (fullname, email, phone, pe_id,))  
            cur.execute('UPDATE us_users SET us_password = %s, us_permissions = %s, mem_id = %s WHERE us_id = %s', (password, permissions, mem_id, id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class sess_usersessions_model():
    def __init__(self):
        pass

    def get_session(self, select = None, id = None):
        cur = mysql.connection.cursor()
        
        if select == 'user':        
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions WHERE sess_usersessions.us_id = %s', (id,))
        else:
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions WHERE sess_usersessions.sess_id = %s', (id,))

        data = cur.fetchone()
        cur.close()
        return data

    def get_sessions(self, select = None, online = None):
        cur = mysql.connection.cursor()
        
        if select == 'online':        
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions WHERE sess_online = %s', (online,))
        else:
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions')

        data = cur.fetchall()
        cur.close()
        return data
    
    def insert_session(self, sess_id, sess_useragent, us_id):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO sess_usersessions(sess_id, sess_useragent, us_id) VALUES(%s, %s, %s)', (sess_id, sess_useragent, us_id,))        
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_session(self, update = None, id = None, online = 0):
        cur = mysql.connection.cursor()
        
        if update == 'online':        
            cur.execute('UPDATE sess_usersessions SET sess_online = %s, sess_date = NOW() WHERE sess_id = %s', (online, id,))
        elif update == 'offline':  
            cur.execute('UPDATE sess_usersessions SET sess_online = 0 WHERE sess_date < NOW() - INTERVAL 2 MINUTE')
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

    def remove_session(self, delete = None, id = None):
        cur = mysql.connection.cursor()
        
        if delete == 'user':        
            cur.execute('DELETE FROM sess_usersessions WHERE us_id = %s', (id,))
        else:
            cur.execute('DELETE FROM sess_usersessions WHERE sess_id = %s', (id,))

        mysql.connection.commit()
        cur.close()
        return True

class mem_memberships_model():
    def __init__(self):
        pass
    
    def get_membership(self, id):
        cur = mysql.connection.cursor()       
        cur.execute('SELECT mem_memberships.* FROM mem_memberships WHERE mem_memberships.mem_id = %s', (id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_memberships(self):
        cur = mysql.connection.cursor()       
        cur.execute('SELECT mem_memberships.* FROM mem_memberships')
        data = cur.fetchall()
        cur.close()
        return data
    
class pm_paymentmethods_model():
    def __init__(self):
        pass
    
    def get_paymentmethod(self, id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id = %s', (id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_paymentmethods(self, select = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id LIKE %s OR pm_paymentmethods.pm_name LIKE %s ORDER BY pm_paymentmethods.pm_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_paymentmethods_count(self, select = None, search = None):       
        cur = mysql.connection.cursor()

        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id LIKE %s OR pm_paymentmethods.pm_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM pm_paymentmethods')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_paymentmethod(self, name = None, per = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO pm_paymentmethods(pm_name, pm_per) VALUES(%s, %s)', (name, per,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_paymentmethod(self, update = None, name = None, per = None, status = None, id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE pm_paymentmethods SET pm_name = %s, pm_per = %s WHERE pm_id = %s', (name, per, id,))
        elif update == 'status':        
            cur.execute('UPDATE pm_paymentmethods SET pm_status = %s WHERE pm_id = %s', (status, id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class lo_locations_model():
    def __init__(self):
        pass
    
    def get_location(self, id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_id = %s', (id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_locations(self, select = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_id LIKE %s OR lo_locations.lo_name LIKE %s ORDER BY lo_locations.lo_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT lo_locations.* FROM lo_locations')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_locations_count(self, select = None, search = None):       
        cur = mysql.connection.cursor()

        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM lo_locations WHERE lo_locations.lo_id LIKE %s OR lo_locations.lo_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM lo_locations')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_location(self, name = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO lo_locations(lo_name) VALUES(%s)', (name,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_location(self, update = None, name = None, status = None, id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE lo_locations SET lo_name = %s WHERE lo_id = %s', (name, id,))
        elif update == 'status':        
            cur.execute('UPDATE lo_locations SET lo_status = %s WHERE lo_id = %s', (status, id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class ca_categories_model():
    def __init__(self):
        pass
    
    def get_category(self, id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_id = %s', (id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_categories(self, select = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_id LIKE %s OR ca_categories.ca_name LIKE %s ORDER BY ca_categories.ca_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT ca_categories.* FROM ca_categories')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_categories_count(self, select = None, search = None):       
        cur = mysql.connection.cursor()

        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM ca_categories WHERE ca_categories.ca_id LIKE %s OR ca_categories.ca_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM ca_categories')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_category(self, name = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO ca_categories(ca_name) VALUES(%s)', (name,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_category(self, update = None, name = None, status = None, id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE ca_categories SET ca_name = %s WHERE ca_id = %s', (name, id,))
        elif update == 'status':        
            cur.execute('UPDATE ca_categories SET ca_status = %s WHERE ca_id = %s', (status, id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class br_brands_model():
    def __init__(self):
        pass
    
    def get_brand(self, id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_id = %s', (id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_brands(self, select = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_id LIKE %s OR br_brands.br_name LIKE %s ORDER BY br_brands.br_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT br_brands.* FROM br_brands')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_brands_count(self, select = None, search = None):       
        cur = mysql.connection.cursor()

        if select == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM br_brands WHERE br_brands.br_id LIKE %s OR br_brands.br_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM br_brands')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_brand(self, name = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO br_brands(br_name) VALUES(%s)', (name,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_brand(self, update = None, name = None, status = None, id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE br_brands SET br_name = %s WHERE br_id = %s', (name, id,))
        elif update == 'status':        
            cur.execute('UPDATE br_brands SET br_status = %s WHERE br_id = %s', (status, id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True