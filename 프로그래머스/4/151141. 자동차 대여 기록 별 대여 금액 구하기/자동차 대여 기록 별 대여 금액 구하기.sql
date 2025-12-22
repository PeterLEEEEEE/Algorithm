SELECT HISTORY_ID, 
    round(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1)
    * (case 
    when DATEDIFF(END_DATE, START_DATE)+1 < 7 then 1
    when DATEDIFF(END_DATE, START_DATE)+1 < 30 then 0.95
    when DATEDIFF(END_DATE, START_DATE)+1 < 90 then 0.92
    else 0.85 end)) as "FEE"
FROM (SELECT CAR_ID, DAILY_FEE
      FROM CAR_RENTAL_COMPANY_CAR
      WHERE CAR_TYPE = '트럭') as CC
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH ON CC.CAR_ID = CH.CAR_ID
ORDER BY FEE DESC, HISTORY_ID DESC


# with base as (
#     select c.CAR_ID, HISTORY_ID, DAILY_FEE, DATEDIFF(h.END_DATE, h.START_DATE)+1 as used_date
#     from CAR_RENTAL_COMPANY_CAR c
#         JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.CAR_ID = h.CAR_ID
#     where CAR_TYPE = '트럭'
# )
# select HISTORY_ID, case 
#     when used_date < 7 THEN ROUND(DAILY_FEE * used_date)
#     when used_date < 30 THEN ROUND((DAILY_FEE * used_date) * 0.95)
#     when used_date < 90 THEN ROUND((DAILY_FEE * used_date) * 0.93)
#     else ROUND((DAILY_FEE * used_date) * 0.9) end as 'FEE'
# from base 
# order by FEE desc, HISTORY_ID desc