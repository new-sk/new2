import os
import sys
import platform
import sqlite3
import pandas as pd

class my95_stock:
    """
    SQLite DB에서 지정한 테이블을 읽어 엑셀로 저장하고,
    저장된 엑셀 파일을 다시 읽어 출력하는 기능을 제공하는 클래스.

    - DB 이름은 고정: 'my_stock.db'
    - 엑셀 파일 이름은 고정: 'my_stock_excel.xlsx'
    - OS에 따라 경로 설정:
        • Windows: D:\my_stock\
        • macOS : 파이썬 소스코드(.py)가 있는 디렉토리
    """

    def __init__(self, table_name='tb_blog_code'):
        """
        클래스 초기화: 운영체제에 따라 DB 및 엑셀 경로를 설정하고 테이블명을 저장함.

        Parameters:
            table_name (str): 사용할 SQLite 테이블 이름
        """
        self.table_name = table_name
        self.os_name = platform.system()
        self.conn = None
        self.db_name = 'my_stock.db'
        self.excel_name = 'my_stock_excel.xlsx'

        if self.os_name == 'Windows':
            base_dir = r'D:\my_stock'
        elif self.os_name == 'Darwin':  # macOS
            base_dir = os.path.dirname(os.path.abspath(__file__))
        else:
            print(f"[에러] 지원되지 않는 운영체제입니다: {self.os_name}")
            sys.exit(1)

        self.db_path = os.path.join(base_dir, self.db_name)
        self.excel_path = os.path.join(base_dir, self.excel_name)


    def connect_db(self):
        """
        SQLite DB에 연결, 연결 안되면 오류 출력 후 프로그램 종료.
        """
        if not os.path.isfile(self.db_path):
            print(f"[에러] DB 파일이 존재하지 않습니다: {self.db_path}")
            sys.exit(1)

        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()

    
    def save_table_to_excel(self, sheet_name=None):
        """
        지정된 SQLite 테이블을 엑셀 파일로 저장함.
        기존 엑셀 파일이 있다면 덮어쓰기 방식으로 저장됨.

        Parameters:
            sheet_name (str): 저장할 엑셀 시트명 (기본값: 테이블 이름과 동일)
        """
        if self.conn is None:
            print("[에러] DB 연결이 되어 있지 않습니다. connect_db() 먼저 호출하세요.")
            return

        if sheet_name is None:
            sheet_name = self.table_name

        df = pd.read_sql_query(f"SELECT * FROM {self.table_name}", self.conn)

        with pd.ExcelWriter(self.excel_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"[완료] '{self.table_name}' 테이블을 '{self.excel_path}'의 '{sheet_name}' 시트에 저장했습니다.")


    def read_excel(self, sheet_name=None):
        """
        엑셀 파일에서 지정한 시트를 읽고 상위 5개 행을 출력함.

        Parameters:
            sheet_name (str): 읽을 시트명 (기본값: 테이블 이름과 동일)
        """
        if not os.path.isfile(self.excel_path):
            print(f"[에러] 엑셀 파일이 존재하지 않습니다: {self.excel_path}")
            return

        if sheet_name is None:
            sheet_name = self.table_name

        try:
            df = pd.read_excel(self.excel_path, sheet_name=sheet_name, engine='openpyxl')
            print(f"\n[엑셀 읽기 결과 - '{sheet_name}' 시트 미리보기]")
            print(df.head())
        except Exception as e:
            print(f"[에러] 엑셀 파일 읽기 실패: {e}")




if __name__ == '__main__':
    stock = my95_stock(table_name='tb_blog_code')
    stock.connect_db()
    stock.save_table_to_excel()  # 자동으로 시트명은 'tb_blog_code'
    stock.read_excel()           # 동일하게 시트명은 'tb_blog_code'
