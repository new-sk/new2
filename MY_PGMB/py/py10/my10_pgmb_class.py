# BLOG 만들기

import os
import configparser 
import pandas as pd
import sys

class cMy10pgmB:
    
  def __init__(self):
    self.my_dir = ""                # 현재 디렉토리
    self.my_fini = 'my10_pgmb.ini'  # INI FileName
    self.fcd_str  = ""             # 파일명 String
    self.fcd_list  = []              # 파일명 List
    self.fcm_str  = ""             # 파일명 String
    self.fcm_list  = []              # 파일명 List
    self.dfcd = pd.DataFrame()       # DF, from Read group file
    self.dfcm = pd.DataFrame()       # DF, from Read group file
    
    self.set_mode()
    # self.get_excel()

  def set_mode(self):
    # 현재 디렉토리 읽기
    self.my_dir, my_file = os.path.split(__file__)
    # 설정파일 읽고 변수에 저장
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + self.my_fini)  # 설정 파일 읽기 (파일 위치)
    # 1번 설정값 읽기 : 코드 : 최초 문자열 -> List로 변경
    self.fcd_str = config.get('file', 'fcd')
    self.fcd_list = self.fcd_str.replace(' ', '').split(',')
    # 2번 설정값 읽기 : 매핑 : 최초 문자열 -> List로 변경
    self.fcm_str = config.get('file', 'fcm')
    self.fcm_list = self.fcm_str.replace(' ', '').split(',')
    

  def read_group(self):
    # 코드 읽기
    for fcd in self.fcd_list:
      df = pd.read_csv(self.my_dir + '/' + fcd)
      # ignore_index=True면 인덱스를 새로 만드는 것이네
      self.dfcd = pd.concat([self.dfcd,df], ignore_index=True)
    # 매핑 읽기
    for fcm in self.fcm_list:
      # print(fcm)
      df = pd.read_csv(self.my_dir + '/' + fcm)
      # print(df)
      self.dfcm = pd.concat([self.dfcm,df], ignore_index=True)
      # print(self.dfcm)

    # dfcd 데이터 정합성 확인
    # "GG", "CG", "CC"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = self.dfcd[~(self.dfcd['Key'].str.startswith(('GG', 'CG', 'CC')) | (self.dfcd['Key'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("1.1 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, CC, ROOT)")
        print(invalid_keys['Key'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")
    # Key 값이 중복이면 멈춘다
    duplicated_keys = self.dfcd[self.dfcd.duplicated(subset='Key', keep=False)]        
    if not duplicated_keys.empty:
        # 중복된 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("1.2 중복된 Key 값이 발견되었습니다:")
        print(duplicated_keys['Key'].unique())
        sys.exit("중복된 Key 값으로 인해 프로그램이 종료되었습니다.")
  
    # dfcm 데이터 정합성 확인
    # gKey : "GG", "CG"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = self.dfcm[~(self.dfcm['gKey'].str.startswith(('GG', 'CG')) | (self.dfcm['gKey'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("2.1 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, ROOT)")
        print(invalid_keys['gKey'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")
    # cKey : "GG", "CG", "CC"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = self.dfcm[~(self.dfcm['cKey'].str.startswith(('GG', 'CG', 'CC')) | (self.dfcm['cKey'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("2.2 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, CC, ROOT)")
        print(invalid_keys['cKey'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")

    # dfcm 데이터 정합성 체크 2 : gKey & cKey
    # 둘 다 CG로 시작하는 경우
    both_cg_keys = self.dfcm[(self.dfcm['gKey'].str.startswith('CG')) & (self.dfcm['cKey'].str.startswith('CG'))]
    if not both_cg_keys.empty:
        # gKey와 cKey가 모두 "CG"로 시작하는 경우 종료
        print("3.1 gKey와 cKey가 모두 'CG'로 시작하는 행이 발견되었습니다:")
        print(both_cg_keys[['gKey', 'cKey']])
        sys.exit("gKey와 cKey가 모두 'CG'로 시작하는 행이 있어 프로그램이 종료되었습니다.")
    # 두 키가 모두 중복된 경우 확인
    duplicated_keys = self.dfcm[self.dfcm.duplicated(subset=['gKey', 'cKey'], keep=False)]
    if not duplicated_keys.empty:
        print("3.2 gKey와 cKey가 중복하는 행이 발견되었습니다:")
        print(duplicated_keys[['gKey', 'cKey']])
        sys.exit("gKey와 cKey가 중복되는 행이 있어 프로그램이 종료되었습니다.")

  # file header
  def gen_title(self, title):
    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body>

  """

  # file tail
  def gen_tail(self):
    return f"""
</body>
</html>
"""

  def gen_group(self): 
    # 향후 조인시 인덱스 유지를 위해서 보관
    self.dfcm['orgIndex'] = self.dfcm.index
    # gKey를 기준으로 dfcd와 조인하여 gName을 가져옴
    dflist = pd.merge(self.dfcm, self.dfcd, left_on='gKey', right_on='Key', how='left')
    dflist = dflist.rename(columns={'Name': 'gName'})  # gName으로 이름 변경
    dflist = dflist.drop(columns=['Key'])  # Key 컬럼 제거
    # cKey를 기준으로 다시 dfcd와 조인하여 cName을 가져옴
    dflist = pd.merge(dflist, self.dfcd, left_on='cKey', right_on='Key', how='left')
    dflist = dflist.rename(columns={'Name': 'cName'})  # cName으로 이름 변경
    dflist = dflist.drop(columns=['Key'])  # Key 컬럼 제거
    # 원래 인덱스를 기준으로 다시 정렬 (순서 유지)
    dflist = dflist.sort_values(by=['gKey','orgIndex']).reset_index(drop=True)
    print(dflist)
    '''# HTML header
    myhtml = self.gen_title("MY PGM HTML v3")

    # HTML original contencts
    # 임시로 만든 것임 : 아직 V3로 변환이 안되어서
    myhtml += "<p><a href=\"./MY_PGMB/pyhtml/index.html\">Study</a></p>\n"
    
    # HTML group contencts
    # DataFrame을 한 줄씩 읽어서 조건에 맞는 HTML 작성
    for n_row, row in self.dfgl.iterrows():  # iterrows() 사용
      if n_row == 0:
        myhtml += f"<br><h4>{row['ggName']}</h4>\n"
      elif row['ggKey'] != prev_ggKey:
        myhtml += f"<br><h4>{row['ggName']}</h4>\n"
      myhtml += f"<p><a href=\"./pyhtml/{row['gKey']}.html\">{row['gName']}</a></p>\n"
      prev_ggKey = row['ggKey']
    # HTML tail
    myhtml += self.gen_tail()
    # HTML file generate
    with open(self.my_dir + '/../../../index.html', "w", encoding="utf-8") as file:
      file.write(myhtml)
  '''