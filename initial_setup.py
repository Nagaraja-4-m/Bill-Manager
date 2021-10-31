########## Initial setup ############

def setup(Scolumns):
    shop_details=[]
    admin_details=[]
    print(' ====================== SETUP ====================== ')
    print('   Shop details:')
    print('   -------------')
    for i in Scolumns:
        shop_details.append(str(input("   {}:".format(i[0].upper()))))
    print('   -------------')
    print('')
    print('   Admin details:')
    print('   -------------')
    admin_details.append(str(input("   USER_NAME:")))
    admin_details.append(str(input("   USER_MOBILE:")))
    admin_details.append(str(input("   USER_EMAIL:")))
    admin_details.append(str(input("   PASSWORD:")))
    print('   -------------')
    return shop_details,admin_details

