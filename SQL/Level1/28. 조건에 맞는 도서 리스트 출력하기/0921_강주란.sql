SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021
AND CATEGORY = '인문'
ORDER BY 2;

/*MySQL에서는 YEAR() 함수가 날짜에서 연도를 추출하고,
그 결과는 숫자 데이터 타입으로 반환
YEAR(PUBLISHED_DATE) = '2021'처럼 문자열로 비교하는 경우에도
MySQL이 자동으로 형 변환을 해주긴함
*/