create table devices(
id int(11) AUTO_INCREMENT,
    nombreDevice varchar(20),
    primary key(id)
);

create table devicepos(
id int(11) AUTO_INCREMENT,
    lat Double,
    lng Double,
    fecha date,
    deviceId int(11),
    primary key(id),
    FOREIGN key (deviceId) REFERENCES devices(id)
);