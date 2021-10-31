########### funct
import time
import os
from connection import *
from datetime import datetime

def account(email):   #account management
    nemail=None
    while(True):
        print()
        print("         ....... ACCOUNT MANAGEMENT .......")
        print("            1. Show Account details")
        print("            2. Edit Account details")
        print("            9. Main Menu") 
        print("            .........................")
        choice_sub=int(input("            Input:"))
        if(choice_sub==9 or choice_sub==0):
            print()
            break
        elif(choice_sub==1):
            rows=get_info_by_email(email)
            print()
            print("               ******* ACCOUNT DETAILS *******")
            print()
            print("                  User_Name:{}".format(rows[0][1]))
            print("                  Mobile:{}".format(rows[0][2]))
            print("                  Email:{}".format(rows[0][3]))
            nemail=rows[0][3]
            if(rows[0][5]==1):
                print("                  Role:Admin")
            elif(rows[0][5]==0):
               print("                  Role:Member")
            print("\n               ****************************")
            print()
            time.sleep(2)
        elif(choice_sub==2):
            fields=[]
            print()
            print("                  ******* EDIT ACCOUNT DETAILS *******")
            print()
            fields.append(str(input("                  User_Name:")))
            fields.append(str(input("                  Mobile:")))
            fields.append(str(input("                  Email:")))
            fields.append(str(input("                  Password:")))
            conn=connect_db()
            cursor=conn.cursor()
            confirm=str(input("\n                  > Are you sure??(y/n):"))
            if(confirm=='y' or confirm=='Y'):
                try:
                    cursor.execute("UPDATE `billmanager`.`users` SET `user_name` = '{}',`user_mobile` = '{}',`user_email` = '{}',`user_password` = '{}' WHERE (`user_email` = '{}')".format(fields[0],fields[1],fields[2],fields[3],nemail))
                    conn.commit()
                    time.sleep(1)
                    print()
                    print("                  > Account details updated sucessfuly")
                    time.sleep(1)
                    print()
                    print("                  > Kindly Logout and Login again")
                    email=fields[2]
                except:
                    print()
                    print("                  > Unable to update account details!")
                    conn.rollback()
            time.sleep(1)    
            print("\n               *********************************** ")
            print()
            cursor.close()
            time.sleep(1)
        else:
            print("\n             > Wrong input")
            time.sleep(1)
        
    

