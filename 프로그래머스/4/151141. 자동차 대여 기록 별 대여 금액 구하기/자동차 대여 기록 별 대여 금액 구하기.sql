# SELECT HISTORY_ID, 
#     round(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1)
#     * (case 
#     when DATEDIFF(END_DATE, START_DATE)+1 < 7 then 1
#     when DATEDIFF(END_DATE, START_DATE)+1 < 30 then 0.95
#     when DATEDIFF(END_DATE, START_DATE)+1 < 90 then 0.92
#     else 0.85 end)) as "FEE"
# FROM (SELECT CAR_ID, DAILY_FEE
#       FROM CAR_RENTAL_COMPANY_CAR
#       WHERE CAR_TYPE = '트럭') as CC
#     JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH ON CC.CAR_ID = CH.CAR_ID
# ORDER BY FEE DESC, HISTORY_ID DESC


# with base as (
#     select c.CAR_ID, HISTORY_ID, DAILY_FEE, DATEDIFF(h.END_DATE, h.START_DATE)+1 as used_date,
#     CAST(REGEXP_REPLACE(DURATION_TYPE, '[^0-9]', '') AS UNSIGNED) as DURATION_TYPE
#     from CAR_RENTAL_COMPANY_CAR c
#         JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.CAR_ID = h.CAR_ID
#         JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on c.CAR_TYPE = p.CAR_TYPE
#     where c.CAR_TYPE = '트럭' and DURATION_TYPE < used_date
# )
# select HISTORY_ID, case 
#     when used_date < DURATION_TYPE THEN ROUND(DAILY_FEE * used_date)
#     when used_date < DURATION_TYPE THEN ROUND((DAILY_FEE * used_date) * 0.95)
#     when used_date < DURATION_TYPE THEN ROUND((DAILY_FEE * used_date) * 0.93)
#     else ROUND((DAILY_FEE * used_date) * 0.9) end as 'FEE'
# from base 
# order by FEE desc, HISTORY_ID desc

with plan as (
    select 
        CAR_TYPE
        , CAST(REGEXP_REPLACE(DURATION_TYPE, '[^0-9]', '') AS UNSIGNED) as DURATION_TYPE
        , DISCOUNT_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
),
base as (
    select c.CAR_ID
        , c. CAR_TYPE
        , HISTORY_ID
        , DAILY_FEE
        , DATEDIFF(h.END_DATE, h.START_DATE)+1 as USED_DATE
    from CAR_RENTAL_COMPANY_CAR c
        JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.CAR_ID = h.CAR_ID
),
temp as (
    select b.CAR_ID
        , b.HISTORY_ID
        , b.CAR_TYPE
        , DAILY_FEE
        , USED_DATE
        , DURATION_TYPE
        , DISCOUNT_RATE
        , ROW_NUMBER() over (partition by HISTORY_ID order by DURATION_TYPE desc) as RN
    from base b
        join plan p on b.CAR_TYPE = p.CAR_TYPE
        and DURATION_TYPE <= USED_DATE
)
select b.HISTORY_ID
    , FLOOR((b.DAILY_FEE * b.USED_DATE) * (1 - (IFNULL(t.DISCOUNT_RATE, 0) / 100))) AS FEE
from base b
    left join temp t on b.HISTORY_ID = t.HISTORY_ID and RN = 1
where b.CAR_TYPE = '트럭'
order by FEE desc, HISTORY_ID desc

