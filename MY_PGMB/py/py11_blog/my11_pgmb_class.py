# BLOG 만들기
# MY11 : text file에서 sqlite를 활용하는 것으로 변경 (with dbeaver)
#      : my10 만든지 오래되어 어떻게 만들었는지 기억나지 않는다.

import subprocess
import os
import platform
import configparser 
import pandas as pd
import sys
from pathlib import Path  # OS별 패스 구분자 자동변환
import sqlite3

#sys.path.append("../py00_util")  # 상대경로로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../py00_util")))
from py00_utils import load_sql_query  # 새로운 버전 사용

class cMy11pgmB:
    
  def __init__(self):
    self.my_fini = 'my11_pgmb.ini'  # INI FileName
    self.my_fsql = 'my11_pgmb_query.sql' # SQL FileName
    self.my_dir  = ""               # 현재 디렉토리
    self.fcd_list  = []             # 파일명 List : 미활용
    self.fcm_list  = []             # 파일명 List : 미활용
    self.dflist = pd.DataFrame()    # DF, from Read group file
    self.dfgroup = pd.DataFrame()   # DF, from Read group file
    self.ggdir = ""
    self.ccdir = ""
    
    self.set_mode()
    # self.get_excel()

    self.read_group()


  ###
  ### INI 파일에서 기초 정보 읽어오기
  ### 1. 디렉토리 확인 : global 변수에 저장
  ### 2. INI파일 읽기 : my10에서만 사용 (어떤 파일 읽을지 결정)
  ###
  def set_mode(self):
    ### 1. 현재 디렉토리 읽기
    self.my_dir, my_file = os.path.split(__file__)

    ### 2. 설정파일 읽고 변수에 저장
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + self.my_fini)  # 설정 파일 읽기 (파일 위치)
    # 1번 설정값 읽기 : 코드 : 최초 문자열 -> List로 변경
    fcd_str = config.get('file', 'fcd')
    self.fcd_list = fcd_str.replace(' ', '').split(',')
    # 2번 설정값 읽기 : 매핑 : 최초 문자열 -> List로 변경
    fcm_str = config.get('file', 'fcm')
    self.fcm_list = fcm_str.replace(' ', '').split(',')


  ###
  ### 데이터 읽어서 향후 활용할 DF 변수에 저장
  ### 1. dflist 생성
  ### 2. dfgroup 생성
  ###   
  def read_group(self):
    ### 1. dfcd/dfcm에 데이터 입력

    # SQLite 데이터베이스 연결
    conn = sqlite3.connect(self.my_dir + '/' + "my_blog.db")
    
    self.dflist = pd.read_sql("""
select gKey, tbc1.Name gName, cKey, tbc2.Name cName, tbc2.cURL, seq
from tb_blog_map tbm, tb_blog_code tbc1, tb_blog_code tbc2
where tbm.gKey = tbc1."Key" and tbm.cKey = tbc2."Key"
order by tbc1.cdOrder, gKey, seq
""", conn)
    print(self.dflist)

    self.dfgroup = pd.read_sql("""
select distinct gKey, tbc.Name gName
from tb_blog_map tbm, tb_blog_code tbc
where tbm.gKey = tbc."Key" 
""", conn)
    print(self.dfgroup)
    conn.close()

    
  ###
  ### HTML Header 생성 : title 패러미터
  ###   
  def gen_title(self, title):
    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 뷰포트 설정 추가 -->
  <title>{title}</title>
  <link rel="stylesheet" href="../styles.css"> <!-- 외부 CSS 파일 연결 -->
</head>
<body>

  """


  ###
  ### HTML Tail 생성 
  ###   
  # file tail
  def gen_tail(self):
    return f"""
