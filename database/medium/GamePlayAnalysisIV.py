# Write your MySQL query statement below
with first_date(player_id, first_login)
as (
    select 
    player_id,
    min(event_date) as first_login
    from Activity
    group by player_id
),
cte1(cnt)
as (
    select 
    count(distinct f.player_id) as cnt
    from first_date as f
    left join Activity as A2
    on f.player_id = A2.player_id
    where date_sub(A2.event_date, interval 1 day) = f.first_login
),
cte2(total) 
as 
(
    select count(distinct player_id) as total
    from Activity
)
select round(cnt/total,2) as fraction
from cte2, cte1

