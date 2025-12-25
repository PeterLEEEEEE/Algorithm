-- 코드를 작성해주세요
with base as (
select RARITY, SUM(PRICE) as TOTAL_PRICE
from ITEM_INFO
group by RARITY
)
select TOTAL_PRICE
from base
where RARITY = 'LEGEND'