def product():   #product management
    print()
    conn=connect_db()
    cursor=conn.cursor()
    while(True):
        print()
        print("         ....... PRODUCT MANAGEMENT .......")
        print("            1. Add Product details")
        print("            2. Edit Product details")
        print("            3. Remove Product details")
        print("            4. Show Product details")
        print("            9. Main Menu")     
        print("            ................................")
        choice_sub=int(input("            Input:"))
        print()
        if(choice_sub==9 or choice_sub==0):
            print()
            break
         ##adding products
        elif(choice_sub==1):        ##adding products
            print("               ******* ADD PRODUCT DETAILS *******")
            fields=collect_product_details()
            confirm=str(input("\n                  > Are you sure??(y/n):"))
            if(confirm=='y' or confirm=='Y'):
                try:
                    cursor.execute("SELECT pro_id FROM billmanager.products")
                    rows=cursor.fetchall()
                    for row in rows:
                        if(row[0]==fields[0]):
                            print("\n                  > Product id already exists!")
                            time.sleep(2)
                            break
                    else:
                        cursor.execute("INSERT INTO `billmanager`.`products` (`pro_id`, `pro_title`, `pro_category`, `pro_price`, `pro_gst`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(fields[0],fields[1],fields[2],fields[3],fields[4]))
                        conn.commit()
                        time.sleep(1)
                        print()
                        print("                  > Product details added sucessfuly")
                        time.sleep(1)
                except:
                    print()
                    print("                 > Unable to add product details!")
                    conn.rollback()
            time.sleep(1)
            print("\n             *********************************** ")
            print()

        ## updating the product details
        elif(choice_sub==2):
            print("\n               ******* UPDATE PRODUCT DETAILS *******")
            print()
            Id=str(input("                  > Product ID?:"))
            Is_exist=validate_product(cursor,Id)
            if(not Is_exist):
                print("\n                  > Product ID doesn't exist\n")
            else:
                print("\n                  > Enter new details\n")
                fields=collect_product_details()
                confirm=str(input("\n                  > Are you sure??(y/n):"))
                if(confirm=='y' or confirm=='Y'):
                    try:
                        cursor.execute("UPDATE `billmanager`.`products` SET `pro_id` = '{}', `pro_title` = '{}', `pro_category` = '{}', `pro_price` = '{}', `pro_gst` = '{}' WHERE (`pro_id` = '{}')".format(fields[0],fields[1],fields[2],fields[3],fields[4],Id))
                        conn.commit()
                        time.sleep(1)
                        print()
                        print("                  > Product details updated sucessfuly")
                        time.sleep(1)
                    except:
                        print()
                        print("                  > Unable to update product details!")
                        conn.rollback()
            time.sleep(1)
            print("\n                *********************************** \n")

        ## remove the product details
        elif(choice_sub==3):
            print("\n               ******* REMOVE PRODUCT DETAILS *******")
            print()
            Id=str(input("                  > Product ID?:"))
            Is_exist=validate_product(cursor,Id)
            if(not Is_exist):
                print("\n                  > Product ID doesn't exist\n")
            else:
                confirm=str(input("\n                  > Are you sure??(y/n):"))
                if(confirm=='y' or confirm=='Y'):
                    try:
                        cursor.execute("DELETE FROM `billmanager`.`products` WHERE (`pro_id` = '{}')".format(Id))
                        conn.commit()
                        time.sleep(1)
                        print()
                        print("                  > Product details removed sucessfuly")
                        time.sleep(1)
                    except:
                        print()
                        print("                 > Unable to remove product details!")
                        conn.rollback()
            time.sleep(1)
            print("\n               ***********************************\n ")

            
        #show all the product details
        elif(choice_sub==4):
            show_all_products(cursor)
        else:
            print("               > Wrong input")
            time.sleep(1)
    cursor.close()
    conn.close()

def members():   #members management
    conn=connect_db()
    cursor=conn.cursor()
    print()
    while(True):
        print()
        print("         ....... MEMBERS MANAGEMENT.......")
        print("            1. Add New Member")
        print("            2. Show all user details")
        print("            3. Remove Member details")
        print("            4. Give admin control to member")
        print("            9. Main Menu")
        print("            ..............................")
        choice_sub=int(input("            Input:"))
        if(choice_sub==9 or choice_sub==0):
                print()
                break
        elif(choice_sub==1):
            count=0
            fields=[]
            print()
            print("               ******* ADD NEW MEMBER *******")
            print()
            fields.append(str(input("                  User_Name:")))
            fields.append(int(input("                  Mobile:")))
            fields.append(str(input("                  Email:")))
            #check email whether email id already exists or not
            try:
                cursor.execute("SELECT * FROM billmanager.users where user_email='{}' ".format(fields[2]))
                count=cursor.rowcount
            except:
                print()
            if(count==0):
                fields.append(str(input("                  Password:")))
                fields.append(int(input("""                  control(1:admin/2:member)):""")))
                if(fields[4]==1 or fields[4]==2):
                    confirm=str(input("\n                  > Are you sure??(y/n):"))
                    if(confirm=='y' or confirm=='Y'):
                        try:
                            cursor.execute("INSERT INTO `billmanager`.`users` (`user_name`, `user_mobile`, `user_email`, `user_password`, `status_role`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(fields[0],fields[1],fields[2],fields[3],fields[4]))
                            conn.commit()
                            time.sleep(1)
                            print()
                            print("                  > Account details added sucessfuly")
                            time.sleep(1)
                            print()
                        except:
                            print()
                            print("                  > Unable to add account details!")
                            conn.rollback()
                    time.sleep(1)    
                    print("\n               *********************************** \n")
                    time.sleep(1)            
                else:
                  print()
                  print("                  > Control should be '1' or '2'") 
                  time.sleep(1) 
            else:
                print()
                print("                  > Email already exists!! try another") 
                time.sleep(1)
        elif(choice_sub==2):
                    print()
                    print(" %5s ------------------------------------------------------------------------------------"%(""))
                    print(" %5s |%-20s|%-15s|%-24s|%-20s|"%("","   USER NAME"," MOBILE NUMBER","  EMAIL","  ROLE"))
                    print(" %5s ------------------------------------------------------------------------------------"%(""))
                    try:
                        cursor.execute("SELECT user_name,user_mobile,user_email,status_role FROM billmanager.users order by status_role ASC")
                        total=cursor.rowcount
                        rows=cursor.fetchall()
                        for row in rows:
                            if(row[3]==1):
                                role="Admin"
                            elif(row[3]==2):
                                role="Member"
                            print(" %5s |%-20s|%-15s|%-24s|%-20s|"%("",row[0],row[1],row[2],role))
                        print(" %5s ------------------------------------------------------------------------------------"%(""))
                    except:
                        print("                  > Problem while fetching the details!")
                    time.sleep(5)
        elif(choice_sub==3):
            print()
            print("               ******* REMOVE MEMBER DETAILS *******")
            print()
            Id=str(input("                  > Member Email?:"))
            try:
                cursor.execute("SELECT user_email FROM billmanager.users where user_email='{}' and status_role='{}'".format(Id,"2"))
                rows=cursor.rowcount
                if(rows!=0):
                    confirm=str(input("\n                  > Are you sure??(y/n):"))
                    if(confirm=='y' or confirm=='Y'):
                        try:
                            cursor.execute("DELETE FROM `billmanager`.`users` WHERE (`user_email` = '{}')".format(Id))
                            conn.commit()
                            print()
                            print("                  > Member details removed sucessfuly")
                            time.sleep(1)
                        except:
                            print()
                            print("                  > Unable to remove member details!")
                            conn.rollback()
                            time.sleep(1)
                            print("\n               *********************************** \n")
                else:
                    print()
                    print("                  > Member Email doesn't exist\n")
            except:
                print()
                print("                  > Problem while validaing Member id! \n")
        elif(choice_sub==4):
            print()
            print("               ******* ADMIN CONTROL TO MEMBER *******")
            print()
            Id=str(input("                  > Member Email?:"))
            try:
                cursor.execute("SELECT user_email FROM billmanager.users where user_email='{}' and status_role='{}'".format(Id,"2"))
                rows=cursor.rowcount
                if(rows!=0):
                    confirm=str(input("\n                  > Are you sure??(y/n):"))
                    if(confirm=='y' or confirm=='Y'):
                        try:
                            cursor.execute("UPDATE `billmanager`.`users` SET `status_role` = '1' WHERE (`user_email` = '{}')".format(Id))
                            conn.commit()
                            print()
                            print("                  > Member details updated sucessfuly")
                            time.sleep(1)
                        except:
                            print()
                            print("                  > Unable to update member details!")
                            conn.rollback()
                            time.sleep(1)
                            print("\n               ***********************************\n")
                else:
                    print()
                    print("                  > Member Email doesn't exist\n")
            except:
                print()
                print("                  > Problem while validaing Member email ! \n")
        else:
            print("               > Wrong input")
            time.sleep(1)

def report():   #report details
    pass
##    
##    print()
##    while(True):
##        print()
##        print("      ------- REPORTS -------")
##        print("         1. Date-Date Report")
##        print("         2. Hr-Hr Report")
##        print("         9. Main Menu")
##        print("         ---------------------")
##        choice_sub=int(input("         Input:"))
##        if(choice_sub==9 or choice_sub==0):
##            break
##        elif(choice_sub==1):
##            validity=False
##
##            #from date
##            print("            >> +++++++ FROM +++++++")
##            syr=int(input("            > Year:"))
##            smn=int(input("            > Month(1-12):"))
##            if(smn>=0 and smn<=12):
##               sdy=int(input("            > Day:"))
##               if(sdy>= and sdy<=31):
##                   validity=True
##               else:
##                    print("            > Day is not valid")
##            else:
##                print("            > Month is not valid")
##             
##            #to date
##            if(validity):
##                print("\n            >> +++++++ TO +++++++ ")
##                tyr=int(input("            > Year:"))
##                tmn=int(input("            > Month(1-12):"))
##                if(tmn>=1 and tmn<=12):
##                   tdy=int(input("            > Day:"))
##                   if(tdy>=1 and tdy<=31):
##                       pass #code
##                   else:
##                        validity=False
##                        print("            > Day is not valid")
##                else:
##                    validity=False
##                    print("            > Month is not valid")
##                    
##        elif(choice_sub==2):
##            
##            validity=False
##            #from date
##            print("            >> +++++++ FROM +++++++")
##            shr=int(input("            > Hour:"))
##            smin=int(input("            > Minute:"))
##            if(smin>=1 and smin<60):
##               sdy=int(input("            > Day:"))
##               if(sdy>=1 and sdy<=31):
##                   validity=True
##               else:
##                    print("            > Day is not valid")
##            else:
##                print("            > Month is not valid")
##             
##            #to date
##            if(validity):
##                print("\n            >> +++++++ TO +++++++ ")
##                tyr=int(input("            > Year:"))
##                tmn=int(input("            > Month(1-12):"))
##                if(tmn>=1 and tmn<=12):
##                   tdy=int(input("            > Day:"))
##                   if(tdy>=1 and tdy<=31):
##                       pass #code
##                   else:
##                        validity=False
##                        print("            > Day is not valid")
##                else:
##                    validity=False
##                    print("            > Month is not valid")
##    
##        else:
##            print("            > Wrong input")
##            time.sleep(1)
##            

def  bill(cursor,email): #bill function
    customer=[]
    print("               ******* BILL GENERATION *******")
    print()
    customer.append(str(input("                  Customer Name:")))
    customer.append(int(input("                  Customer Mobile:")))
    ids=[]
    quantity=[]
    addnext=1
    while(addnext==1):
        print()
        Id=str(input("                  Product ID?:"))
        if(validate_product(cursor,Id)):
            ids.append(Id)
            quantity.append(float(input("\n                  Quantity?:")))
            addnext=int(input("\n                  > Add next?(1/0):"))
        else:
            print("\n                  > Product ID doesn't exist\n")
            if(Id=="quit"):
                break
            time.sleep(2)
###BILL Printing
    if(len(ids)!=0):
        try:
            billno=generate_bill(cursor,email)
            cursor.execute("SELECT * FROM billmanager.shopdetails")
            shop=cursor.fetchone()
            print()
            print()
            print("%10s"%(""),end='')
            print("#"*60)
            print("%10s#%10s"%("",""),end='')
            print("%-39s"%(shop[0].upper()),end='')
            print("%9s#"%(""))
            print("%10s"%(""),end='')
            print("# %-56s #"%("Location:{}".format(shop[6])))
            print("%10s"%(""),end='')
            print("# %-28s%28s #"%("Contact:{}".format(shop[4]),"Email:{}".format(shop[5])))
            print("%10s#"%(""),end='')
            print("#"*58,end='')
            print("#")
            print("%10s"%(""),end='')
            print("# %-28s%28s #"%("Name:{}".format(customer[0]),"Mobile:{}".format(customer[1])))
            print("%10s#"%(""),end='')
            print(" %-56s #"%("Billno:{}".format(billno)))
            print("%10s#"%(""),end='')
            print("#"*58,end='')
            print("#")
            print("%10s# %-20s%-9s%-11s%-7s%9s #"%("","ITEM","RATE","QUANTITY","GST %","PRICE"))
            print("%10s#"%(""),end='')
            print("-"*58,end='')
            print("#")
            grand_total=0
            for i in range(len(ids)):
                cursor.execute("SELECT pro_title,pro_price,pro_gst FROM products where pro_id='{}'".format(ids[i]))
                row=cursor.fetchone()
                a=float(row[1])*quantity[i]
                item_total=(a+(float(row[2])/100)*a)
                grand_total=grand_total+item_total
                print("%10s# %-20s%-9s%-11s%-7s%9s #"%("",row[0],row[1],quantity[i],row[2],"{:.2f}".format(item_total)))
            print("%10s#"%(""),end='')
            print("-"*58,end='')
            print("#")
            print("%10s# %-20s%9s%11s%-2s%-14s #"%("","Grand Total:","","","","Rs {:.2f}".format(grand_total)))
            print("%10s#"%(""),end='')
            print("-"*58,end='')
            print("#")
            print("%10s#"%(""),end='')
            print("%30s"%("VISIT AGAIN...,"),end='')
            print(" "*28,end='')
            print("#")
            print("%10s"%(""),end='')
            print("#"*60)
            try:
                conn=connect_db()
                cursor=conn.cursor()
                items=','.join(ids)
                cursor.execute("INSERT INTO `billmanager`.`billings` (`bill_no`, `cust_name`, `cust_mob`, `items_id`, `total_cost`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(billno,customer[0],customer[1],items,grand_total))
                conn.commit()
                cursor.close()
                conn.close()
            except:
                print("\n                  > Problem while saving bill information!")
                conn.rollback()

        except:
            print("\n                  > Problem while generating the bill!")
    else:
       print("\n                  > No products selected!")

    time.sleep(2)     
            
            
    

def collect_product_details():
    fields=[]
    print()
    fields.append(str(input("                  ID:")))
    fields.append(str(input("                  Title:")))
    fields.append(str(input("                  Category:")))
    fields.append(float(input("                  Price:")))
    fields.append(float(input("                  GST:")))
    #fields.append(int(input("            Quantity:")))
    return fields


def validate_product(cursor,Id):
    try:
        cursor.execute("SELECT pro_id FROM billmanager.products where pro_id='{}'".format(Id))
        rows=cursor.rowcount
        if(rows==0):
            return False
        else:
            return True
    except:
        return False

def show_all_products(cursor):
    print(" %4s ----------------------------------------------------------------------------------------"%(""))
    print(" %5s |%-8s|%-30s|%-14s|%-15s|%-14s|"%("","ID","NAME","CATEGORY","PRICE(Rs.)","GST(%)"))
    print(" %4s ----------------------------------------------------------------------------------------"%(""))
    try:
        cursor.execute("SELECT * FROM billmanager.products")
        total=cursor.rowcount
        rows=cursor.fetchall()
        for row in rows:
            print(" %5s |%-8s|%-30s|%-14s|%-15s|%-14s|"%("",row[1],row[2],row[3],row[4],row[5]))
        print()
        if(total==0):
            print("%28s Currently no products are available to show"%(""))
        else:
            print("%33s Total:%d"%("",total))
        print(" %4s ---------------------------------------------------------------------------------------- "%(""))
    except:
        print("            > Problem while fetching the details!")
    time.sleep(5)

def generate_bill(cursor,email):
    currently=datetime.now()
    currently=str(currently.strftime("%Y%m%d%H%M%S"))
    name=None
    uid=None
    try:
        cursor.execute("SELECT id,user_name FROM billmanager.users where user_email='{}'".format(email))
        row=cursor.fetchone()
        uid=str(row[0])
        name=str(row[1])
        name=name[:2].upper()
    except:
        print("            > Problem while generating the bill number!")
        time.sleep(1)
    billno=uid+name+currently
    return billno

def get_bill_details(cursor):
    print()
    billno=str(input("            Bill no:"))
    try:
        cursor.execute("SELECT bill_no,cust_name,cust_mob,items_id,total_cost FROM billmanager.billings where bill_no='{}'".format(billno))
        rows=cursor.fetchone()
        if(len(rows)>0):
            print()
            print("            ******* BILL DETAILS *******")
            print()
            print("               Bill number:{}".format(rows[0]))
            print("               Customer name:{}".format(rows[1]))
            print("               Mobile:{}".format(rows[2]))
            print("               Date:{}\n               Time:{}".format(billno[9:11]+"-"+billno[7:9]+"-"+billno[3:7],billno[11:13]+":"+billno[13:15]+":"+billno[15:]))
            ids=rows[3].split(",")
            print("               Purchased items:",end='')
            for i in ids:
                cursor.execute("SELECT pro_title FROM billmanager.products where pro_id='{}'".format(i))
                its=cursor.fetchone()
                print(its[0],end=",")
            print("\n               Total price:{}".format(rows[4]))
            print("\n            *********************************** ")    
                
    except:
        print("\n               > Bill number not found!")
    time.sleep(2)



def logouttGreeting():
    time.sleep(1)
    print("    ",end='')
    print("_-"*5,end='')
    print(" Logged out ",end='')
    print("_-"*5,end='')
    print()
    time.sleep(1)
