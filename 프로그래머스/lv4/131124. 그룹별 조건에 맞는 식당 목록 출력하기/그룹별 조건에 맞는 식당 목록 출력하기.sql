-- 코드를 입력하세요
SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE P JOIN REST_REVIEW R ON R.MEMBER_ID = P.MEMBER_ID
WHERE R.MEMBER_ID IN (SELECT MEMBER_ID
                      FROM REST_REVIEW
                      GROUP BY MEMBER_ID
                      HAVING COUNT(MEMBER_ID) = (SELECT COUNT(REVIEW_TEXT) AS NUM
                                                 FROM REST_REVIEW
                                                 GROUP BY MEMBER_ID
                                                 ORDER BY NUM DESC
                                                 LIMIT 1))
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT
