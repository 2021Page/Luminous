create database luminous;

use mysql; create user 'user'@'%' identified by '1234';
grant select, insert, update, delete on luminous.* to 'user'@'%';

use luminous;

drop table testTable;

create table Product(
   product_ID int auto_increment,
   title varchar(45),
   price int,
   image varchar(100),
   category varchar(45),
   detail_category varchar(45),
   CONSTRAINT PK_Product PRIMARY KEY(product_ID),
   CONSTRAINT UQ_Product_title UNIQUE(title),
   CONSTRAINT UQ_Product_image UNIQUE(image)
);

create table User(
user_ID varchar(45),
password varchar(45),
user_Name varchar(45),
email varchar(45),
point int not null default 0,
Phone varchar(45),
city varchar(45),
gu varchar(45),
zipcode int,
CONSTRAINT PK_User PRIMARY KEY(user_ID),
CONSTRAINT UQ_User_email UNIQUE(email)
);

create table Questionnaire(
q_ID int, 
email varchar(45),
comment varchar(500),
user_ID varchar(45),
CONSTRAINT PK_Questionnaire PRIMARY KEY(q_ID),
CONSTRAINT FK_Questionnaire FOREIGN KEY (user_ID) REFERENCES User(user_ID)
);

create table Cart(
product_ID int,
user_ID varchar(45),
quantity int,
CONSTRAINT PK_Cart PRIMARY KEY(product_ID),
CONSTRAINT FK_Cart FOREIGN KEY (user_ID) REFERENCES User(user_ID)
);

create table Order_Info(
order_ID int,
order_Date date,
total_Price int,
order_Status varchar(45),
user_ID varchar(45),
CONSTRAINT PK_Order_Info PRIMARY KEY(order_ID),
CONSTRAINT FK_Order_Info FOREIGN KEY (user_ID) REFERENCES User(user_ID)
);

drop table event;
create table event(
event_ID int primary key NOT NULL,
event_Name varchar(45) not null
);

drop table Participate;
create table Participate(
user_ID varchar(45),
event_ID int, 
participation_Date date,
CONSTRAINT FK_Participate_User FOREIGN KEY (user_ID) REFERENCES User(user_ID),
CONSTRAINT FK_Participate_ID FOREIGN KEY (event_ID) REFERENCES Event(event_ID)
);

create table Coupon(
user_ID varchar(45), 
coupon_Num int,
CONSTRAINT FK_Coupon FOREIGN KEY (user_ID) REFERENCES User(user_ID)
);

create table Likes(
user_ID varchar(45),
Product_ID int,
CONSTRAINT FK_Likes FOREIGN KEY (user_ID) REFERENCES User(user_ID)
);

