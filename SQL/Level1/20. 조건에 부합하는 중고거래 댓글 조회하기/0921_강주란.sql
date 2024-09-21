
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS,
        DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
FROM USED_GOODS_BOARD b
INNER JOIN USED_GOODS_REPLY r
ON b.BOARD_ID = r.BOARD_ID
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY r.CREATED_DATE, b.TITLE;


/*참고
LEFT JOIN은 두 테이블 간의 연결을 하되,
왼쪽 테이블 (USED_GOODS_BOARD)의 모든 행을 유지하면서
오른쪽 테이블 (USED_GOODS_REPLY)의 데이터를 매칭시키는 방식입니다.
이때, 오른쪽 테이블에 BOARD_ID가 동일한 값이 여러 개 있으면,
해당 값들 각각에 대해 결과에 행이 추가됩니다.
즉, 중복된 값 중 하나만 출력되는 것이 아니라,
USED_GOODS_REPLY에서 동일한 BOARD_ID를 가진 모든 행들이 결과에 포함됩니다.

USED_GOODS_REPLY 테이블에 동일한 BOARD_ID를 가진 행이 여러 개 있다면,
INNER JOIN도 마찬가지로 각 중복된 행에 대해 결과가 여러 행으로 출력됩니다.
즉, 하나만 출력되는 것이 아니라, 모든 매칭되는 행이 출력됩니다.
*/
