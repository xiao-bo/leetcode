# Write your MySQL query statement below
# using join
# it also use window function to reduce space complexity
with cte(id1, id2, id3)
as (
select 
s1.id, s2.id, s3.id
from Stadium as s1
inner join Stadium as s2
on s1.id+1 = s2.id
inner join Stadium as s3
on s1.id+2 = s3.id
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
)
select 
distinct 
id,
visit_date,
people 
from Stadium
where id in (select id1 from cte) or id in (select id2 from cte) 
or id in (select id3 from cte)
