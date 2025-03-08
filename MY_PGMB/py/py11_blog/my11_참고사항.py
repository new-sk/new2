'''
    파일 my10_input_map_root.txt에서 데이터프레임을 읽을꺼야
    데이터프레임에는 gKey, cKey 컬럼만 있어
    이 내역을 sqlite db에 tb_blog_map에 입력할꺼야.
    테이블에는 컬럼이 3개야.
    gKey와 cKey 외에 seq라는 컬럼이 있어.
    seq는 데이터프레임의 row number를 넣어줘
    파이썬 코드로 만들어줘
'''

import pandas as pd
import sqlite3
import os

my_dir, my_file = os.path.split(__file__)

print(my_dir)
# 파일에서 데이터 읽기
df = pd.read_csv(my_dir + '/' + "my10_input_map_root.txt", usecols=["gKey", "cKey"])

# seq 컬럼 추가
df["seq"] = range(1, len(df) + 1)

# SQLite 데이터베이스 연결
conn = sqlite3.connect(my_dir + '/' + "my_blog.db")  # 적절한 DB 이름 지정
cursor = conn.cursor()

# 테이블 생성 (한 번만 실행)
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_blog_map (
    gKey TEXT,
    cKey TEXT,
    seq integer,
    PRIMARY KEY (gKey, cKey)
)
""")

# 데이터 삽입
df.to_sql("tb_blog_map", conn, if_exists="append", index=False)

# 변경 사항 저장 및 연결 종료
conn.commit()
conn.close()

print("데이터 삽입 완료!")


'''
    ### code 값들을 읽어서 테이블로 저장하는 것
    def read_group(self):
        # 로컬변수 초기화
        dfcd = pd.DataFrame()
        dfcm = pd.DataFrame()

        # 코드 읽기 (dfcd)
        df1 = pd.read_csv(self.my_dir + '/' + self.fcd_list[0])
        df2 = pd.read_csv(self.my_dir + '/' + self.fcd_list[1])
        
        # 2️⃣ 병합 (Key 기준, Name 하나만 유지)
        merged_df = pd.merge(df1, df2, on='Key', how='outer', suffixes=('_df1', '_df2'))

        # 3️⃣ 최종 Name 선택
        merged_df['Name'] = merged_df['Name_df1'].fillna(merged_df['Name_df2'])

        # 4️⃣ 필요 없는 컬럼 정리
        merged_df = merged_df[['Key', 'Name', 'cURL']]  # 'URL'이 없으면 NaN → 자동 처리됨

        # 5️⃣ NaN 값 처리 (URL은 빈 문자열로)
        merged_df['cURL'] = merged_df['cURL'].fillna("")

        # 4️⃣ SQLite 데이터베이스 연결
        conn = sqlite3.connect(self.my_dir + '/' + "my_blog.db")
        cursor = conn.cursor() 

        # 5️⃣ 테이블 생성 (한 번만 실행)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_blog_code (
            Key TEXT PRIMARY KEY,
            Name TEXT,
            cURL TEXT
        )
        """)
    
        # 6️⃣ SQLite에 데이터 저장
        merged_df.to_sql("tb_blog_code", conn, if_exists="replace", index=False)
    
        print("📢 데이터 저장 완료후 SELECT!") 
        
        dfcd = pd.read_sql("SELECT * FROM tb_blog_code ", conn) 
        
        # 출력
        print(dfcd)

        # 7️⃣ 연결 종료
        conn.close()

        return
'''