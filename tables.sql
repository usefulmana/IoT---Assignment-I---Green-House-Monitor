create table data_log (
    id int not null auto_increment primary key,
    date datetime not null,
    temperature float not null,
    humidity float not null
)
