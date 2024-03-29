SELECT NCC.CAR_ID, NCC.CAR_TYPE, 
round((NCC.DAILY_FEE * 30) / 100 * (100-DISCOUNT_RATE), 0) as FEE
FROM (SELECT *
     FROM CAR_RENTAL_COMPANY_CAR
     WHERE CAR_TYPE in ('SUV', '세단')
        AND DAILY_FEE * 30 BETWEEN 500000 AND 2000000
     ) as NCC
        JOIN 
            (SELECT CRCRH.CAR_ID, CRCRH.END_DATE
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH
            JOIN (SELECT MAX(END_DATE) as MAX_END_DATE
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                 GROUP BY CAR_ID
                 ) AS MH ON CRCRH.END_DATE = MH.MAX_END_DATE
            WHERE DATE_FORMAT(END_DATE, "%Y-%m-%d") < '2022-11-01'
            GROUP BY CAR_ID) as MMH
            ON NCC.CAR_ID = MMH.CAR_ID
        JOIN 
            (SELECT CAR_TYPE, DISCOUNT_RATE
            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            WHERE CAR_TYPE IN ('SUV', '세단')
                AND DURATION_TYPE = '30일 이상') 
            as CRCDP ON CRCDP.CAR_TYPE = NCC.CAR_TYPE
GROUP BY CAR_ID
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC



# SELECT CAR_TYPE, DISCOUNT_RATE
#             FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
#             WHERE CAR_TYPE IN ('SUV', '세단')
#                 AND DURATION_TYPE = '30일 이상'