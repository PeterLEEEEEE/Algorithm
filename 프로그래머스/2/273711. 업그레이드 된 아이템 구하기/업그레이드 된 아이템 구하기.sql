-- 코드를 작성해주세요
WITH rare_items AS (
    SELECT ITEM_ID
    FROM ITEM_INFO
    WHERE RARITY = 'RARE'
)
SELECT
    it.ITEM_ID,
    ii.ITEM_NAME,
    ii.RARITY
FROM
    ITEM_INFO AS ii
    INNER JOIN ITEM_TREE AS it
        ON ii.ITEM_ID = it.ITEM_ID
    INNER JOIN rare_items AS ri
        ON it.PARENT_ITEM_ID = ri.ITEM_ID
ORDER BY
    it.ITEM_ID DESC