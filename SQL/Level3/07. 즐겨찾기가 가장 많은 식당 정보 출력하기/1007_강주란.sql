WITH MAX_ID AS (SELECT FOOD_TYPE, MAX(FAVORITES)
                    FROM REST_INFO
                    GROUP BY FOOD_TYPE
)

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT *
                    FROM MAX_ID)
ORDER BY 1 DESC;


/*
SELECT REST_ID
FROM REST_INFO
GROUP BY FOOD_TYPE
HAVING MAX(FAVORITES)
이 쿼리는 FOOD_TYPE으로 그룹화한 후 MAX(FAVORITES)의 값이 있는 그룹을 필터링하는 것입니다.
하지만 SELECT절에서 REST_ID만을 선택했기 때문에,
MAX(FAVORITES)와 관련 없는 임의의 REST_ID가 결과로 나올 수 있습니다.
다시 말해, MAX(FAVORITES)가 어떤 레코드에 있는지 알 수 없으므로,
해당하는 식당의 ID를 가져오지 않습니다.
이로 인해 결과의 REST_ID가 우리가 의도한 최대 FAVORITES 값을 가진 식당과 일치하지 않게 됩니다.
*/