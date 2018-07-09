import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(name, phone, email):
    return f"""
    INSERT INTO users (name,phone, email) 
    VALUES('{name}', '{phone}', '{email}')
    """

@commit_close    
def db_update(phone, id):
    return f"""
    UPDATE users SET phone = '{phone}' WHERE id = {id}
    """

@commit_close
def db_delete(id):
    return f"""
    DELETE FROM users WHERE id = {id}
    """   

def db_select(data, field):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = f"""
    SELECT id, name, phone, email
    FROM users 
    WHERE {field} =  {data}
    """
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data