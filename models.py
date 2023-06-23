from config import *

class us_users_model():
    def __init__(self):
        pass
    
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
        cur.execute('INSERT INTO pe_persons(pe_fullname, pe_email, pe_phone) VALUES(%s, %s, %s)', (fullname, email, phone,))
        pe_id = cur.lastrowid
        cur.execute('INSERT INTO us_users(us_id, us_password, mem_id, pe_id) VALUES(%s, %s, %s, %s)', (us_id, password, mem_id, pe_id,))
        mysql.connection.commit()
        cur.close()
        return True

    def update_user(self, update = None, us_id = None, fullname = None, email = None, password = None, phone = None, permissions = None, mem_id = None):
        cur = mysql.connection.cursor()
        
        if update == 'password':        
            cur.execute('UPDATE us_users SET us_password = %s WHERE us_id = %s', (password, us_id,))
        elif update == 'all':  
            pe_id = self.get_user(us_id=us_id)['pe_id']
            pe_persons_model().update_person(update = 'all', pe_id = pe_id, pe_fullname = fullname, pe_email = email, pe_phone = phone)  
            cur.execute('UPDATE us_users SET us_password = %s, us_permissions = %s, mem_id = %s WHERE us_id = %s', (password, permissions, mem_id, us_id,))
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
    
    def get_paymentmethods(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pm_paymentmethods.* FROM pm_paymentmethods WHERE pm_paymentmethods.pm_id LIKE %s OR pm_paymentmethods.pm_name LIKE %s ORDER BY pm_paymentmethods.pm_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
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
    
    def get_locations(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT lo_locations.* FROM lo_locations WHERE lo_locations.lo_id LIKE %s OR lo_locations.lo_name LIKE %s ORDER BY lo_locations.lo_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
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
        cur.execute('SELECT cu_customers.* FROM cu_customers WHERE cu_customers.cu_id = %s', (cu_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_customers(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT cu_customers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id WHERE cu_customers.cu_id LIKE %s OR cu_customers.cu_regdate LIKE %s ORDER BY cu_customers.cu_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT cu_customers.*, pe_persons.pe_email, pe_persons.pe_fullname, pe_persons.pe_phone FROM cu_customers INNER JOIN pe_persons ON pe_persons.pe_id = cu_customers.pe_id')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_customers_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM cu_customers WHERE cu_customers.cu_id LIKE %s OR cu_customers.cu_regdate LIKE %s', (like, like,))
        else:
            cur.execute('SELECT COUNT(*) AS total FROM cu_customers')
        
        data = cur.fetchone()['total']
        cur.close()        
        return data

    def insert_customer(self, cu_id = None, fullname = None, email = None, phone = None):
        cur = mysql.connection.cursor()  
        cur.execute('INSERT INTO pe_persons(pe_fullname, pe_email, pe_phone) VALUES(%s, %s, %s)', (fullname, email, phone,))
        pe_id = cur.lastrowid     
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
        cur.execute('INSERT INTO pe_persons(pe_fullname, pe_email, pe_phone) VALUES(%s, %s, %s)', (fullname, email, phone,))
        pe_id = cur.lastrowid     
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
        cur.execute('SELECT pr_products.* FROM pr_products WHERE pr_products.pr_id = %s', (pr_id,))
        data = cur.fetchone()
        cur.close()
        return data
    
    def get_products(self, get = None, page_start = 1, quantity = 10, search = None):
        cur = mysql.connection.cursor()
        
        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT pr_products.*, br_brands.br_name, ca_categories.ca_name, pe_persons.pe_fullname FROM pr_products INNER JOIN br_brands ON br_brands.br_id = pr_products.br_id INNER JOIN ca_categories ON ca_categories.ca_id = pr_products.ca_id INNER JOIN pv_providers ON pv_providers.pv_id = pr_products.pv_id INNER JOIN pe_persons ON pe_persons.pe_id = pv_providers.pe_id WHERE pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s ORDER BY pr_products.pr_id ASC LIMIT %s, %s',(like, like, page_start, quantity,))
        else:
            cur.execute('SELECT pr_products.* FROM pr_products')
        
        data = cur.fetchall()
        cur.close()        
        return data

    def get_products_count(self, get = None, search = None):       
        cur = mysql.connection.cursor()

        if get == 'table':
            like = f'%{search}%'
            cur.execute('SELECT COUNT(*) AS total FROM pr_products WHERE pr_products.pr_id LIKE %s OR pr_products.pr_name LIKE %s', (like, like,))
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

