-- 코드를 작성해주세요
with temp as (
    select YEAR(DIFFERENTIATION_DATE) as year, max(SIZE_OF_COLONY) as max_colo
    from ECOLI_DATA 
    group by YEAR(DIFFERENTIATION_DATE)
)
select t.year, ABS(SIZE_OF_COLONY - max_colo) as YEAR_DEV, ID
from ECOLI_DATA d
    LEFT JOIN temp t on YEAR(d.DIFFERENTIATION_DATE) = t.year
order by t.year asc, YEAR_DEV asc