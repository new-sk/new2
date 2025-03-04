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