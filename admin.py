############# admin
import MySQLdb
import time
from connection import *
from funct import *

def admin_main(Isloggedin,email):
    ##admin main 
    if(not Isloggedin):
        return None

    #mysql connection
    conn=connect_db()
    cursor=conn.cursor()
    try:
        cursor.execute("select * from users where status_role='1' and user_email='{}'".format(email))
        rows=cursor.fetchall()
    except:
        print(" > Server Error!")
        return None
    print()    
    print("   ================ WELCOME {} ================ ".format(rows[0][1].upper()))
    print()
    print("   Role:Admin \t\t\t\t   0:logout\n")
    while(Isloggedin):
        print("   ------- MAIN MENU -------")
        print("      1. Account Management")
        print("      2. Product Management")
        print("      3. Members Management")
        #print("      4. Reports")
        print("      5. Generate Bill")
        print("      6. Get bill information")
        print("      0. Logout")
        print("      ---------------------")
        choice=int(input("      Input:"))
        ##
        if(choice==0):
            Isloggedin=False
            logouttGreeting()
        elif(choice==1):
            account(email)
            print()
        elif(choice==2):
            product()
            print()
        elif(choice==3):
            members()
            print()
        elif(choice==4):
            report()
            print()
        elif(choice==5):
            bill(cursor,email)
            print()
        elif(choice==6):
            get_bill_details(cursor)
            print()
        else:
            print()
            print("      > Wrong choice")
            time.sleep(1)
            print()
    cursor.close()
    conn.close()

