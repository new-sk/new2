-- 101.find_tree

/* 잘못된 데이터인 경우 : 무한 루핑 가능 : depth 제한 필요 */
/*    원하는대로 모든 것이 나오지는 않는 듯 조정 필요 : GG35 : 중복된 값도 출력되고, 데이터 자체도 꼬여 있 */

WITH RECURSIVE 

/* 1️⃣ 특정 `some_value`가 gKey이든 cKey이든 먼저 찾기 */
start_nodes AS (
    SELECT tbm.gKey, tbm.cKey, tbc.Name 
    FROM tb_blog_map tbm, tb_blog_code tbc
    WHERE tbm.cKey = ? 
    and tbm.cKey= tbc."Key"
),

/* 2️⃣ 부모 방향 탐색 (위로 올라가기) */
parent_tree AS (
    SELECT gKey, cKey, Name, ROW_NUMBER() OVER () * 100 AS depth, gKey || ' > ' || cKey AS path
    FROM start_nodes

    UNION ALL

    SELECT tb.gKey, tb.cKey, tbc.Name, pt.depth - 1, tb.gKey || ' > ' || pt.path
    FROM tb_blog_map tb, tb_blog_code tbc
    INNER JOIN parent_tree pt ON tb.cKey = pt.gKey
        and tb.cKey= tbc."Key"
),

/* 3️⃣ 자식 방향 탐색 (아래로 내려가기) */
child_tree AS (
    SELECT gKey, cKey, Name, ROW_NUMBER() OVER () * 100 AS depth, gKey || ' > ' || cKey  AS path
    FROM start_nodes

    UNION ALL

    SELECT tb.gKey, tb.cKey, tbc.Name, ct.depth + 1, ct.path || ' > ' || tb.cKey
    FROM tb_blog_map tb, tb_blog_code tbc
    INNER JOIN child_tree ct ON tb.gKey = ct.cKey
        and tb.cKey= tbc."Key"
)

/* 4️⃣ 결과 정리 및 보기 좋게 출력 */
SELECT 
    gKey, 
    cKey, 
    depth,
    path,
    Name
FROM (
    SELECT * FROM parent_tree
    UNION
    SELECT * FROM child_tree
)
ORDER BY depth, path;
