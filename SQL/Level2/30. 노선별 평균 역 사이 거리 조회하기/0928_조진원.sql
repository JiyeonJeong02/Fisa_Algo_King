-- 문자열 정렬이랑, 숫자의 정렬이랑 달라서 이 점을 유의할 것!!

SELECT 
    ROUTE,
    CONCAT(TOTAL_DISTANCE, 'km') AS TOTAL_DISTANCE,
    CONCAT(AVERAGE_DISTANCE, 'km') AS AVERAGE_DISTANCE
FROM
(SELECT 
    ROUTE, 
    ROUND(SUM(D_BETWEEN_DIST),1) AS TOTAL_DISTANCE, 
    ROUND(AVG(D_BETWEEN_DIST),2) AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY 2 DESC) SUB;