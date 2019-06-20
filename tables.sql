create table data_log (
    id int not null auto_increment primary key,
    date datetime not null,
    temperature float not null,
    humidity float not null
);

create table daily_report(
    id int not null  auto_increment primary key,
    record_date datetime not null,
    status varchar(255) not null
);