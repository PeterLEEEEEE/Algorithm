SELECT MEMBER_NAME, REVIEW_TEXT, 
    DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM REST_REVIEW r 
    JOIN MEMBER_PROFILE m ON r.MEMBER_ID = m.MEMBER_ID
WHERE r.MEMBER_ID in (SELECT MEMBER_ID
                  FROM REST_REVIEW
                  GROUP BY MEMBER_ID
                  HAVING COUNT(*) = (SELECT MAX(cnt)
                                     FROM (SELECT COUNT(MEMBER_ID) as cnt, MEMBER_ID
                                           FROM REST_REVIEW 
                                           GROUP BY MEMBER_ID) as r))
ORDER BY REVIEW_DATE, REVIEW_TEXT


