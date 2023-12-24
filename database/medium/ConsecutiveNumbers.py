# Write your MySQL query statement below
# 1. join solution
# 2. window function

# solution1: join 
select
distinct l1.num as ConsecutiveNums
from logs as l1
inner join logs as l2
on l1.id+1 = l2.id
inner join logs as l3
on l1.id+2 = l3.id
where l1.num = l2.num
and l2.num = l3.num

# solution2: window function
with cte(num1, num2, num3)
as (
    select
    num,
    lead(num,1) over (order by id ) as num2,
    lead(num,2) over (order by id) as num3
    from logs
)
select
distinct num1 as ConsecutiveNums
from cte
where num1 = num2 and num2 = num3
