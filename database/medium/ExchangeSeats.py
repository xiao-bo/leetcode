# Write your MySQL query statement below
# solution 1: window function
# solution 2: join solution

# solution 1: window function
with cte (id, student)
as (
    select 
    s1.id,
    ifnull(s2.student, s1.student) as student
    from Seat as s1
    left join Seat as s2
    on s1.id +1 = s2.id 
    where s1.id %2 = 1
    union 
    select 
    s1.id,
    ifnull(s2.student, s1.student) as student
    from Seat as s1
    left join Seat as s2
    on s1.id = s2.id+1
    where s1.id %2 = 0
)
select 
id, 
student
from cte
order by id asc


# solution 2: join solution
select id, student
from (
    select
    id,
    lead(student, 1, student) over (order by id asc) as student
    from Seat
) subquery
where id %2 = 1
union
select id, student
from (
    select
    id,
    lag(student, 1, student) over (order by id asc) as student
    from Seat
) subquery
where id %2 = 0
order by id asc
