# Write your MySQL query statement below

select 
 c1.visited_on, sum(c1.amount) as amount,round(sum(c1.amount)/7  , 2) as average_amount
from
  (select visited_on, sum(amount) as amount from customer group by visited_on) c1,
   (select visited_on, sum(amount) as amount from customer group by visited_on) c2
where c2.visited_on between Date_sub(c1.visited_on , Interval 6 day) and c1.visited_on 
group by c2.visited_on
having count(*)=7
order by c2.visited_on
