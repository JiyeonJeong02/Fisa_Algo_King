SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY ID;


/**트러블 슈팅
concat 과 in 내 , | 구분을 못했음
CONCAT() NULL이 하나라도 있으면 결과는 NULL
**/