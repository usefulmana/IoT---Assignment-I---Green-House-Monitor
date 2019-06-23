create table data_log (
    id int not null auto_increment primary key,
    date datetime not null,
    temperature float not null,
    humidity float not null
);

create table daily_notification(
    id int not null  auto_increment primary key,
    record_date date unique not null,
    status varchar(255) not null
);

# create table daily_data_report(
#     id int not null auto_increment primary key,
#     record_date date unique not null,
#     avg_temperature float not null,
#     avg_humidity float not null,
#     min_temperature float not null,
#     max_temperature float not null,
#     min_humidity float not null,
#     max_humidity float not null
# );

select round(avg(temperature),2), round(avg(humidity),2) from data_log where date between '2019-06-21 00:00:00' and '2019-06-21 23:59:59';
select max(temperature), max(humidity) from data_log where date between '2019-06-21 00:00:00' and '2019-06-21 23:59:59';
select min(temperature), min(humidity) from data_log where date between '2019-06-21 00:00:00' and '2019-06-21 23:59:59';

select distinct date(date) from data_log;

select distinct date(date) from data_log order by date(date) desc limit 7;

select date, humidity from data_log where humidity > 60 and date between '2019-06-23 00:00:00' and '2019-06-23 23:59:59';