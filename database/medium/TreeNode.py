# Write your MySQL query statement below
# 1. p_id = null的，一定屬於root
# 2. id 不在p_id裡面的，一定屬於leaf
# 3. else，屬於inner node

select 
id,
case 
    when ifnull(p_id, 'null') = 'null' then 'Root'
    when id not in (select distinct p_id from Tree where p_id is not null ) then 'Leaf'
    else 'Inner'
end as 'type'
from Tree
