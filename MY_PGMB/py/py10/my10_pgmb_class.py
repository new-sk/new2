# BLOG 만들기

import os
import configparser 
import pandas as pd
import sys

class cMy10pgmB:
    
  def __init__(self):
    self.my_dir = ""                # 현재 디렉토리
    self.my_fini = 'my10_pgmb.ini'  # INI FileName
    self.fcd_list  = []              # 파일명 List
    self.fcm_list  = []              # 파일명 List
    self.dflist = pd.DataFrame()       # DF, from Read group file
    self.dfgroup = pd.DataFrame()       # DF, from Read group file
    self.ggdir = ""
    self.ccdir = ""
    
    self.set_mode()
    # self.get_excel()

    self.read_group()

  def set_mode(self):
    # 현재 디렉토리 읽기
    self.my_dir, my_file = os.path.split(__file__)
    # 설정파일 읽고 변수에 저장
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + self.my_fini)  # 설정 파일 읽기 (파일 위치)
    # 1번 설정값 읽기 : 코드 : 최초 문자열 -> List로 변경
    fcd_str = config.get('file', 'fcd')
    self.fcd_list = fcd_str.replace(' ', '').split(',')
    # 2번 설정값 읽기 : 매핑 : 최초 문자열 -> List로 변경
    fcm_str = config.get('file', 'fcm')
    self.fcm_list = fcm_str.replace(' ', '').split(',')
    
  def read_group(self):
    # 로컬변수 초기화
    dfcd = pd.DataFrame()
    dfcm = pd.DataFrame()

    # 코드 읽기
    for fcd in self.fcd_list:
      df = pd.read_csv(self.my_dir + '/' + fcd)
      # ignore_index=True면 인덱스를 새로 만드는 것이네
      dfcd = pd.concat([dfcd,df], ignore_index=True)
    # 매핑 읽기
    for fcm in self.fcm_list:
      # print(fcm)
      df = pd.read_csv(self.my_dir + '/' + fcm)
      # print(df)
      dfcm = pd.concat([dfcm,df], ignore_index=True)
      # print(dfcm)

    # dfcd 데이터 정합성 확인
    # "GG", "CG", "CC"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = dfcd[~(dfcd['Key'].str.startswith(('GG', 'CG', 'CC')) | (dfcd['Key'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("1.1 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, CC, ROOT)")
        print(invalid_keys['Key'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")
    # Key 값이 중복이면 멈춘다
    duplicated_keys = dfcd[dfcd.duplicated(subset='Key', keep=False)]        
    if not duplicated_keys.empty:
        # 중복된 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("1.2 중복된 Key 값이 발견되었습니다:")
        print(duplicated_keys['Key'].unique())
        sys.exit("중복된 Key 값으로 인해 프로그램이 종료되었습니다.")
  
    # dfcm 데이터 정합성 확인
    # gKey : "GG", "CG"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = dfcm[~(dfcm['gKey'].str.startswith(('GG', 'CG')) | (dfcm['gKey'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("2.1 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, ROOT)")
        print(invalid_keys['gKey'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")
    # cKey : "GG", "CG", "CC"로 시작하거나 "ROOT"가 아닌 것이 존재하면 멈춘다
    invalid_keys = dfcm[~(dfcm['cKey'].str.startswith(('GG', 'CG', 'CC')) | (dfcm['cKey'] == 'ROOT'))]
    if not invalid_keys.empty:
        # 조건에 맞지 않는 값이 있을 경우 해당 키값 출력 후 프로그램 종료
        print("2.2 조건에 맞지 않는 Key 값이 발견되었습니다: (GG, CG, CC, ROOT)")
        print(invalid_keys['cKey'].unique())
        sys.exit("잘못된 Key 값으로 인해 프로그램이 종료되었습니다.")

    # dfcm 데이터 정합성 체크 2 : gKey & cKey
    # 둘 다 CG로 시작하는 경우
    both_cg_keys = dfcm[(dfcm['gKey'].str.startswith('CG')) & (dfcm['cKey'].str.startswith('CG'))]
    if not both_cg_keys.empty:
        # gKey와 cKey가 모두 "CG"로 시작하는 경우 종료
        print("3.1 gKey와 cKey가 모두 'CG'로 시작하는 행이 발견되었습니다:")
        print(both_cg_keys[['gKey', 'cKey']])
        sys.exit("gKey와 cKey가 모두 'CG'로 시작하는 행이 있어 프로그램이 종료되었습니다.")
    # 두 키가 모두 중복된 경우 확인
    duplicated_keys = dfcm[dfcm.duplicated(subset=['gKey', 'cKey'], keep=False)]
    if not duplicated_keys.empty:
        print("3.2 gKey와 cKey가 중복하는 행이 발견되었습니다:")
        print(duplicated_keys[['gKey', 'cKey']])
        sys.exit("gKey와 cKey가 중복되는 행이 있어 프로그램이 종료되었습니다.")

    # 매핑내역에서 사용되지 않는 항목 찾기 (gKey)
    dfcd_group = dfcd[dfcd['Key'].str.startswith(('GG', 'CG')) | (dfcd['Key'] == 'ROOT')]
    # 4.1 : gKey : in dfcd and not in dfcm
    dfcd_only = dfcd_group[~dfcd_group['Key'].isin(dfcm['gKey'])]
    if not dfcd_only.empty:
      print(f"4.1 dfcd에만 존재하고 매핑에는 존재하지 않는 gKey 값(GG,CG): {dfcd_only}")
      sys.exit()
    # 4.2 : gKey : in dfcm and not in dfcd
    dfcm_only = dfcm[~dfcm['gKey'].isin(dfcd['Key'])]
    if not dfcm_only.empty:
      print(f"4.2 dfcm에만 존재하고 코드에는 존재하지 않는 gKey 값(GG,CG): {dfcm_only}")
      sys.exit()
    # 매핑내역에서 사용되지 않는 항목 찾기 (cKey)
    dfcd_contents = dfcd[dfcd['Key'].str.startswith(('CG', 'CC'))]
    # 4.3 : cKey : in dfcd and not in dfcm
    dfcd_only = dfcd_contents[~dfcd_contents['Key'].isin(dfcm['cKey'])]
    if not dfcd_only.empty:
      print(f"4.3 dfcd에만 존재하고 매핑에는 존재하지 않는 cKey 값(CG,CC): {dfcd_only}")
      sys.exit()
    # 4.4 : cKey : in dfcm and not in dfcd
    dfcm_only = dfcm[~dfcm['cKey'].isin(dfcd['Key'])]
    if not dfcm_only.empty:
      print(f"4.4 dfcm에만 존재하고 코드에는 존재하지 않는 cKey 값(CG,CC): {dfcm_only}")
      sys.exit()

    # MAKE self.dflist
    # 향후 조인시 인덱스 유지를 위해서 보관
    dfcm['orgIndex'] = dfcm.index
    # gKey를 기준으로 dfcd와 조인하여 gName을 가져옴
    self.dflist = pd.merge(dfcm, dfcd[['Key','Name']], left_on='gKey', right_on='Key', how='left')
    self.dflist = self.dflist.rename(columns={'Name': 'gName'})  # gName으로 이름 변경
    self.dflist = self.dflist.drop(columns=['Key'])  # Key 컬럼 제거
    # cKey를 기준으로 다시 dfcd와 조인하여 cName을 가져옴
    self.dflist = pd.merge(self.dflist, dfcd, left_on='cKey', right_on='Key', how='left')
    self.dflist = self.dflist.rename(columns={'Name': 'cName'})  # cName으로 이름 변경
    self.dflist = self.dflist.drop(columns=['Key'])  # Key 컬럼 제거
    # 원래 인덱스를 기준으로 다시 정렬 (순서 유지)
    self.dflist = self.dflist.sort_values(by=['gKey','orgIndex']).reset_index(drop=True)
    print("print dflist")   
    print(self.dflist)

    # MAKE dfgroup 
    #self.dfgroup = self.dflist[self.dflist['gKey'].str.startswith('GG')][['gKey', 'gName']].drop_duplicates()
    self.dfgroup = self.dflist[['gKey', 'gName']].drop_duplicates()

    print("print dfgroup")   
    print(self.dfgroup)

    
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
  

  # generate file 
  def gen_gKey(self, dfKey):
    myhtml = self.gen_title(self.dfgroup[self.dfgroup['gKey']==dfKey]['gName'].values[0])
    
    # 상수값 입력할 때 오류를 범하네 : GG, CG, CC 
    for n_row, row in self.dflist[self.dflist['gKey']==dfKey].iterrows():  # iterrows() 사용
      if row['cKey'].startswith('GG'):
        myhtml += f"<p><a href=\"{self.ggdir}/{row['cKey']}.html\">{row['cName']}</a></p>\n"
      elif row['cKey'].startswith('CG'):
        myhtml += self.gen_detail_gc(row['cKey'],row['cName'])
      elif row['cKey'].startswith('CC'):
        # 외부 사이트
        if row['cURL'].startswith('http'):
          myhtml += f"<p><a href=\"{row['cURL']}\">{row['cName']}</a></p>\n"  
        # 내부 사이트
        else:
          myhtml += f"<p><a href=\"{self.ccdir}{row['cURL']}\">{row['cName']}</a></p>\n"  

    myhtml += self.gen_tail()
    return myhtml
  

  def gen_detail_gc(self, rck,rcm):
    mygc_html = f"<br><h4>{rcm}</h4>\n"
    for n_row, row in self.dflist[self.dflist['gKey']==rck].iterrows():  # iterrows() 사용
      if row['cKey'].startswith('GG'):
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
      print(myhtml)
      with open(self.my_dir + '/../../../pyhtml/' + row['gKey'] + '.html', "w", encoding="utf-8") as file:
        file.write(myhtml)
