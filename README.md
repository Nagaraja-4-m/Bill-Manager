# Bill-Manager
Bill Manager is a non-GUI, general purpose billing management system developed using Python3 and MySQL.
![image](https://user-images.githubusercontent.com/89149882/139582640-9f75fce5-b35a-4862-b063-4c5e1af4cd06.png)

Admin functionalities:
 1. Account management
 2. Members management
 3. Products management
 4. Billing
 5. Bill information
 
Members functionalities:
 1. Account management
 2. Products information
 3. Billing
 4. Bill information

**Setup:**
1. Install/update  latest python(3.9 or above recommended)
2. Install/Update Mysql(8.0 or above)
3. Install/update MysQL-python interface

4. login to  mysql workbench and import file `db_file.sql` from 'database' directory and execute the code. This will creates  database and all necessary tables.
5. go to `connection.py`  file and update your mysql 'user' and 'password' details in    `connect_db()` function.
6. run `main.py` file 

Note:To  run this code in linux based system please find 'os.system("cls")' statements in all the files and replace it to ' os.system("clear")'


**Files:**
main --  execution stars from here
initial_setup -- when runs first time, to set shop and user account details
validation -- to authenticate user/member
connection -- to connect database
admin -- had admin menu
member -- had member menu
funct -- had all functionalities
database/db_file -- had SQL code to create necessary database and tables


Initial setup.
![Initial setup](https://user-images.githubusercontent.com/89149882/139580999-94a33198-b244-417e-b6ec-db248ae7d882.png)

Admin menu:
![Admin](https://user-images.githubusercontent.com/89149882/139581068-5b34ca12-d454-440a-b6fc-cbb91dd95642.png)

Member menu:
![image](https://user-images.githubusercontent.com/89149882/139582547-74aef67c-18e3-45a5-bbe3-1ce5d021883e.png)

product management/adding products:
![Add product](https://user-images.githubusercontent.com/89149882/139581445-7718e19a-05e5-418a-9690-4821ae1f6564.png)

Bill Generation:
![image](https://user-images.githubusercontent.com/89149882/139581994-c6901aa6-b02e-4ac7-87b8-b415511e3098.png)

Bill Information:
![image](https://user-images.githubusercontent.com/89149882/139582092-798f8cf8-8983-417a-a448-789c474bf75e.png)

Products:
![image](https://user-images.githubusercontent.com/89149882/139582874-e8b352e1-1942-47ea-8be3-f1bc6e379693.png)

user details:
![image](https://user-images.githubusercontent.com/89149882/139582911-c324b06d-cce1-4000-a227-d9dfc1e5f619.png)

