########## validating admin and user
import MySQLdb
import time
import os
from connection import *

def validate(role,user_email,user_password):
    #mysql connection
    conn=connect_db()
    cursor=conn.cursor()
    result=False
    try:
        cursor.execute("select user_email,user_password,status_role from users where user_email='{}'and user_password='{}' and status_role='{}'".format(user_email,user_password,role))
        rows=cursor.fetchall()
        try:
            email,password,id1=rows[0][0],rows[0][1],rows[0][2]
            if(id1==role and email==user_email and password==user_password):
                result=True
        except:
            pass
    except:
        print(" > Unable to Validate user details")
        
    cursor.close()
    conn.close()
    return result

def login(role):
    os.system('cls')
    user_name=str(input('  >User_name(email):'))
    password=str(input('  >Password:'))
    Is_valid=validate(role,user_name,password)
    if( not Is_valid):
        print()
        print("  >Email/Password is Incorrect")
        print()
        time.sleep(2)
        os.system('cls')
    else:
        time.sleep(1)
        os.system('cls')
        print()
    return Is_valid,user_name
    
    
