# 클래스 변수 초기화
max_loop = 3                        # Test Mode인 경우 3페이지만 가져옴
my_dir = ""                         # os
my_xfile = '/my9_stock_sData.xlsx'  # excel file
my_xfile_sname = 'sData'            # excel file sheet name

import json
from urllib import parse
from collections import OrderedDict
import sys
import configparser  # 24.07.28 추가 : INI 설정

from my9_stock_naver import *

### 1. set mode
# 1.1 INI파일에서 mode 설정
my_dir, my_file = os.path.split(__file__)
my_os = os.name

# WOW : 설정 파일 만들고 읽기
config_file = my_file.rsplit('.', 1)[0] + '.ini'
config = configparser.ConfigParser()  # 객체 생성
config.read(my_dir + '/' + config_file)  # 설정 파일 읽기 (파일 위치)
sMode = config.get('mode', 'smode')

# 1.3.1 Test 모드 (2페이지만 가져오기)
if sMode == "Test":
  max_loop = 3  # 2페이지만 가져오기 (1,2)

# 1.3.2 Real 모드 (전체 가져오기)
elif sMode == "Real":
  max_loop = 0  # 전체 가져오기
  if my_os == "nt":
    my_dir = 'D:\MY_BLOG_LOCAL_HOME\py'
  else:  # NT가 아니면 종료
    print("여기서는 Real Mode가 안됩니다.")
    exit()

# 1.3.3 모드 이상 : 그냥 종료
else:
  print("sMode 이상")
  exit()



#''' 테스트 영역
# 엑셀 파일에서 읽기 (테스트중)
# 엑셀 파일 경로
# my_xfile = '/my9_stock_sData.xlsx'
# my_xfile_sname = 'sData'

# WOW : 엑셀 읽기 : 
#     : 파일명, 시트명(sheet_name)
#     : 열명(usecols) : 컬럼영문알파벳, 인덱스(숫자0부터), 컬럼명  : 'A:E', range(0,4), ['saAccount','saName'] 
# WOW : 데이터타입(dtype) 숫자로 지정해도 엑셀에 저장된 값이 float이면 intger로 변환되지 않는다고 함 : 음... 엑셀에서 int로 변환한것도 float로 저장되는데, 
df = pd.read_excel(my_dir + my_xfile, sheet_name=my_xfile_sname, usecols='A:E', na_values=["N/A", "NA", "-", "", "none"])
df = df.dropna()
print(df)

for sName in df['spName']:
  startN = df.loc[df['spName'] == sName, 'spStart'].iloc[0].astype('int32')
  endN   = df.loc[df['spName'] == sName, 'spEnd'].iloc[0].astype('int32')
  print(startN, ' : ', endN)
  dfx = pd.read_excel(my_dir + my_xfile, sheet_name=my_xfile_sname, usecols=range(startN-1, startN+endN-1), header=2, na_values=["N/A", "NA", "-", "", "none"])
  # WOW : 모든 값이 na인 경우에만 행을 삭제하도록 개선
  # dfx = dfx.dropna()
  all_na_rows = dfx.isna().all(axis=1) # 모든 값이 NaN인 행을 식별
  dfx = dfx[~all_na_rows]  # 모든 값이 NaN인 행만 제거
  print(dfx)
  # WOW : global 변수 이름에 해당 데이터 저장 : sName에 저장된 값으로 변수를 만들어서 저장
  globals()[sName] = dfx




for sCode in dfi['siCode']:
  # 파일 존재 여부 확인
  my_filename = my_dir + '/my9_stock_out_' + sCode + '.txt' 
  if os.path.exists(my_filename):
    get_one(sCode)
    print(sCode + " : 파일이 존재합니다.")
  else:
    get_all(sCode, 'FILE')   
    print(sCode + " : 파일을 새로 만들었습니다")


### 3 : 특정 날짜 데이터 취합하기 
# df = pd.read_csv(my_dir + my_sfile, dtype={'sCode': str})

dfall = pd.DataFrame() # 초기화

for sCode in dfi['siCode']:
  # 종목명 정보 읽어오기
  my9_fname = '/my9_stock_out_' + sCode + '.txt'
  dfs = pd.read_csv(my_dir + my9_fname, dtype={'sCode': str})
  # 특정 날짜 정보만 취합하기
  dfs = dfs[dfs['Date'].isin(['2024.09.06'])]
  dfall = pd.concat([dfall, dfs], ignore_index=True)

# 취합정보 출력
print(dfall)
dfall.to_csv(my_dir + '/my9_stock_out_all.txt', index=False)
#'''