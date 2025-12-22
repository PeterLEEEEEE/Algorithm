-- 코드를 작성해주세요
select COUNT(ID) as FISH_COUNT
from FISH_INFO
where LENGTH <= 10.0 or LENGTH is null