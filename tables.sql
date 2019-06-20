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

create table daily_data_report(
    id int not null auto_increment primary key,
    record_date date unique not null,
    avg_temperature float not null,
    avg_humidity float not null,
    min_temperature float not null,
    max_temperature float not null,
    min_humidity float not null,
    max_humidity float not null
)