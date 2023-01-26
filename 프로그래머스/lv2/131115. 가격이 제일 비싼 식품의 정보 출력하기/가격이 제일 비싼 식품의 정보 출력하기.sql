-- 코드를 입력하세요
-- 내가 푼 풀이
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;

-- 레퍼런스
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE =
  (SELECT MAX(PRICE) FROM FOOD_PRODUCT)
