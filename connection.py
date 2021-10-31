import MySQLdb

def connect_db():
     conn=MySQLdb.connect(host='localhost',database='billmanager',user='root',password='zxcvbnm')
     return conn

def get_info_by_email(email):
    conn=connect_db()
    cursor=conn.cursor()
    try:
        cursor.execute("select * from users where user_email='{}'".format(email))
        rows=cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except:
        print(" > Server Error!")
        cursor.close()
        conn.close()
        return None
