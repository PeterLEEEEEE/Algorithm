-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) as TOTAL_SALES
FROM (
    SELECT * 
    FROM BOOK_SALES 
    WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = '2022-01') as BS
    JOIN BOOK B ON BS.BOOK_ID = B.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY ASC