# Write your MySQL query statement below
select 
request_at as "Day",
round(
    count(if (status in ('cancelled_by_driver','cancelled_by_client'), t.id, null))/
    count(t.id),2
) as "Cancellation Rate"
from Trips as T
left join Users as u1
on T.client_id = u1.users_id 
left join Users as u2
on T.driver_id = u2.users_id
where 
u1.banned = 'No' and u2.banned = 'No'
and request_at between '2013-10-01' and '2013-10-03'
group by request_at