</body>
</html>
"""
  

  # generate file 
  def gen_gKey(self, dfKey):
    myhtml = self.gen_title(self.dfgroup.loc[self.dfgroup['gKey'] == dfKey, 'gName'].values[0])
    

    # 상수값 입력할 때 오류를 범하네 : GG, CG, CC 
    for n_row, row in self.dflist[self.dflist['gKey']==dfKey].iterrows():  # iterrows() 사용
      # print(row['gKey'], row['gName'], row['cKey'], row['cName'])
      if row['cKey'].startswith('GG'):
        myhtml += f"<p><a href=\"{self.ggdir}/{row['cKey']}.html\">{row['cName']}</a></p>\n"
      elif row['cKey'].startswith('CG'):
        myhtml += self.gen_detail_cg(row['cKey'],row['cName'])
      elif row['cKey'].startswith('CC'):
        # 외부 사이트
        if row['cURL'].startswith('http'):
          myhtml += f"<p><a href=\"{row['cURL']}\">{row['cName']}</a></p>\n"  
        # 내부 사이트
        else:
          myhtml += f"<p><a href=\"{self.ccdir}{row['cURL']}\">{row['cName']}</a></p>\n"  

    myhtml += self.gen_tail()
    return myhtml
  

  def gen_detail_cg(self, rck, rcm):
    mygc_html = f"<br><h4 id=\"{rck}\">{rcm}</h4>\n"
    for n_row, row in self.dflist[self.dflist['gKey']==rck].iterrows():  # iterrows() 사용
      if row['cKey'].startswith('GG'):
        if '#' in row['cKey']:
          file_part, anchor_part = row['cKey'].split('#', 1)
          mygc_html += f"<p><a href=\"{self.ggdir}/{file_part}.html#{anchor_part}\">{row['cName']}</a></p>\n"
        else:
          mygc_html += f"<p><a href=\"{self.ggdir}/{row['cKey']}.html\">{row['cName']}</a></p>\n"
      elif row['cKey'].startswith('CC'):
        mygc_html += f"<p><a href=\"{self.ccdir}{row['cURL']}\">{row['cName']}</a></p>\n"
      else:
        print('gen_detail_dc error : cKey')
    return mygc_html


  def gen_group(self): 
    # MAKE ROOT
    self.ggdir = "./pyhtml"
    self.ccdir = "."
    myhtml = self.gen_gKey('ROOT')
    print('print ROOT html')
    print(myhtml)
    # HTML file generate
    with open(self.my_dir + '/../../../index.html', "w", encoding="utf-8") as file:
      file.write(myhtml)

    # MAKE GG
    self.ggdir = "."
    self.ccdir = ".."
    for n_row, row in self.dfgroup[self.dfgroup['gKey'].str.startswith('GG')].iterrows():  # iterrows() 사용
      myhtml = self.gen_gKey(row['gKey'])
      print('print GG html : ' + row['gKey'])
      #print(myhtml)
      with open(self.my_dir + '/../../../pyhtml/' + row['gKey'] + '.html', "w", encoding="utf-8") as file:
        file.write(myhtml)


  def input_command(self):
    # 명령어 파심
    input_msg = """명령어를 입력해 주세요 (명령어(1글자) 내용) : \r
 - S : Search cName \r
 - O : Open File cURL \r
 - T : Find Tree \r
 - X : Exit
 """
    while 1==1:
      # input
      str_input = input(input_msg + "  : ")
      # 입력값에서 앞부분 1자리 문자와 나머지 문자열을 분리
      str_input = str_input.strip()  # 전체 입력 문자열의 양쪽 공백 제거

      if len(str_input) == 0:
        print("입력 문자열이 억습니다. 최소 2자리 이상의 문자열이어야 합니다.")
        continue

      # 첫 번째 토큰: 첫 한 글자 (이미 전체 공백이 제거된 상태)
      first_token = str_input[0].upper()
      if first_token == "X":
        sys.exit("정상 종료 ^^")
      elif len(str_input) < 2:
        print("입력 값이 너무 짧습니다. 최소 2자리 이상의 문자열이어야 합니다.")
        continue

      # 두 번째 토큰: 나머지 문자열 (이미 전체 공백이 제거된 상태)
      second_token = str_input[1:].strip()  # 두 번째 토큰 자체에만 남아 있는 공백을 다시 제거

      # 두 번째 토큰이 없을 경우 에러 처리
      if not second_token:
        print("두 번째 토큰이 존재하지 않습니다.")  
        continue
      elif first_token == "S":
        self.search_group(second_token)
      elif first_token == "O":
        self.open_file(second_token)
      elif first_token == "T":
        self.find_tree(second_token)
      else:
        print("명령어 시작 문자 오류")


  def open_file(self, ccName):
    print(f"Comming Soon : OPEN file {ccName}")

    ccName = ccName.strip()

    if ccName.startswith('CC'):
        # dflist에서 cKey가 input_values인 행을 찾음
        matching_row = self.dflist[self.dflist['cKey'] == ccName]
        print('matching_row : ', matching_row)
        if matching_row.empty:
            print(f"'{ccName}'에 해당하는 cKey가 없습니다.")
            return
        
        # cURL 값을 가져옴
        cURL = matching_row['cURL'].values[0]
        # file_name = self.my_dir + '/../../..' + cURL
        file_name = Path(self.my_dir).resolve().parents[2] / Path(cURL.lstrip('/'))

    elif ccName.startswith('GG'):
        print(f"Comming Soon : GG 파일 '{ccName}'을 읽습니다.")
        # file_name = self.my_dir + '/../../../pyhtml/' + ccName + '.html'
        file_name = Path(self.my_dir).resolve().parents[2] / "pyhtml" / f"{ccName}.html"

    else:
        print('not CC, not GG')
        return


    # 열고 싶은 파일의 경로
    

    # VSCode의 경로 설정 (기본적으로 설치된 경로를 사용할 수 있음)
    if platform.system() == "Windows":
      vscode_path = r'C:\Users\ICTUSER\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd'
    else:
      vscode_path = "/Applications/Visual Studio Code-2.app/Contents/Resources/app/bin/code"
    #'code'  # VSCode가 PATH에 추가되어 있으면 'code'만으로도 가능
    # 파일이 존재하는지 확인
    print (file_name)
    if os.path.isfile(file_name):
        # VSCode에서 파일 열기
        subprocess.run([vscode_path, file_name])
    else:
        print("파일을 찾을 수 없습니다.")


  # original search_group 
  def search_group(self, cName_value):
    # 입력 받기
    # cName_value = input("찾고자 하는 값을 입력하세요: ")
    # print("cName : " + cName_value)
    # DataFrame에서 cName 컬럼에 search_value가 포함된 DataFrame들만 필터링
    
    # 기존 cName에서만 찾음
    # print(self.dflist[self.dflist['cName'].str.contains(cName_value, case=False, na=False)])

    print(self.dflist[self.dflist[['cName', 'gName', 'gKey', 'cKey']].apply(lambda col: col.str.contains(cName_value, case=False, na=False)).any(axis=1)])


  def find_tree(self, ccName):

    # 데이터베이스 연결
    conn = sqlite3.connect(self.my_dir + '/' + "my_blog.db")
    cursor = conn.cursor()

    # 실행할 쿼리 선택
    query_name = "101.find_tree"  # 실행할 SQL 이름
    sql_query = load_sql_query(self.my_dir + '/' + self.my_fsql, query_name)

    print(ccName)

    if sql_query:
        cursor.execute(sql_query, (ccName,))
        results = cursor.fetchall()

        # 결과 출력
        for row in results:
            print(row)
    else:
        print(f"쿼리 '{query_name}'를 찾을 수 없습니다.")

    # 연결 종료
    conn.close()
