-- 코드를 작성해주세요

with temp as (
    select EMP_NO, ROUND(AVG(SCORE), 1) as SCORE,
        CASE WHEN ROUND(AVG(SCORE), 1) >= 96 THEN 'S'
            WHEN ROUND(AVG(SCORE), 1) >= 90 THEN 'A'
            WHEN ROUND(AVG(SCORE), 1) >= 80 THEN 'B'
            ELSE 'C' 
        END as GRADE
    from HR_GRADE
    group by EMP_NO
)
select e.EMP_NO, EMP_NAME, GRADE,
    CASE 
        WHEN GRADE = 'S' THEN SAL * 0.2 
        WHEN GRADE = 'A' THEN SAL * 0.15
        WHEN GRADE = 'B' THEN SAL * 0.1
        ELSE 0 
        END as BONUS
from HR_EMPLOYEES e
    join temp t on e.EMP_NO = t.EMP_NO
