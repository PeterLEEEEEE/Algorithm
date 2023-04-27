-- 코드를 입력하세요
SELECT DISTINCT(CRCRH.CAR_ID)
FROM ( SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_CAR
        WHERE CAR_TYPE = '세단') CRCC 
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH ON CRCC.CAR_ID = CRCRH.CAR_ID
WHERE MONTH(START_DATE)=10
ORDER BY CRCRH.CAR_ID DESC
        
        
