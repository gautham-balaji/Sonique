import mysql.connector as con

conn=con.connect(host='localhost',user='root',passwd='admin')
if conn.is_connected():
    print('Succesfully Connected!')

cur=conn.cursor()
cur.execute ('drop database if exists CarManagement')
cur.execute('create database CarManagement')
cur.execute('use CarManagement')
conn.commit()

cur.execute('create table car_details(Car varchar(20), Owner_Name char(30), Price int(9), Year_Of_Release int(4), Fuel char(9))')
cur.execute('create table owner_details(Owner_Name char(30), Car varchar(20), Price int(9), Year_Of_Purchase int(4), Fuel char(10), Address varchar(50))')
cur.execute('create table sale_details(Owner_Name char(30), Car varchar(20), Price int(9), Year_Of_Purchase int(4), Fuel char(10), Address varchar(50), Sale_Price int(9))')
conn.commit()

cur.execute('insert into car_details values("Mercedes AMG One", "Toto Wolff", 100000000, 2022, "Petrol")')
cur.execute('insert into car_details values("Pagani Utopia", "Karthick", 79000000, 2022, "Petrol")')
cur.execute('insert into car_details values("McLaren MP4-12C", "Suresh", 9850000, 2010, "Petrol")')
cur.execute('insert into car_details values("Bugatti Chiron", "Andrew",  28000000, 2016, "Diesel")')
cur.execute('insert into car_details values("Tesla Model X", "Adithya", 2400000, 2016, "Electric")')
conn.commit()

cur.execute('insert into owner_details values("Toto Wolff", "Mercedes AMG One", 100000000, 2022, "Petrol", "Thiruvanmiyur")')
cur.execute('insert into owner_details values("Karthick", "Pagani Utopia", 79000000, 2022, "Petrol", "Adyar")')
cur.execute('insert into owner_details values("Suresh", "McLaren MP4-12C", 9850000, 2017, "Petrol", "Egmore")')
cur.execute('insert into owner_details values("Andrew",  "Bugatti Chiron", 28000000, 2019, "Diesel", "Chengelpettu")')
cur.execute('insert into owner_details values("Adithya", "Tesla Model X", 2400000, 2018, "Electric", "T Nagar")')
conn.commit()

cur.execute('insert into sale_details values("Mukunth", "Maruti Swift", 990000, 2011, "Petrol", "Thiruvanmiyur", 560000)')
cur.execute('insert into sale_details values("Manikandan", "Hyundai i20", 1200000, 2015, "Petrol", "Adyar", 879000)')
cur.execute('insert into sale_details values("Subhu", "Honda Amaze", 1140000, 2012, "Petrol", "Egmore", 780000)')
cur.execute('insert into sale_details values("Gopal",  "Honda WRV", 1280000, 2017, "Diesel", "Chengelpettu", 980000)')
cur.execute('insert into sale_details values("Vivek", "Tata Nexon", 1750000, 2022, "Electric", "T Nagar", 1305000)')
conn.commit()
