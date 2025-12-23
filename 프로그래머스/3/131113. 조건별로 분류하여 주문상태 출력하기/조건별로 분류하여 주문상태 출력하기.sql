-- 코드를 입력하세요
# SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d'),
#     (CASE 
#         WHEN DATE_FORMAT(OUT_DATE, '%m-%d') > '05-01' THEN '출고대기' 
#         WHEN DATE_FORMAT(OUT_DATE, '%m-%d') <= '05-01' THEN '출고완료'
#         ELSE '출고미정'
#         END) as '출고여부'
# FROM FOOD_ORDER


select ORDER_ID
    , PRODUCT_ID
    , DATE_FORMAT(OUT_DATE, '%Y-%m-%d')
    , CASE 
        WHEN DATE_FORMAT(OUT_DATE, '%m-%d') > '05-01' THEN '출고대기' 
        WHEN DATE_FORMAT(OUT_DATE, '%m-%d') <= '05-01' THEN '출고완료'
        ELSE '출고미정'
      END as '출고여부'
from FOOD_ORDER
