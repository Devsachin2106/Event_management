Create table events (
  id serial Primary key,
  event Varchar(255) NOT NULL,
  place Varchar(255) NOT NULL,
  amount int NOT NULL
);

Create table special_events (
  id serial primary key,
  special_feature varchar(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES events(id)
);

Create table attendees (
  id int primary key,
  event_id serial ,
  name varchar(100),
  email varchar(100),
  phone varchar(20),
  FOREIGN KEY (event_id) REFERENCES events(id)
);

Create table payments (
  id int primary key,
  event_id serial,
  amount decimal(10, 2),
  payment_date date,
  FOREIGN KEY (event_id) REFERENCES events(id)
);



Insert into events (event, place, amount)
Values ('Birthday Party', 'Venue A', 1000),
       ('Conference', 'Venue B', 5000),
       ('Wedding', 'Venue C', 8000);

Insert into special_events (special_feature)
Values ( 'Live Music'),
       ( 'Keynote Speaker'),
       ( 'Fireworks');

Insert into attendees (id,name, email, phone,address)
Values
  (1,'Sachin', 'sachin6445@gmail.com', '6385560918','madurai'),
  (2,'vetrivel', 'vetrivel123@gmail.com', '7876234590','chennai'),
  (3,'Prasad', 'prasad321@gmail.com', '8908451230','vellore'),
  (4,'Sakthi', 'sakthi7654@gamil.com', '9832906587','theni'),
  (5,'Santhosh', 'santhosh657@gmail.com', '9856769012','trichy'),
  (6,'Ajay', 'ajay098@gmail.com', '8732543456','nellai');
update attendees set name='vignesh' where id=1;'its update and replace the specific word in table'

delete from attendees where id='1'; 'its delete the specic row in the table'

alter table attendees add column address varchar(102); 'Its add a new coloumn in table'

select distinct email from attendees;   'its specify the take on neeed coloumn'

select * from attendees order by name asc;

select name,email from attendees group by name,email;

select * from attendees where email like '%s';

select * from attendees;
  
Insert into payments (id, amount, payment_date)
Values
  (1, 100.00, '2023-06-15'),
  (2, 75.50, '2023-06-16'),
  (3, 200.00, '2023-06-18'),
  (4, 150.00, '2023-06-17'),
  (5, 50.50, '2023-06-19'),
  (6, 100.00, '2023-06-20');
  
select * from events;
select * from special_events;
select avg(amount) from payments;
select * from payments where amount>=100;