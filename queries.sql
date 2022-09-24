insert into items(name, price)
values ('Corolla', 30000), ('Civic', 29000), ('Focus', 26000), ('Rav4', 38000), ('CR-V', 36000),
('X1', 42000), ('Golf', 31000), ('Tiguan', 39000), ('Camry', 33000), ('Accord', 3000);

select i.id, i.name , i.price 
from items i;

select i.id, i.name , i.price 
from items i
where i.price >= 30000;

call get_all_items;
call filter_by_price(30000);