################ Member
import MySQLdb
import time
from funct import account,bill,show_all_products,logouttGreeting,get_bill_details
from connection import *

def member_main(Isloggedin,email):
        #main
        if(not Isloggedin):
                return None

        #mysql connection
        conn=connect_db()
        cursor=conn.cursor()
        try:
                cursor.execute("select * from users where status_role='2' and user_email='{}'".format(email))
                rows=cursor.fetchall()
        except:
                print()
                print(" > Server Error!")
                return None
        print()    
        print("   ================ WELCOME {} ================ ".format(rows[0][1].upper()))
        print()
        print("   Role:Member \t\t\t\t   0:logout\n")
        while(Isloggedin):
                print("   ------- MAIN MENU -------")
                print("      1. Account Management")
                print("      2. Product Details")
                print("      3. Generate Bill")
                print("      4. Get bill information")
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
                        show_all_products(cursor)
                        print()
                elif(choice==3):
                        bill(cursor,email)
                        print()
                elif(choice==4):
                        get_bill_details(cursor)
                        print()
                else:
                        print()
                        print("      > Wrong choice")
                        time.sleep(1)
                        print()
        cursor.close()
        conn.close()




