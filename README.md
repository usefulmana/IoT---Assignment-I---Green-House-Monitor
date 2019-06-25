## **COSC 2790 - Programming IoT - Assignment I**

**Group**: 3.14

**Members:** Nguyen Le Bao Anh (s3616128) - 

**Github: [Link](https://github.com/usefulmana/IoT---Assignment-I---Green-House-Monitor)** <br> 

**Project Description:** A green house monitor that records temperature and humidity and notify users if measurements
are within range or not. Additionally, this program will also generate relevant reports and charts to inform users.

#### Required packages:
    - python version >= 3.5.3
    - sense-hat
    - pybluez
    - python-crontab
    - mysql-connector
    - matplotlib
    - pushbullet.py
    - seaborn
To install all dependencies:
````
pip install -r requirements.txt
````
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
### Bluetooth
To use the notification feature via BlueTooth, you must own a BlueTooth-capable device (your smartphone or laptop).
- You will need to pair your device with RPi
- Install the following packages to your RPi:
    ````
    sudo apt-get install bluetooth bluez blueman bluez-tools
    ````
- Install the Pushbullet application/plugin on your devices
- Turn on Bluetooth and make your device discoverable when you want to receive notifications

### Running the program

To run the program, simply run scheduler.py which will run the programs in a predetermined schedule.
Or you can just run each file individually. The executable files are:
- monitorAndNotify.py: will log temperature and humidity into the mysql database and send out notification if any
parameter exceeds the predetermined range.

- createReport.py: will create two reports. One with status of each day. Another one with a detailed report that 
includes the information such as: average and min/max temperature/humidity.

- bluetooth_messenger.py: will scan for BlueTooth devices in the nearby area and detect if any device matches with paired
devices' MAC addresses. Should a match occur, a notification will be sent out via Pushbullet.

- analytics.py: this script will create an array of plots that displaying any relevant data collected from RPi.