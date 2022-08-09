####### MAIN ##########

##importing
import MySQLdb
from initial_setup import *
from validation import *
from admin import *
from member import *
from connection import *
import time
import os



##def take_input():
##    os.system('cls')
##    user_name=str(input(' >User_name(email):'))
##    password=str(input(' >Password:'))
##    time.sleep(1)
##    os.system('cls')
##    print()
##    print(" @@@@@@@@@@@@@@@@@@@@@@ {} @@@@@@@@@@@@@@@@@@@@@@ ".format(shop_name[0].upper()))
##    return user_name,password
##


#PART1: SETTING UP THE MACHINE
#mysql connection
conn=connect_db()
cursor=conn.cursor()
cursor.execute("select * from shopdetails")
rows=cursor.rowcount
if(rows==0):     #for first time,to setup the shop information and admin account
    cursor.execute("select column_name from information_schema.columns where table_name=N'shopdetails' ORDER BY ORDINAL_POSITION ")
    shop_columns=cursor.fetchall()
    shop_details,admin_details=setup(shop_columns)
    shop_details=tuple(shop_details)
    admin_details=tuple(admin_details)
    try:
        query="insert into shopdetails values('%s','%s','%s','%s','%s','%s','%s')"
        cursor.execute(query % shop_details)
        conn.commit()
        print('   > Shop details Setted.')
        query="insert into users(user_name,user_mobile,user_email,user_password,status_role) values('%s','%s','%s','%s','1')"
        cursor.execute(query % admin_details)
        time.sleep(1)
        print('   > Admin setted.')
        conn.commit()
        # clear screen for windows
        os.system("cls")
    except:
        print('   > Unable to SETUP!.')
        conn.rollback()
cursor.execute("select shop_name from shopdetails")
shop_name=cursor.fetchone()
print('')
print(" @@@@@@@@@@@@@@@@@@@@@@ {} @@@@@@@@@@@@@@@@@@@@@@ ".format(shop_name[0].upper()))
loop=1
while(loop==1):
    print('')
    print(" -_-_-_-_-_-_ LOGIN -_-_-_-_-_-_\n")
    print("    1. Admin")
    print("    2. Member")
    print("    0. Exit")
    print("    ---------")
    choice_main=int(input("    Input:"))
    print()
    if(choice_main==1):
        status,email=login(1)
        print(" @@@@@@@@@@@@@@@@@@@@@@ {} @@@@@@@@@@@@@@@@@@@@@@ ".format(shop_name[0].upper()))
        if(status):
            Isloggedin=True
            admin_main(Isloggedin,email)
    elif(choice_main==2):
        status,email=login(2)
        print(" @@@@@@@@@@@@@@@@@@@@@@ {} @@@@@@@@@@@@@@@@@@@@@@ ".format(shop_name[0].upper()))
        if(status):
            Isloggedin=True
            member_main(Isloggedin,email)
    elif(choice_main==0):
        #os.system('cls')
        print(" @@@@@@@@@@@@@@@@@@@  THANK YOU @@@@@@@@@@@@@@@@@@@")
        loop=0
        time.sleep(1)
    else:
        print(" > Wrong input")
        time.sleep(1)
cursor.close()
conn.close()





