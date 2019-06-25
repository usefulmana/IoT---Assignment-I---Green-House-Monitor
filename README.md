## **COSC 2790 - Programming IoT - Assignment I**

**Group**: 3.14

**Members:** Nguyen Le Bao Anh (s3616128) - 

**Github: [Link](https://github.com/usefulmana/IoT---Assignment-I---Green-House-Monitor)** <br> 

**Project Description:** 

#### Required packages:
    - python version >= 3.5.3
    - sense-hat
    - pybluez
    - python-crontab
    - mysql-connector
    - matplotlib
    - pushbullet.py
    - seaborn

#### Setting up:
In order to run this program in your RPi, you will need to set up a local MySQL server. Follow the steps below:
- SSH into your machine, and install mysql server and client:
    ``````
    sudo apt-get install mysql-server mysql-client
    ``````
- Log into mysql as root:
    ````
    sudo mysql
    ````
- Create a new database:
    ````
    create database your_database_name;
    ````
- Create a new user:
    ````
    create user 'your_user_name' identified by 'your_password';
    ````
- Grant privileges to new user:
    ````
    grant usage on your_database_name.* to 'your_user_name'@localhost identified by 'your_password';
    flush privileges;
    ````
- Check if user has privileges:
    ````
    show grants for 'your_user_name'@localhost;
    ````
- Fill the appropriate information in database.py
- To receive notification, get your API key from [Pushbullet](https://www.pushbullet.com/) and fill in the appropriate 
info in notification.py
- Go to your local folder, and create a setup.json file that follows the below format and fill the missing information:
    ````
    {
  "database_name": "your database name",
  "host": "your_host(usually localhost)",
  "user": "your username",
  "password": "your password",
  "API_KEY": "pushbullet api key"}
    ````

To run the program, simply run scheduler.py which will run the programs in a predetermined schedule.
Or you can just run each file individually. Three executable files are:
- monitorAndNotify.py: will log temperature and humidity into the mysql database and send out notification if any
parameter exceeds the predetermined range.

- createReport.py: will create two reports. One with status of each day. Another one with a detailed report that 
includes the information such as: average and min/max temperature/humidity.

- bluetooth_messenger.py: will scan any device that has a preset MAC address and send out notification regarding current
temperature and humidity.