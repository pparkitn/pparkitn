# DataBricks Same Query
## Simple Select
```
%sql

select sum(num) dl, date
from table
where date > date_sub(current_date(), 10) 
group by date
```
