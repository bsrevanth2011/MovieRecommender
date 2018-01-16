insert into Competition_2 values
('Hawaii', '11:15', '2010-11-22'),
('London', '15:30', '2011-11-22'),
('California', '15:20', '2012-11-22');

insert into Competition values 
('C001', 'Competition 1', '2010-11-22'),
('C002', 'Competition 2', '2011-11-22'),
('C003', 'Competition 3', '2012-11-22');

insert into Event_Head values
('EH001', 'Akshay Prabhu'),
('EH002', 'Revanth'),
('EH003', 'Abhishek');

insert into Events values
('E001', 'Event_1', 'EH001'),
('E002', 'Event_2', 'EH001'),
('E003', 'Event_3', 'EH002');

insert into Winner_2 values
(1, 45000, 1000 ),
(2, 35000, 2000 ),
(3, 25000, 4000 ),
(5, 25000, 2500 ),
(6, 55000, 2300 );


insert into Department_Head values
('DH001', 'Ramohan', 'Reddy'),
('DH002', 'Deethi', 'L'),
('DH003', 'Biju', 'Mohan');

insert into Department values
('D001', 'IT', 'DH001'),
('D002', 'CS', 'DH002'),
('D003', 'EE', 'DH003');

insert into Teams values
('T001', 'abc', 'Ninjas', 'Las Vegas'),
('T002', 'def', 'Atlantians' , 'Bangalore'),
('T003', 'ghi', 'Amazons' , 'Mangalore'),
('T004', 'xyz', 'Avengers', 'Miami'),
('T005', 'xyz', 'Justice League', 'Boston'),
('T006', 'pqr', 'Suicide Squad', 'Gotham');


insert into Team_member values
('TM001', 'DeadPool', '1997-10-30'),
('TM002', 'Deathstroke', '1997-10-30'),
('TM003', 'Superman', '1997-10-30'),
('TM004', 'Wonderwoman', '1997-10-30'),
('TM005', 'Aquaman', '1997-10-30'),
('TM006', 'Cyborg', '1997-10-30');

insert into Team_members_2 values
('9945012034', 'TM001'),
('9921342324', 'TM002'),
('6935232485', 'TM003'),
('2352223423', 'TM004'),
('6336363634', 'TM005'),
('7459527392', 'TM006');

insert into Faculty_member values
('FM001', 'Deepthi'),
('FM002', 'Sangeetha'),
('FM003', 'Geetha'),
('FM004', 'Biju'),
('FM005', 'Sidney Rosario'),
('FM006', 'Tulasi');

insert into Judge values
('Ironman', 'J001', '10'),
('Thor', 'J002', '10'),
('Hulk', 'J003', '10'),
('Hawkeye', 'J004', '10'),
('Daredevil', 'J005', '10'),
('Strange', 'J006', '10');

insert into Facilitate values
('DH001', 'T001'),
('DH002', 'T002'),
('DH003', 'T003');

insert into contain values
('TM001', 'FM001', 'T001'),
('TM002', 'FM001', 'T001'),
('TM003', 'FM002', 'T002'),
('TM004', 'FM002', 'T002'),
('TM005', 'FM003', 'T003'),
('TM006', 'FM003', 'T003');

insert into Finance_Committee values
(20, 'Berkshire_Hathaway','FC002', CURRENT_DATE , 'E001'),
(30, 'Goldman_Sachs','FC001', CURRENT_DATE , 'E002'),
(50, 'Morgan_Stanley','FC003', CURRENT_DATE , 'E003');

insert into Winner values
('T001' ,'Ninjas' , 1000 , 'J001'),
('T002' ,'Atlantians' , 2000 , 'J002'),
('T003' ,'Amazons' , 4000 , 'J003'),
('T004', 'Avengers', 4000, 'J001'),
('T005', 'Justice League', 2500, 'J002'),
('T006', 'Suicide Squad', 2300, 'J003');


insert into Consists_of values
('D001', 'E001', 'C001'),
('D001', 'E002', 'C002'),
('D002', 'E003', 'C003');

insert into Take_part_in values
('T001', 'J001', 'C001'),
('T002', 'J002', 'C002'),
('T003', 'J003', 'C003'),
('T001', 'J004', 'C001'),
('T002', 'J005', 'C002'),
('T003', 'J006', 'C003');

insert into Give_prizes values
(10000, 20 , 'J001', 'T001' ),
(9000, 30 , 'J002', 'T003' ),
(11000, 20 , 'J003', 'T001' ),
(12000, 50 , 'J003', 'T002' ),
(9500, 40 , 'J002', 'T002' ),
(8500, 50 , 'J005', 'T003' );








