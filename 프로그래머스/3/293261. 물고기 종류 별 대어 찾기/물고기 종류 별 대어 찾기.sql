-- 코드를 작성해주세요
with base as (
    select ID, FISH_TYPE, LENGTH, 
        dense_rank() over(partition by FISH_TYPE order by LENGTH desc) as rn
    from FISH_INFO
)
select b.ID, i.FISH_NAME, b.LENGTH
from base b
    join FISH_NAME_INFO i on b.FISH_TYPE = i.FISH_TYPE
where rn = 1
order by ID
