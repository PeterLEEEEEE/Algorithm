-- 코드를 작성해주세요

with base as (
    select LOCATION2, YEAR(YM) as YEAR, ROUND(AVG(PM_VAL1), 2) as 'PM10', ROUND(AVG(PM_VAL2), 2) as 'PM2.5'
    from AIR_POLLUTION 
    GROUP BY LOCATION2, YEAR(YM)
)
select YEAR, `PM10`, `PM2.5`
from base
where LOCATION2 = '수원'
order by YEAR asc