-- 코드를 입력하세요
SELECT DATE_FORMAT(DATETIME, '%H') HOUR, COUNT(ANIMAL_ID) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR > 8 AND HOUR <= 19
ORDER BY HOUR