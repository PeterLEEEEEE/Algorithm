-- 코드를 작성해주세요

with base as ( 
    select ID, FISH_TYPE, TIME, 
        CASE 
            WHEN LENGTH < 10 or LENGTH is null THEN 10
            else LENGTH 
        END as LENGTH
    from FISH_INFO
)
select COUNT(*) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE
from base
group by FISH_TYPE
having AVG(LENGTH) >= 33
order by FISH_TYPE 