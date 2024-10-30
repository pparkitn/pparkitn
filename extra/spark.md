# DataBricks 
## Simple Select
```
%sql

select sum(num) dl, date
from table
where date > date_sub(current_date(), 10) 
group by date
```
## Simple Select into Spark Table
```
spark_df = spark.sql(
    f""" 
select sum(num) dl, date
from table
where date > date_sub(current_date(), 10) 
group by date
    """
)

spark_df.show()

```
### Select Into Another Table
```
%sql
drop view if exists temp_view;
CREATE OR REPLACE TEMPORARY VIEW temp_view AS 
SELECT 
  *
FROM table
where country = 'CA'
```
```
%sql
select * from temp_view limit 100
```
