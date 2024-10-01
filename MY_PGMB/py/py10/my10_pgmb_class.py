# BLOG 만들기

import os
import configparser 
import pandas as pd

class cMy10pgmB:
    
  def __init__(self):
    self.my_dir = ""                # 현재 디렉토리
    self.my_fini = 'my10_pgmb.ini'  # INI File
    self.my_fg  = ""
    self.my_fgg = ""
    self.my_fgl = ""

    self.set_mode()
    # self.get_excel()

  def set_mode(self):
    self.my_dir, my_file = os.path.split(__file__)

    # WOW : 설정 파일 만들고 읽기
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + self.my_fini)  # 설정 파일 읽기 (파일 위치)
    self.my_fg = config.get('file', 'fg')
    self.my_fgg = config.get('file', 'fgg')
    self.my_fgl = config.get('file', 'fgl')

    print(self.my_fgl)

  def read_group(self):
    print(self.my_dir + '/' + self.my_fgl)
    dfg = pd.read_csv(self.my_dir + '/' + self.my_fg)
    print(dfg)
    dfgg = pd.read_csv(self.my_dir + '/' + self.my_fgg)
    print(dfgg)
    dfgl = pd.read_csv(self.my_dir + '/' + self.my_fgl)
    print(dfgl)
    
