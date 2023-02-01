-- 코드를 입력하세요
# SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
# FROM MEMBER_PROFILE P INNER JOIN REST_REVIEW R ON R.MEMBER_ID = P.MEMBER_ID
# WHERE R.MEMBER_ID IN (SELECT MEMBER_ID
#                       FROM REST_REVIEW R
#                       GROUP BY MEMBER_ID
#                       HAVING COUNT(*) = (SELECT MAX(COUNT(*))
#                                          FROM REST_REVIEW
#                                          GROUP BY MEMBER_ID))
# ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT

SELECT A.MEMBER_NAME, B.REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE A JOIN REST_REVIEW B
ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING COUNT(member_id) = (SELECT COUNT(REVIEW_TEXT) AS 'NUM'
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                                ORDER BY NUM DESC
                                LIMIT 1))
ORDER BY B.REVIEW_DATE, B.REVIEW_TEXT