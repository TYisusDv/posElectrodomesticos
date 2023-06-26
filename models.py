from config import *

class us_users_model():
    def __init__(self):
        pass
    
    def gen_user_id(self):
        unique_number = None
        cur = mysql.connection.cursor()
        while not unique_number:
            randomNumber = str(random.randint(100000, 999999))
            query = "SELECT us_id FROM us_users WHERE us_id = %s"
            cur.execute(query, (randomNumber,))
            result = cur.fetchone()
            if not result:
                unique_number = randomNumber
        cur.close()
        return unique_number

    def get_user(self, get = None, us_id = None, email = None):
        cur = mysql.connection.cursor()
        
        if get == 'email':        
            cur.execute('SELECT us_users.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM us_users INNER JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE pe_persons.pe_email = %s', (email,))
        elif get == 'emailornumid':        
            cur.execute('SELECT us_users.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM us_users INNER JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE pe_persons.pe_email = %s OR us_users.us_id = %s', (email, us_id,))
        else:
            cur.execute('SELECT us_users.*, mem_memberships.mem_name, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE us_users.us_id = %s', (us_id,))

        data = cur.fetchone()
        cur.close()
        return data
    
    def get_users(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT us_users.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone, mem_memberships.mem_name FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE us_users.us_id LIKE %s OR pe_persons.pe_fullname LIKE %s OR pe_persons.pe_email LIKE %s OR pe_persons.pe_phone LIKE %s OR us_users.us_regdate LIKE %s OR mem_memberships.mem_name LIKE %s ORDER BY us_users.mem_id ASC LIMIT %s, %s',(like, like, like, like, like, like, page_start, quantity,))
        else:
            cur.execute('SELECT us_users.*, mem_memberships.mem_name FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_users_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id INNER JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE us_users.us_id LIKE %s OR pe_persons.pe_fullname LIKE %s OR pe_persons.pe_email OR pe_persons.pe_phone LIKE %s LIKE %s OR us_users.us_regdate LIKE %s OR mem_memberships.mem_name LIKE %s',(like, like, like, like, like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM us_users INNER JOIN mem_memberships ON mem_memberships.mem_id = us_users.mem_id')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_user(self, us_id = None, fullname = None, email = None, password = None, phone = None, mem_id = None):
        cur = mysql.connection.cursor()       
        pe_id = str(uuid.uuid4())
        pe_persons_model().insert_person(pe_id = pe_id, pe_fullname = fullname, pe_email = email, pe_phone = phone)
        cur.execute('INSERT INTO us_users(us_id, us_password, mem_id, pe_id) VALUES(%s, %s, %s, %s)', (us_id, password, mem_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_user(self, update = None, us_id = None, fullname = None, email = None, password = None, phone = None, permissions = None, mem_id = None, us_status = None):
        cur = mysql.connection.cursor()
        
        if update == 'password':        
            cur.execute('UPDATE us_users SET us_password = %s WHERE us_id = %s', (password, us_id,))
        elif update == 'all':  
            pe_id = self.get_user(us_id=us_id)['pe_id']
            pe_persons_model().update_person(update = 'all', pe_id = pe_id, pe_fullname = fullname, pe_email = email, pe_phone = phone)  
            cur.execute('UPDATE us_users SET us_password = %s, us_permissions = %s, mem_id = %s WHERE us_id = %s', (password, permissions, mem_id, us_id,))
        elif update == 'status':  
            cur.execute('UPDATE us_users SET us_status = %s WHERE us_id = %s', (us_status, us_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class sess_usersessions_model():
    def __init__(self):
        pass

    def get_session(self, get = None, sess_id = None):
        cur = mysql.connection.cursor()
        
        if get == 'user':        
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions WHERE sess_usersessions.us_id = %s', (sess_id,))
        else:
            cur.execute('SELECT sess_usersessions.* FROM sess_usersessions WHERE sess_usersessions.sess_id = %s', (sess_id,))

        data = cur.fetchone()
        cur.close()
        return data

    def get_sessions(self, get = None, online = None):
        cur = mysql.connection.cursor()
        
        if get == 'online':        
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
    
    def update_session(self, update = None, sess_id = None, online = 0):
        cur = mysql.connection.cursor()
        
        if update == 'online':        
            cur.execute('UPDATE sess_usersessions SET sess_online = %s, sess_date = NOW() WHERE sess_id = %s', (online, sess_id,))
        elif update == 'offline':  
            cur.execute('UPDATE sess_usersessions SET sess_online = 0 WHERE sess_date < NOW() - INTERVAL 2 MINUTE')
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

    def remove_session(self, delete = None, sess_id = None):
        cur = mysql.connection.cursor()
        
        if delete == 'user':        
            cur.execute('DELETE FROM sess_usersessions WHERE us_id = %s', (sess_id,))
        else:
            cur.execute('DELETE FROM sess_usersessions WHERE sess_id = %s', (sess_id,))

        mysql.connection.commit()
        cur.close()
        return True

class mem_memberships_model():
    def __init__(self):
        pass
    
    def get_membership(self, mem_id):
        cur = mysql.connection.cursor()       
        cur.execute('SELECT mem_memberships.* FROM mem_memberships WHERE mem_memberships.mem_id = %s', (mem_id,))
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
    
    def get_paymentmethod(self, pm_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id = %s', (pm_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_paymentmethods(self, get = None, pm_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id LIKE %s OR pm_paymentmethods.pm_name LIKE %s ORDER BY pm_paymentmethods.pm_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'status':
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_status = %s', (pm_status,))
        else:
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_paymentmethods_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
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

    def update_paymentmethod(self, update = None, name = None, per = None, status = None, pm_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE pm_paymentmethods SET pm_name = %s, pm_per = %s WHERE pm_id = %s', (name, per, pm_id,))
        elif update == 'status':        
            cur.execute('UPDATE pm_paymentmethods SET pm_status = %s WHERE pm_id = %s', (status, pm_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class lo_locations_model():
    def __init__(self):
        pass
    
    def get_location(self, lo_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_id = %s', (lo_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_locations(self, get = None, lo_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_id LIKE %s OR lo_locations.lo_name LIKE %s ORDER BY lo_locations.lo_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'status':
            cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_status = %s',(lo_status,))
        else:
            cur.execute('SELECT lo_locations.* FROM lo_locations')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_locations_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
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

    def update_location(self, update = None, name = None, status = None, lo_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE lo_locations SET lo_name = %s WHERE lo_id = %s', (name, lo_id,))
        elif update == 'status':        
            cur.execute('UPDATE lo_locations SET lo_status = %s WHERE lo_id = %s', (status, lo_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class ca_categories_model():
    def __init__(self):
        pass
    
    def get_category(self, get = None, ca_id = None, ca_name = None):
        cur = mysql.connection.cursor()
        
        if get == 'name':
            cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_name = %s', (ca_name,))
        else:
            cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_id = %s', (ca_id,))
            
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_categories(self, get = None, ca_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_id LIKE %s OR ca_categories.ca_name LIKE %s ORDER BY ca_categories.ca_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'status':
            cur.execute('SELECT ca_categories.* FROM ca_categories WHERE ca_categories.ca_status = %s', (ca_status,))
        else:
            cur.execute('SELECT ca_categories.* FROM ca_categories')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_categories_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
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

    def update_category(self, update = None, name = None, status = None, ca_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE ca_categories SET ca_name = %s WHERE ca_id = %s', (name, ca_id,))
        elif update == 'status':        
            cur.execute('UPDATE ca_categories SET ca_status = %s WHERE ca_id = %s', (status, ca_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class br_brands_model():
    def __init__(self):
        pass
    
    def get_brand(self, get = None, br_id = None, br_name = None):
        cur = mysql.connection.cursor()
        
        if get == 'name':
            cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_name = %s', (br_name,))
        else:
            cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_id = %s', (br_id,))
            
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_brands(self, get = None, br_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_id LIKE %s OR br_brands.br_name LIKE %s ORDER BY br_brands.br_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'status':
            cur.execute('SELECT br_brands.* FROM br_brands WHERE br_brands.br_status = %s', (br_status,))
        else:
            cur.execute('SELECT br_brands.* FROM br_brands')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_brands_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
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

    def update_brand(self, update = None, name = None, status = None, br_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE br_brands SET br_name = %s WHERE br_id = %s', (name, br_id,))
        elif update == 'status':        
            cur.execute('UPDATE br_brands SET br_status = %s WHERE br_id = %s', (status, br_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class cu_customers_model():
    def __init__(self):
        pass
    
    def gen_customer_id(self):
        unique_number = None
        cur = mysql.connection.cursor()
        while not unique_number:
            randomNumber = str(random.randint(100000, 999999))
            query = "SELECT cu_id FROM cu_customers WHERE cu_id = %s"
            cur.execute(query, (randomNumber,))
            result = cur.fetchone()
            if not result:
                unique_number = randomNumber
        cur.close()
        return unique_number

    def get_customer(self, cu_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT cu_customers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id WHERE cu_customers.cu_id = %s', (cu_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_customers(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT cu_customers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id WHERE cu_customers.cu_id LIKE %s OR cu_customers.cu_regdate LIKE %s OR pe_persons.pe_email LIKE %s OR pe_persons.pe_fullname LIKE %s OR pe_persons.pe_phone LIKE %s ORDER BY cu_customers.cu_regdate DESC LIMIT %s, %s',(like, like, like, like, like, page_start, quantity,))
        else:
            cur.execute('SELECT cu_customers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_customers_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id WHERE cu_customers.cu_id LIKE %s OR cu_customers.cu_regdate LIKE %s OR pe_persons.pe_email LIKE %s OR pe_persons.pe_fullname LIKE %s OR pe_persons.pe_phone LIKE %s',(like, like, like, like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM cu_customers')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_customer(self, cu_id = None, fullname = None, email = None, phone = None):
        cur = mysql.connection.cursor()  
        pe_id = str(uuid.uuid4())
        pe_persons_model().insert_person(pe_id = pe_id, pe_fullname = fullname, pe_email = email, pe_phone = phone)
        cur.execute('INSERT INTO cu_customers(cu_id, pe_id) VALUES(%s, %s)', (cu_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_customer(self, update = None, cu_id = None, pe_fullname = None, pe_email = None, pe_phone = None, status = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            pe_id = self.get_customer(cu_id)['pe_id']
            pe_persons_model().update_person(update = 'all', pe_id = pe_id, pe_fullname = pe_fullname, pe_email = pe_email, pe_phone = pe_phone)
        elif update == 'status':        
            cur.execute('UPDATE cu_customers SET cu_status = %s WHERE cu_id = %s', (status, cu_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class pe_persons_model():
    def __init__(self):
        pass
    
    def get_person(self, get = None, pe_id = None):
        cur = mysql.connection.cursor()
        if get == 'email':
            cur.execute('SELECT pe_persons.* FROM pe_persons WHERE pe_persons.pe_email = %s', (pe_id,))
        else:
            cur.execute('SELECT pe_persons.* FROM pe_persons WHERE pe_persons.pe_id = %s', (pe_id,))
        data = cur.fetchone()
        cur.close()
        return data

    def insert_person(self, pe_id = None, pe_fullname = None, pe_email = None, pe_phone = None):
        cur = mysql.connection.cursor()        
        cur.execute('INSERT INTO pe_persons(pe_id, pe_fullname, pe_email, pe_phone) VALUES(%s, %s, %s, %s)', (pe_id, pe_fullname, pe_email, pe_phone,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_person(self, update = None, pe_id = None, pe_fullname = None, pe_email = None, pe_phone = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE pe_persons SET pe_fullname = %s, pe_email = %s, pe_phone = %s WHERE pe_id = %s', (pe_fullname, pe_email, pe_phone, pe_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class pv_providers_model():
    def __init__(self):
        pass
    
    def gen_provider_id(self):
        unique_number = None
        cur = mysql.connection.cursor()
        while not unique_number:
            randomNumber = str(random.randint(100000, 999999))
            query = "SELECT pv_id FROM pv_providers WHERE pv_id = %s"
            cur.execute(query, (randomNumber,))
            result = cur.fetchone()
            if not result:
                unique_number = randomNumber
        cur.close()
        return unique_number

    def get_provider(self, pv_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT pv_providers.* FROM pv_providers WHERE pv_providers.pv_id = %s', (pv_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_providers(self, get = None, pv_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pv_providers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM pv_providers INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id WHERE pv_providers.pv_id LIKE %s OR pv_providers.pv_regdate LIKE %s ORDER BY pv_providers.pv_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'status':
            cur.execute('SELECT pv_providers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM pv_providers INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id WHERE pv_providers.pv_status = %s', (pv_status,))
        else:
            cur.execute('SELECT pv_providers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM pv_providers INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_providers_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM pv_providers WHERE pv_providers.pv_id LIKE %s OR pv_providers.pv_regdate LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM pv_providers')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_provider(self, pv_id = None, fullname = None, email = None, phone = None):
        cur = mysql.connection.cursor()  
        pe_id = str(uuid.uuid4())
        pe_persons_model().insert_person(pe_id = pe_id, pe_fullname = fullname, pe_email = email, pe_phone = phone)
        cur.execute('INSERT INTO pv_providers(pv_id, pe_id) VALUES(%s, %s)', (pv_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_provider(self, update = None, pv_id = None, pe_fullname = None, pe_email = None, pe_phone = None, status = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            pe_id = self.get_provider(pv_id)['pe_id']
            pe_persons_model().update_person(update = 'all', pe_id = pe_id, pe_fullname = pe_fullname, pe_email = pe_email, pe_phone = pe_phone)
        elif update == 'status':        
            cur.execute('UPDATE pv_providers SET pv_status = %s WHERE pv_id = %s', (status, pv_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class pr_products_model():
    def __init__(self):
        pass
    
    def get_product(self, pr_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT pr_products.*, br_brands.br_name FROM pr_products INNER JOIN br_brands ON br_brands.br_id = pr_products.br_id WHERE pr_products.pr_id = %s', (pr_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_products(self, get = None, page_start = 1, quantity = 10, search = None, pr_status = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pr_products.*, br_brands.br_name, ca_categories.ca_name, pe_persons.pe_fullname FROM pr_products INNER JOIN br_brands ON br_brands.br_id = pr_products.br_id INNER JOIN ca_categories ON ca_categories.ca_id = pr_products.ca_id INNER JOIN pv_providers ON pv_providers.pv_id = pr_products.pv_id INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id WHERE pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s ORDER BY pr_products.pr_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        elif get == 'tablestatus':
            like = f'%{search}%'
            cur.execute('SELECT pr_products.*, br_brands.br_name, ca_categories.ca_name, pe_persons.pe_fullname FROM pr_products INNER JOIN br_brands ON br_brands.br_id = pr_products.br_id INNER JOIN ca_categories ON ca_categories.ca_id = pr_products.ca_id INNER JOIN pv_providers ON pv_providers.pv_id = pr_products.pv_id INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id WHERE pr_products.pr_status = %s AND (pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s) ORDER BY pr_products.pr_id ASC LIMIT %s, %s',(pr_status, like, like, page_start, quantity,))
        else:
            cur.execute('SELECT pr_products.* FROM pr_products')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_products_count(self, get = None, search = None, pr_status = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM pr_products WHERE pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s', (like, like,))
        elif get == 'tablestatus':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM pr_products WHERE pr_products.pr_status = %s AND (pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s)', (pr_status, like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM pr_products')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_product(self, pr_id = None, pr_barcode = None, pr_name = None, pr_model = None, pr_description = None, pr_cost = None, pr_price = None, ca_id = None, br_id = None, pv_id = None):
        cur = mysql.connection.cursor()       
        cur.execute('INSERT INTO pr_products(pr_id, pr_barcode, pr_name, pr_model, pr_description, pr_cost, pr_price, ca_id, br_id, pv_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (pr_id, pr_barcode, pr_name, pr_model, pr_description, pr_cost, pr_price, ca_id, br_id, pv_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_product(self, update = None, pr_id = None, pr_barcode = None, pr_name = None, pr_model = None, pr_description = None, pr_cost = None, pr_price = None, ca_id = None, br_id = None, pv_id = None, pr_status = None):
        cur = mysql.connection.cursor()  
        
        if update == 'all':        
           cur.execute('UPDATE pr_products SET pr_barcode = %s, pr_name = %s, pr_model = %s, pr_description = %s, pr_cost = %s, pr_price = %s, ca_id = %s, br_id = %s, pv_id = %s WHERE pr_id = %s', (pr_barcode, pr_name, pr_model, pr_description, pr_cost, pr_price, ca_id, br_id, pv_id, pr_id,))
        elif update == 'status':        
           cur.execute('UPDATE pr_products SET pr_status = %s  WHERE pr_id = %s', (pr_status, pr_id,))
        else:
            cur.close()
            return False
            
        mysql.connection.commit()
        cur.close()
        return True

class ci_cities_model():
    def __init__(self):
        pass

    def get_city(self, get = None, ci_id = None, ci_name = None, st_name = None):
        cur = mysql.connection.cursor()
        
        if get == 'name':
            cur.execute('SELECT ci_cities.* FROM ci_cities WHERE ci_cities.ci_name = %s', (ci_name,))
        elif get == 'nameandstate':
            cur.execute('SELECT ci_cities.*, st_states.st_name FROM ci_cities INNER JOIN st_states ON st_states.st_id = ci_cities.st_id WHERE ci_cities.ci_name = %s AND st_states.st_name = %s', (ci_name, st_name,))
        else:
            cur.execute('SELECT ci_cities.* FROM ci_cities WHERE ci_cities.ci_id = %s', (ci_id,))
            
        data = cur.fetchone()
        cur.close()
        return data

    def get_cities(self, get = None, ci_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'status':
            cur.execute('SELECT ci_cities.* FROM ci_cities WHERE ci_cities.ci_status = %s', (ci_status,))
        elif get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT ci_cities.*, st_states.st_name FROM ci_cities INNER JOIN st_states ON st_states.st_id = ci_cities.st_id WHERE ci_cities.ci_id LIKE %s OR ci_cities.ci_name LIKE %s ORDER BY ci_cities.ci_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT ci_cities.* FROM ci_cities')
            
        data = cur.fetchall()
        cur.close()
        return data

    def get_cities_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM ci_cities WHERE ci_cities.ci_id LIKE %s OR ci_cities.ci_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM ci_cities')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data
    
    def insert_city(self, ci_name = None, st_id = None):
        cur = mysql.connection.cursor()  
        cur.execute('INSERT INTO ci_cities(ci_name, st_id) VALUES(%s, %s)', (ci_name, st_id,))
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_city(self, update = None, ci_name = None, ci_status = None, ci_id = None, st_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE ci_cities SET ci_name = %s, st_id = %s WHERE ci_id = %s', (ci_name, st_id, ci_id,))
        elif update == 'status':        
            cur.execute('UPDATE ci_cities SET ci_status = %s WHERE ci_id = %s', (ci_status, ci_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class st_states_model():
    def __init__(self):
        pass
    
    def get_state(self, get = None, st_id = None, st_name = None):
        cur = mysql.connection.cursor()
        
        if get == 'name':
            cur.execute('SELECT st_states.* FROM st_states WHERE st_states.st_name = %s', (st_name,))
        else:
            cur.execute('SELECT st_states.* FROM st_states WHERE st_states.st_id = %s', (st_id,))
            
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_states(self, get = None, st_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'status':
            cur.execute('SELECT st_states.* FROM st_states WHERE st_states.st_status = %s', (st_status,))
        elif get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT st_states.* FROM st_states WHERE st_states.st_id LIKE %s OR st_states.st_name LIKE %s ORDER BY st_states.st_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT st_states.* FROM st_states')
            
        data = cur.fetchall()
        cur.close()
        return data

    def get_states_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM st_states WHERE st_states.st_id LIKE %s OR st_states.st_name LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM st_states')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_state(self, st_name = None):
        cur = mysql.connection.cursor()  
        cur.execute('INSERT INTO st_states(st_name) VALUES(%s)', (st_name,))
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_state(self, update = None, st_name = None, st_status = None, st_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE st_states SET st_name = %s WHERE st_id = %s', (st_name, st_id,))
        elif update == 'status':        
            cur.execute('UPDATE st_states SET st_status = %s WHERE st_id = %s', (st_status, st_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True
    
class ad_addresses_model():
    def __init__(self):
        pass
    
    def get_address(self, get = None, ad_id = None, pe_id = None):
        cur = mysql.connection.cursor()
        
        if get == 'idperson':
            cur.execute('SELECT ad_addresses.* FROM ad_addresses WHERE ad_addresses.ad_id = %s AND pe_id = %s', (ad_id, pe_id,))
        else:
            cur.execute('SELECT ad_addresses.* FROM ad_addresses WHERE ad_addresses.ad_id = %s AND pe_id = %s', (ad_id, pe_id,))
            
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_addresses(self, get = None, pe_id = None, ad_status = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'tableperson':
            like = f'%{search}%'
            cur.execute('SELECT ad_addresses.*, ci_cities.ci_name, st_states.st_name FROM ad_addresses INNER JOIN ci_cities ON ci_cities.ci_id = ad_addresses.ci_id INNER JOIN st_states ON st_states.st_id = ci_cities.st_id WHERE ad_addresses.pe_id = %s AND ad_addresses.ad_status = 1 AND (ad_addresses.ad_id LIKE %s OR ad_addresses.ad_address LIKE %s OR ad_addresses.ad_postalcode LIKE %s OR ci_cities.ci_name LIKE %s OR st_states.st_name LIKE %s) ORDER BY ad_addresses.ad_regdate DESC LIMIT %s, %s',(pe_id, like, like, like, like, like, page_start, quantity,))
        elif get == 'person':
            cur.execute('SELECT ad_addresses.* FROM ad_addresses WHERE ad_addresses.pe_id = %s',(pe_id,))
        elif get == 'personstatus':
            cur.execute('SELECT ad_addresses.* FROM ad_addresses WHERE ad_addresses.pe_id = %s AND ad_status = %s',(pe_id, ad_status,))
        else:
            cur.execute('SELECT ad_addresses.* FROM ad_addresses')
        
        data = cur.fetchall()
        cur.close()        
        return data
    
    def get_addresses_count(self, get = None, pe_id = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'tableperson':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM ad_addresses INNER JOIN ci_cities ON ci_cities.ci_id = ad_addresses.ci_id INNER JOIN st_states ON st_states.st_id = ci_cities.st_id WHERE ad_addresses.pe_id = %s AND ad_addresses.ad_status = 1 AND (ad_addresses.ad_id LIKE %s OR ad_addresses.ad_address LIKE %s OR ad_addresses.ad_postalcode LIKE %s OR ci_cities.ci_name LIKE %s OR st_states.st_name LIKE %s) ORDER BY ad_addresses.ad_id ASC',(pe_id, like, like, like, like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM ad_addresses')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_address(self, ad_type = None, ad_address = None, ad_postalcode = None, ad_reference = None, ad_contact = None, ci_id = None, pe_id = None):
        cur = mysql.connection.cursor()  
        ad_id = str(uuid.uuid4())
        cur.execute('INSERT INTO ad_addresses(ad_id, ad_type, ad_address, ad_postalcode, ad_reference, ad_contact, ci_id, pe_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', (ad_id, ad_type, ad_address, ad_postalcode, ad_reference, ad_contact, ci_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_address(self, update = None, ad_type = None, ad_address = None, ad_postalcode = None, ad_reference = None, ad_contact = None, ci_id = None, ad_status=None, ad_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'all':        
            cur.execute('UPDATE ad_addresses SET ad_type = %s, ad_address = %s, ad_postalcode = %s, ad_reference = %s, ad_contact = %s, ad_regdate = NOW(), ci_id = %s WHERE ad_id = %s', (ad_type, ad_address, ad_postalcode, ad_reference, ad_contact, ci_id, ad_id,))
        elif update == 'status':        
            cur.execute('UPDATE ad_addresses SET ad_status = %s WHERE ad_id = %s', (ad_status, ad_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True
    
class ts_typessales_model():
    def __init__(self):
        pass
    
    def get_typesale(self, ts_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT ts_typessales.* FROM ts_typessales WHERE ts_typessales.ts_id = %s', (ts_id,))         
        data = cur.fetchone()
        cur.close()
        return data

    def get_typessales(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT ts_typessales.* FROM ts_typessales')         
        data = cur.fetchall()
        cur.close()
        return data

class sa_sales_model():
    def __init__(self):
        pass
    
    def get_sale(self, get = None, sa_id = None, sa_status = None):
        cur = mysql.connection.cursor()

        if get == 'sa_id':
            cur.execute('SELECT sa_sales.*, lo_locations.lo_name, ts_typessales.ts_name, cu_pe_persons.pe_fullname AS cu_pe_fullname, us_pe_persons.pe_fullname AS us_pe_fullname FROM sa_sales INNER JOIN lo_locations ON lo_locations.lo_id = sa_sales.lo_id INNER JOIN ts_typessales ON ts_typessales.ts_id = sa_sales.ts_id LEFT JOIN cu_customers ON cu_customers.cu_id = sa_sales.cu_id LEFT JOIN pe_persons AS cu_pe_persons ON cu_pe_persons.pe_id = cu_customers.pe_id INNER JOIN us_users ON us_users.us_id = sa_sales.us_id INNER JOIN pe_persons AS us_pe_persons ON us_pe_persons.pe_id = us_users.pe_id WHERE sa_sales.sa_id = %s', (sa_id,))  
        elif get == 'sa_id>sa_status':
            cur.execute('SELECT sa_sales.*, lo_locations.lo_name, ts_typessales.ts_name, cu_pe_persons.pe_fullname AS cu_pe_fullname, us_pe_persons.pe_fullname AS us_pe_fullname FROM sa_sales INNER JOIN lo_locations ON lo_locations.lo_id = sa_sales.lo_id INNER JOIN ts_typessales ON ts_typessales.ts_id = sa_sales.ts_id LEFT JOIN cu_customers ON cu_customers.cu_id = sa_sales.cu_id LEFT JOIN pe_persons AS cu_pe_persons ON cu_pe_persons.pe_id = cu_customers.pe_id INNER JOIN us_users ON us_users.us_id = sa_sales.us_id INNER JOIN pe_persons AS us_pe_persons ON us_pe_persons.pe_id = us_users.pe_id WHERE sa_sales.sa_id = %s AND sa_sales.sa_status = %s', (sa_id, sa_status,))  
        else:
            cur.close()
            return None

        data = cur.fetchone()
        cur.close()        
        return data
        
    def get_sales(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT sa_sales.*, lo_locations.lo_name, ts_typessales.ts_name, cu_pe_persons.pe_fullname AS cu_pe_fullname, us_pe_persons.pe_fullname AS us_pe_fullname FROM sa_sales INNER JOIN lo_locations ON lo_locations.lo_id = sa_sales.lo_id INNER JOIN ts_typessales ON ts_typessales.ts_id = sa_sales.ts_id LEFT JOIN cu_customers ON cu_customers.cu_id = sa_sales.cu_id LEFT JOIN pe_persons AS cu_pe_persons ON cu_pe_persons.pe_id = cu_customers.pe_id INNER JOIN us_users ON us_users.us_id = sa_sales.us_id INNER JOIN pe_persons AS us_pe_persons ON us_pe_persons.pe_id = us_users.pe_id ORDER BY sa_sales.sa_regdate ASC LIMIT %s, %s',(page_start, quantity,))
        else:
            cur.execute('SELECT sa_sales.* FROM sa_sales')
        
        data = cur.fetchall()
        cur.close()        
        return data
    
    def get_sales_count(self, get = None, pe_id = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM sa_sales')
        else:
            cur.execute('SELECT COUNT(*) AS total FROM sa_sales')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data
    
    def insert_sale(self, sa_id = None, sa_subtotal = None, sa_discount = None, sa_amountpayments = None, sa_days = None, lo_id = None, ts_id = None, cu_id = None, us_id = None):
        cur = mysql.connection.cursor()          
        cur.execute('INSERT INTO sa_sales(sa_id, sa_subtotal, sa_discount, sa_amountpayments, sa_days, lo_id, ts_id, cu_id, us_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (sa_id, sa_subtotal, sa_discount, sa_amountpayments, sa_days, lo_id, ts_id, cu_id, us_id,))
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_sale(self, update = None, sa_status = None, sa_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'sa_status':        
            cur.execute('UPDATE sa_sales SET sa_status = %s WHERE sa_id = %s', (sa_status, sa_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True

class sd_saledetails_model():
    def __init__(self):
        pass
    
    def get_saledetails(self, get = None, sa_id = None):
        cur = mysql.connection.cursor()

        if get == 'sa_id':
            cur.execute('SELECT sd_saledetails.*, pr_products.pr_name FROM sd_saledetails INNER JOIN pr_products ON pr_products.pr_id = sd_saledetails.pr_id WHERE sd_saledetails.sa_id = %s ORDER BY sd_saledetails.sd_id ASC', (sa_id,))  
        else:
            cur.close()
            return []
    
        data = cur.fetchall()
        cur.close()
        return data
    
    def insert_saledetail(self, sd_price = None, sd_quantity = None, pr_id = None, sa_id = None):
        cur = mysql.connection.cursor()          
        cur.execute('INSERT INTO sd_saledetails(sd_price, sd_quantity, pr_id, sa_id) VALUES(%s, %s, %s, %s)', (sd_price, sd_quantity, pr_id, sa_id,))
        mysql.connection.commit()
        cur.close()
        return True

class sp_salepayments_model():
    def __init__(self):
        pass
    
    def get_salepayment(self, get = None, sp_id = None):
        cur = mysql.connection.cursor()

        if get == 'sp_id':
            cur.execute('SELECT sp_salepayments.* FROM sp_salepayments WHERE sp_salepayments.sp_id = %s', (sp_id,))  
        elif get == 'max_sp_no':
            cur.execute('SELECT COALESCE(MAX(sp_no), 1000000) AS max_sp_no FROM sp_salepayments')  
        else:
            cur.close()
            return None
    
        data = cur.fetchone()
        cur.close()
        return data

    def get_salepayments(self, get = None, sa_id = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()

        if get == 'sa_id':
            cur.execute('SELECT sp_salepayments.* FROM sp_salepayments WHERE sp_salepayments.sa_id = %s ORDER BY sp_salepayments.sp_id ASC', (sa_id,))  
        elif get == 'limitdate':
            cur.execute('SELECT sp.sa_id, MIN(sp.sp_limitdate) AS min_limitdate FROM sp_salepayments sp INNER JOIN sa_sales AS sa ON sa.sa_id = sp.sa_id WHERE sp.sp_pay < sp.sp_subtotal AND sp.sp_limitdate < NOW() AND sa.sa_status = 1 GROUP BY sp.sa_id ORDER BY min_limitdate ASC')  
        elif get == 'table-sa_id':
            like = f'%{search}%'
            cur.execute('SELECT sp_salepayments.*, pm_paymentmethods.pm_name, pe_persons.pe_fullname FROM sp_salepayments LEFT JOIN pm_paymentmethods ON pm_paymentmethods.pm_id = sp_salepayments.pm_id LEFT JOIN us_users ON us_users.us_id = sp_salepayments.us_id LEFT JOIN pe_persons ON pe_persons.pe_id = us_users.pe_id WHERE sp_salepayments.sa_id = %s ORDER BY sp_salepayments.sp_id ASC LIMIT %s, %s',(sa_id, page_start, quantity,))
        else:
            cur.close()
            return []
    
        data = cur.fetchall()
        cur.close()
        return data
    
    def get_salepayments_count(self, get = None, sa_id = None, search = None):
        cur = mysql.connection.cursor()

        if get == 'table-sa_id':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM sp_salepayments WHERE sp_salepayments.sa_id = %s',(sa_id,))  
        else:
            cur.close()
            return 0
    
        data = cur.fetchone()['total']
        cur.close()
        return data

    def insert_salepayment(self, sp_no = None, sp_subtotal = None, sp_commission = None, sp_pay = None, sp_limitdate = None, sp_regdate = None, pm_id = None, us_id = None, sa_id = None):
        cur = mysql.connection.cursor()          
        cur.execute('INSERT INTO sp_salepayments(sp_no, sp_subtotal, sp_commission, sp_pay, sp_limitdate, sp_regdate, pm_id, us_id, sa_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (sp_no, sp_subtotal, sp_commission, sp_pay, sp_limitdate, sp_regdate, pm_id, us_id, sa_id,))
        mysql.connection.commit()
        cur.close()
        return True
    
    def update_salepayment(self, update = None, sp_no = None, sp_commission = None, sp_pay = None, pm_id = None, us_id = None, sp_id = None, sp_limitdate = None):
        cur = mysql.connection.cursor()  
        
        if update == 'pay':
            cur.execute('UPDATE sp_salepayments SET sp_no = %s, sp_commission = %s, sp_pay = %s, sp_regdate = NOW(), pm_id = %s, us_id = %s WHERE sp_id = %s', (sp_no, sp_commission, sp_pay, pm_id, us_id, sp_id,))
        elif update == 'edit':
            cur.execute('UPDATE sp_salepayments SET sp_pay = %s, sp_limitdate = %s, us_id = %s WHERE sp_id = %s', (sp_pay, sp_limitdate, us_id, sp_id,))
        else:
            cur.close()
            return False

        mysql.connection.commit()
        cur.close()
        return True
    