create table Buy(
order_ID int,
Product_ID int,
CONSTRAINT FK_Buy_Order FOREIGN KEY (order_ID) REFERENCES Order_Info(order_ID),
CONSTRAINT FK_Buy_Product FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

ALTER TABLE `luminous`.`cart` 
DROP FOREIGN KEY `FK_Cart`;
ALTER TABLE `luminous`.`cart` 
CHANGE COLUMN `user_ID` `user_ID` VARCHAR(45) NOT NULL ,
CHANGE COLUMN `quantity` `quantity` INT NOT NULL DEFAULT 1;
ALTER TABLE `luminous`.`cart` 
ADD CONSTRAINT `FK_Cart`
  FOREIGN KEY (`user_ID`)
  REFERENCES `luminous`.`user` (`user_ID`),
ADD CONSTRAINT `FK_Cart_product`
  FOREIGN KEY (`product_ID`)
  REFERENCES `luminous`.`product` (`product_ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `luminous`.`likes` 
DROP FOREIGN KEY `FK_Likes`;
ALTER TABLE `luminous`.`likes` 
CHANGE COLUMN `user_ID` `user_ID` VARCHAR(45) NOT NULL ,
CHANGE COLUMN `Product_ID` `Product_ID` INT NOT NULL ,
ADD INDEX `FK_Likes_product_idx` (`Product_ID` ASC) VISIBLE;
;
ALTER TABLE `luminous`.`likes` 
ADD CONSTRAINT `FK_Likes`
  FOREIGN KEY (`user_ID`)
  REFERENCES `luminous`.`user` (`user_ID`),
ADD CONSTRAINT `FK_Likes_product`
  FOREIGN KEY (`Product_ID`)
  REFERENCES `luminous`.`product` (`product_ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
ALTER TABLE `luminous`.`user` 
CHANGE COLUMN `point` `point` INT NULL DEFAULT '0' ;

ALTER TABLE `luminous`.`order_info` 
ADD COLUMN `order_Product` VARCHAR(45) NULL AFTER `user_ID`;

ALTER TABLE `luminous`.`buy` 
DROP FOREIGN KEY `FK_Buy_Order`;

ALTER TABLE `luminous`.`buy` 
CHANGE COLUMN `order_ID` `order_ID` INT NULL AUTO_INCREMENT ;

ALTER TABLE `luminous`.`buy` 
ADD CONSTRAINT `FK_Buy_Order`
  FOREIGN KEY (`order_ID`)
  REFERENCES `luminous`.`order_info` (`order_ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
ALTER TABLE `luminous`.`questionnaire` 
CHANGE COLUMN `q_ID` `q_ID` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `luminous`.`order_info` 
DROP COLUMN `order_Product`;

ALTER TABLE event DROP participant_Num;
ALTER TABLE event DROP event_Content;

ALTER TABLE `luminous`.`event` 
DROP FOREIGN KEY `FK_Event_User`;
ALTER TABLE `luminous`.`event` 
CHANGE COLUMN `user_ID` `event_ID` VARCHAR(45) NOT NULL FIRST,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`event_ID`),
DROP INDEX `FK_Event_User` ;
;

drop table Participate;
ALTER TABLE `luminous`.`event` 
CHANGE COLUMN `event_ID` `event_ID` INT NOT NULL ;
create table Participate(
user_ID varchar(45),
event_ID int, 
participation_Date date,
CONSTRAINT FK_Participate_User FOREIGN KEY (user_ID) REFERENCES User(user_ID),
CONSTRAINT FK_Participate_ID FOREIGN KEY (event_ID) REFERENCES Event(event_ID)
);


insert into product(title, price, image, category, detail_category) values('Sky Smudge', 14, '/media/product/nail1.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Sky Bloom', 13, '/media/product/nail2.png', 'nail', 'best');
insert into product(title, price, image, category, detail_category) values('Slim French', 8, '/media/product/nail3.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Frost White', 8, '/media/product/nail4.png', 'nail', 'new');
insert into product(title, price, image, category, detail_category) values('Sweet Orchid', 11, '/media/product/nail5.png', 'nail', 'new');
insert into product(title, price, image, category, detail_category) values('Black Paradise', 10, '/media/product/nail6.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Romantic Seaside', 13, '/media/product/nail7.png', 'nail', 'new');
insert into product(title, price, image, category, detail_category) values('Charming Daisy', 14, '/media/product/nail8.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Sunflower', 12, '/media/product/nail9.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Lilac Spell', 8, '/media/product/nail10.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Rose Pop', 12, '/media/product/nail11.png', 'nail', 'best');
insert into product(title, price, image, category, detail_category) values('Flower Rain', 12, '/media/product/nail12.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Coral Picnic', 8, '/media/product/nail13.png', 'nail', NULL);
insert into product(title, price, image, category, detail_category) values('Love Sonnet', 12, '/media/product/nail14.png', 'nail', 'best');
insert into product(title, price, image, category, detail_category) values('Orange Crush', 9, '/media/product/nail15.png', 'nail', NULL);

insert into product(title, price, image, category, detail_category) values('Cotton Candy', 9, '/media/product/pedi1.png', 'pedi', 'best');
insert into product(title, price, image, category, detail_category) values('Crayon', 10, '/media/product/pedi2.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Wonder Land', 11, '/media/product/pedi3.png', 'pedi', 'new');
insert into product(title, price, image, category, detail_category) values('Starry Night', 13, '/media/product/pedi4.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('My Daisy', 10, '/media/product/pedi5.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Bling Bling', 9, '/media/product/pedi6.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Water Lily', 10, '/media/product/pedi7.png', 'pedi', 'new');
insert into product(title, price, image, category, detail_category) values('Mint Latte', 8, '/media/product/pedi8.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Blaze', 10, '/media/product/pedi9.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Red Berry', 11, '/media/product/pedi10.png', 'pedi', 'best');
insert into product(title, price, image, category, detail_category) values('Yellow Stitch', 12, '/media/product/pedi11.png', 'pedi', 'best');
insert into product(title, price, image, category, detail_category) values('Never Land', 12, '/media/product/pedi12.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Romantic', 14, '/media/product/pedi13.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Basic Mood', 15, '/media/product/pedi14.png', 'pedi', NULL);
insert into product(title, price, image, category, detail_category) values('Yellow Smile', 13, '/media/product/pedi15.png', 'pedi', 'new');

insert into product(title, price, image, category, detail_category) values('Gel Lamp', 20, '/media/product/lamp.jpg', 'care', NULL);
# title price image category detail_category


insert into event values(1, 'Luminous New Member Event');
insert into event values(2, 'Luminous SNS Authentication Event');
insert into event values(3, 'Luminous Kakao Channel Addition Event');
# event_id, event_name



#view
CREATE VIEW user_mypage AS SELECT U.user_ID, U.user_Name, U.point FROM luminous.user U;
SELECT * from user_mypage;