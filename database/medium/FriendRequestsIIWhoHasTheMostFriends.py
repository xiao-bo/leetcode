# Write your MySQL query statement below
# using cte and join

with cte1 (id, cnt)
as (
    select accepter_id, count(accepter_id) as cnt
    from RequestAccepted
    group by accepter_id
),
cte2(id, cnt) 
as (
    select requester_id, count(requester_id) as cnt
    from RequestAccepted
    group by requester_id
),
cte3(id, num)
as (
select 
    cte1.id, 
    (ifnull(cte1.cnt,0) + ifnull(cte2.cnt,0)) as num
    from cte1 
    left join cte2
    on cte1.id = cte2.id
    union all
    select
    cte2.id, 
    (ifnull(cte1.cnt,0) + ifnull(cte2.cnt,0)) as num
    from cte1 
    right join cte2
    on cte1.id = cte2.id
)
select 
distinct id, num
from cte3
where num in
(select max(num) from cte3)

FriendRequestsIIWhoHasTheMostFriends
