# BLOG 만들기

import os
import configparser 
import pandas as pd

class cMy10pgmB:
    
  def __init__(self):
    self.my_dir = ""                # 현재 디렉토리
    self.my_fini = 'my10_pgmb.ini'  # INI FileName
    self.my_fg  = ""                # Group FileName
    self.my_fgg = ""
    self.my_fgl = ""
    self.dfg = pd.DataFrame()       # DF, from Read group file
    self.dfgg = pd.DataFrame()       # DF, from Read group file
    self.dfgl = pd.DataFrame()       # DF, from Read group file
    

    self.set_mode()
    # self.get_excel()

  def set_mode(self):
    # 현재 디렉토리 읽기
    self.my_dir, my_file = os.path.split(__file__)
    # 설정파일 읽고 변수에 저장
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + self.my_fini)  # 설정 파일 읽기 (파일 위치)
    self.my_fg = config.get('file', 'fg')
    self.my_fgg = config.get('file', 'fgg')
    self.my_fgl = config.get('file', 'fgl')
    # print(self.my_fgl)

  def read_group(self):
    # print(self.my_dir + '/' + self.my_fgl)
    self.dfg = pd.read_csv(self.my_dir + '/' + self.my_fg)
    self.dfgg = pd.read_csv(self.my_dir + '/' + self.my_fgg)
    self.dfgl = pd.read_csv(self.my_dir + '/' + self.my_fgl)
    # print(dfgl)

    ggl_only = set(self.dfg['gKey']) - set(self.dfgl['gKey'])
    if ggl_only:
      print('ggl_Only : ', ggl_only)
    glg_only = set(self.dfgl['gKey']) - set(self.dfg['gKey'])
    if glg_only:
      print('glg_Only : ', glg_only)

    gggl_only = set(self.dfgg['ggKey']) - set(self.dfgl['ggKey'])
    if gggl_only:
      print('gggl_only', gggl_only)
    glgg_only = set(self.dfgl['ggKey']) - set(self.dfgg['ggKey'])
    if glgg_only:
      print('glgg_only', glgg_only)

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
    # HTML header
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
