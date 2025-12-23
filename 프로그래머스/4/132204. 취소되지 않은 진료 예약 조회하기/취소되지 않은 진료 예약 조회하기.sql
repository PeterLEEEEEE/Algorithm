-- 코드를 입력하세요
# SELECT AP.APNT_NO, PT.PT_NAME, PT.PT_NO, DR.MCDP_CD, DR.DR_NAME, AP.APNT_YMD
# FROM (SELECT *
#       FROM APPOINTMENT 
#       WHERE DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13' 
#         and MCDP_CD = 'CS' 
#         and APNT_CNCL_YN = 'N') as AP
#     JOIN DOCTOR DR ON AP.MDDR_ID = DR.DR_ID
#     JOIN PATIENT PT ON AP.PT_NO = PT.PT_NO
# ORDER BY APNT_YMD ASC

with ap as (
    select APNT_NO, PT_NO, MDDR_ID, APNT_YMD
    from APPOINTMENT
    where APNT_CNCL_YN = 'N' and DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
)
select a.APNT_NO, t.PT_NAME, t.PT_NO, d.MCDP_CD, d.DR_NAME, APNT_YMD
from ap a 
    join DOCTOR d on a.MDDR_ID = d.DR_ID
    and d.MCDP_CD = 'CS'
    join PATIENT t on a.PT_NO = t.PT_NO
order by APNT_YMD 