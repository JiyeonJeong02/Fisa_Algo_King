-- 코드를 작성해주세요
-- 부모의 형질을 모두 보유한 대장균, 부모 대장균

SELECT child.ID ID
        , child.GENOTYPE
        , parent.GENOTYPE PARENT_GENOTYPE
FROM ECOLI_DATA child
JOIN ECOLI_DATA parent
ON child.PARENT_ID = parent.ID
WHERE 
ORDER BY 1;child.GENOTYPE & parent.GENOTYPE = parent.GENOTYPE



/*테케 1개 못맞춘 코드*/
SELECT child.ID ID
        , child.GENOTYPE
        , parent.GENOTYPE PARENT_GENOTYPE
FROM ECOLI_DATA child
JOIN ECOLI_DATA parent
ON child.PARENT_ID = parent.ID
WHERE (CONV(child.GENOTYPE, 10, 2) - CONV(parent.GENOTYPE, 10, 2)) NOT LIKE '%9%'
ORDER BY 1;