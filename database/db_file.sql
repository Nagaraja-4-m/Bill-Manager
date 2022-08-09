create database billmanager;
use billmanager;

#shop details table
CREATE table shopdetails(
           shop_name varchar(120) not null,
           shop_note varchar(200),
		   shop_owner_name varchar(70) not null,
           shop_landline  varchar(12),
           shop_mobile varchar(10) not null,
           shop_email varchar(320) not null,
           shop_address varchar(255) not null
		);
        
##SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'shopdetails';

## admin and users account
##status_role=1 represents the admin status_role=2 represents the members
create table users( 
id int  auto_increment,
user_name varchar(100),
user_mobile varchar(10) ,
user_email varchar(100) ,
user_password varchar(16),
status_role int default 1,
primary key(id)
);


## products table
create table products(
id int auto_increment,
pro_id varchar(10),
pro_title varchar(50),
pro_category varchar(50),
pro_price float,
pro_gst float default 2.1,
primary key(id)
);



#billings table
create table billings
(
id int auto_increment,
bill_no varchar(18),
cust_name varchar(20),
cust_mob varchar(10),
items_id varchar(200),
total_cost float,
date_time datetime NOT NULL DEFAULT current_timestamp(),
primary key(id)
);
