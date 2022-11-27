select *
from pizza_order
inner join "user"
on pizza_order."user" = public."user".id;

select "user".name, "user".address, po.pizza
from pizza_order as po
inner join "user"
on po.user = "user".id;
