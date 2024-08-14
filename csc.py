import mysql.connector as con
conn=con.connect(host='localhost',user='root',password='admin',database='BikeManagement')
if conn.isconnected():
    print('Succesfully Connected!')

cur=conn.cursor()
print('------------------+----------------------+--------------------+---------------------+-------------------')
print('Bike Management System')
print('Your Login Credentials are:')
print('User Name: "Pro"')
print('Password: 1234')
print('------------------+----------------------+--------------------+---------------------+-------------------')
print('1. Login')
print('2. Exit')
choice1=int(input('Enter your choice please: '))
if choice1==1:
    l1=input('Enter your User Name: ')
    l2=input('Enter your password: ')
    while l1=='Pro' and l2='1234':
        print('Logged in. Welcome User.')

        print('Welcome to the Bike Management System')
        print('You can choose to add details about a Bike, Add details about the Owner, and see all the details of the Bikes and Owners and have a look if the Owners are selling their bikes at a lower price.')
        print('1. Add Bike Details')
        print('2. Add Owner Details')
        print('3. Bikes on Sale Details')
        print('4. All Bike Details')
        print('5. All Owner Details')
        print('6. All Sale Details')
        print('7, Search for Bike')
        print('8. Search for Owner')
        print('9. Search for Sale')
        choice2=int(input('Enter your choice please: '))
        if choice2==1:
            b_name=input('Enter Bike Name: ')
            o_name=input('Enter Owner Name: ')
            price=int(input('Enter Price: '))
            y_o_rel=int(input('Enter Year of Release: '))
            fuel=input('Enter Fuel used: ')
            cur.execute(f'insert into bike_details values({b_name},{o_name},{price},{y_o_rel},{fuel})')
            print('Succesfully Added Details')
            conn.commit()
        elif choice2==2:
            o_name=input('Enter Owner Name: ')
            o_address=input('Enter Owner Address: ')
            bike=input('Enter Bike Name: ')
            y_o_pur=int(input('Enter Year of Purchase: '))
            fuel=input('Enter Fuel used: ')
            cur.execute(f'insert into owner_details values({o_name},{o_address},{bike},{y_o_pur},{fuel})')
            print('Succesfully Added Details')
            conn.commit()
        elif choice2==3:
            o_name=input('Enter Owner Name: ')
            o_address=input('Enter Owner Address: ')
            bike=input('Enter Bike Name: ')
            y_o_pur=int(input('Enter Year of Purchase: '))
            fuel=input('Enter Fuel used: ')
            price=int(input('Enter Original Price: '))
            s_pri=int(input('Enter Sale Price: '))
            c_numb=int(input('Enter Contact Number: '))
            cur.execute(f'insert into sale_details values({o_name},{o_address},{bike},{y_o_pur},{fuel},{price},{s_pri},{c_numb})')
            print('Succesfully Added Details')
            conn.commit()
        elif choice2==4:
            cur.execute('select * from bike_details')
            r=cur.fetchall()
            for i in r:
                print(i)
        elif choice2==5:
            cur.execute('select * from owner_details')
            r=cur.fetchall()
            for i in r:
                print(i)
        elif choice2==6:
            cur.execute('select * from sale_details')
            r=cur.fetchall()
            for i in r:
                print(i)
        elif choice2==7:
            inp=input('Enter the Bike Name to Search for: ')
            cur.execute(f'select * from bike_details where Bike_Name=({inp})')
            u=c1.fetchall()
            for i in u:
                print(i)
        
