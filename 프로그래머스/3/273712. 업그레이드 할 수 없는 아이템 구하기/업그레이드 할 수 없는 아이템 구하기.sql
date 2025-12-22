-- 코드를 작성해주세요

select i.ITEM_ID, i.ITEM_NAME, RARITY
from ITEM_INFO i
    JOIN ITEM_TREE it on i.ITEM_ID = it.ITEM_ID
where i.ITEM_ID not in (select DISTINCT PARENT_ITEM_ID
    from ITEM_TREE where PARENT_ITEM_ID is not null)
order by i.ITEM_ID desc



# select DISTINCT PARENT_ITEM_ID
#     from ITEM_TREE
    