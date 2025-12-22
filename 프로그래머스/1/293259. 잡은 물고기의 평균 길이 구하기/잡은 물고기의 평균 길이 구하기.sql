-- 코드를 작성해주세요

with base as (
    select CASE WHEN LENGTH is NULL THEN 10 
        WHEN LENGTH is not NULL THEN LENGTH
        END as LENGTH
    from FISH_INFO 
)
select ROUND(AVG(LENGTH), 2) as AVERAGE_LENGTH
from base
