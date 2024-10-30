# DataBricks Same Query
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
