import mysql.connector as con
from prettytable import PrettyTable


conn=con.connect(host='localhost',user='root',passwd='admin', database='CarManagement')
if conn.is_connected():
    print('Succesfully Connected!')

cur=conn.cursor()


print('------------------+----------------------+--------------------+',
      '---------------------+-------------------')
print('\u0332'.join('Car Management System'))
print('Your Login Credentials are:')
print('User Name: "Pro"')
print('Password: 1234')
print('NOTE: It\'s case sensitive')
print('------------------+----------------------+--------------------+',
      '---------------------+-------------------')
print('1. Login')
print('2. Exit')
choice1=int(input('Enter your choice please: '))
if choice1==1:
    l1=input('Enter your User Name: ')
    l2=input('Enter your password: ')
    if l1=='Pro' and l2=='1234':
        print('Logged in. Welcome User.')
        print('')
        print('Welcome to the','\u0332'.join('Cᴀʀ Mᴀɴᴀɢᴇᴍᴇɴᴛ Sʏsᴛᴇᴍ'))
        print('')
        print('You can choose to add details about a Car, Add details about the Owner, and see all',
              'the details of the Cars and Owners and have a look if the Owners are selling their',
              'cars at a lower price.')

    while l1=='Pro' and l2=='1234':
        print('1. Add Car Details')
        print('2. Add Owner Details')
        print('3. Cars on Sale Details')
        print('4. All Car Details')
        print('5. All Owner Details')
        print('6. All Sale Details')
        print('7, Search for Car')
        print('8. Search for Owner')
        print('9. Search for Sale')
        print('10. Exit')
        choice2=int(input('Enter your choice please: '))
        if choice2==1:
            b_name=input('Enter Car Name: ')
            o_name=input('Enter Owner Name: ')
            price=int(input('Enter Price: '))
            y_o_rel=int(input('Enter Year of Release: '))
            fuel=input('Enter Fuel used: ')
            cmd='insert into car_details values(%s,%s,%s,%s,%s)'
            val=[b_name, o_name, price, y_o_rel, fuel]
            cur.execute(cmd,val)
            print('Succesfully Added Details')
            myTable=PrettyTable(['Car','Owner_Name','Price','Year_Of_Release','Fuel'])
            myTable.add_row([b_name, o_name, price, y_o_rel, fuel])
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
            conn.commit()
        elif choice2==2:
            o_name=input('Enter Owner Name: ')
            car=input('Enter Car Name: ')
            price=int(input('Enter Price: '))
            y_o_pur=int(input('Enter Year of Purchase: '))
            fuel=input('Enter Fuel used: ')
            o_address=input('Enter Owner Address: ')
            cmd='insert into owner_details values(%s,%s,%s,%s,%s,%s)'
            val=[o_name,car,price,y_o_pur,fuel,o_address]
            cur.execute(cmd,val)
            print('Succesfully Added Details')
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address'])
            myTable.add_row([o_name,car,price,y_o_pur,fuel,o_address])
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
            conn.commit()
        elif choice2==3:
            o_name=input('Enter Owner Name: ')
            car=input('Enter Car Name: ')
            price=int(input('Enter Original Price: '))
            y_o_pur=int(input('Enter Year of Purchase: '))
            fuel=input('Enter Fuel used: ')
            o_address=input('Enter Owner Address: ')
            s_pri=int(input('Enter Sale Price: '))
            cmd='insert into sale_details values(%s,%s,%s,%s,%s,%s,%s)'
            val=[o_name,car,price,y_o_pur,fuel,o_address,s_pri]
            cur.execute(cmd,val)
            print('Succesfully Added Details')
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address', 'Sale_Price'])
            myTable.add_row([o_name,car,price,y_o_pur,fuel,o_address,s_pri])
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
            conn.commit()
        elif choice2==4:
            cur.execute('select * from car_details')
            r=cur.fetchall()
            myTable=PrettyTable(['Car','Owner_Name','Price','Year_Of_Release','Fuel'])
            for i in r:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==5:
            cur.execute('select * from owner_details')
            r=cur.fetchall()
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address'])
            for i in r:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==6:
            cur.execute('select * from sale_details')
            r=cur.fetchall()
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address', 'Sale_Price'])
            for i in r:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==7:
            inp=input('Enter the Car Name to Search for: ')
            cmd='select * from car_details where Car=%s'
            val=[inp]
            cur.execute(cmd,val)
            u=cur.fetchall()
            myTable=PrettyTable(['Car','Owner_Name','Price','Year_Of_Release','Fuel'])
            for i in u:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==8:
            inp=input('Enter the Owner Name to Search for: ')
            cmd='select * from owner_details where Owner_Name=%s'
            val=[inp]
            cur.execute(cmd,val)
            u=cur.fetchall()
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address'])
            for i in u:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==9:
            inp=input('Enter Car to search Sale for: ')
            cmd='select * from sale_details where Car=%s'
            val=[inp]
            cur.execute(cmd,val)
            u=cur.fetchall()
            myTable=PrettyTable(['Owner_Name', 'Car', 'Price', 'Year_Of_Purchase',
                                 'Fuel', 'Address', 'Sale_Price'])
            for i in u:
                myTable.add_row(i)
            print(myTable)
            print('------------------+----------------------+--------------------+',
                  '---------------------+-------------------')
            print('')
        elif choice2==10:
            break
        
if choice1==2:
    exit()
