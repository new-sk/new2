#import platform
#my_os = platform.system()


# fig : 입력파일 : 데이터파일(group)
#     : input_group.txt : {#1 : KEY, #2 : Order, #3 : NAME}
#     : KEY == 0 그룹핑을 위한 단순 텍스트
# fi_index : 입력파일 : 기본 HTML 파일구조 가짐

import os
my_dir, my_file = os.path.split(__file__)


import pandas as pd

# CSV 파일을 읽어서 데이터프레임에 저장
df = pd.read_csv(my_dir + '/input_group.txt',    dtype={'Key' : str})
dc = pd.read_csv(my_dir + '/input_contents.txt', dtype={'gKey': str})

# 컬럼 Order에서 중복된 값이 있는지 여부 확인 (group)
has_duplicates = df['Order'].duplicated().any()

df = df.sort_values(by='Order')
if has_duplicates:
  print("중복 O")
  df['Order'] = df.index * 10
  df.to_csv(my_dir + '/input_group2.txt', index=False)
else:
  print("중복 X")

# 컬럼 Order에서 중복된 값이 있는지 여부 확인 (Contents)
has_duplicates = dc['Order'].duplicated().any()

dc = dc.sort_values(by=['gKey','Order'])
if has_duplicates:
  print("중복 O")
  dc['Order'] = dc.index * 10
else:
  print("중복 X")

# 인덱스를 재설정하여 새로운 행 번호 부여
dc = dc.reset_index(drop=True)

dc.to_csv(my_dir + '/input_contents2.txt', index=False)

# 데이터프레임 출력
df_shape = df.shape
dc_shape = dc.shape

# print(f"데이터프레임의 크기: {df_shape}")
# print(f"행의 수: {df_shape[0]}")
# print(df_shape[0], df)


### File Index
# 1.1 HTML 앞부분 공통 내역 읽기
with open(my_dir + "/input_index.txt", 'r', encoding='utf-8') as fi_index:
  fi_index_lines = fi_index.readlines()
# 1.2 파일 열고, HTML 앞부분 공통 내역 쓰기
fmyindex = open(my_dir + "/../pyhtml/index.html", 'w', encoding='utf-8')
fmyindex.writelines(fi_index_lines)
# 2. 본문 쓰기
for n_row in range(df_shape[0]):                    # 1줄씩 읽으려고 함
  if df.loc[n_row,"Key"] == "0":
    fmyindex.write("<br><h4>" + df.loc[n_row,"Name"] + "</h4>\n")
  else:
    fmyindex.write("<p><a href=\"./" + df.loc[n_row,"Key"] + ".html\"" + ">" + df.loc[n_row,"Name"] + "</a></p>\n")
# 3. 파일 마무리 & 닫기
fmyindex.write("</body>\n</html>\n") # 파일 끝 저장 : 마지막 파일
fmyindex.close()
### END OF File Index


### File Contents
# 1. 변수 초기화
my_gKey = "__isnotmyname__"
fw_cnt = 0
# 2. Contents 쓰기
for n_row in range(dc_shape[0]):                    # 1줄씩 읽으려고 함
  # 2.1 새로운 파일 열기 (기존 파일 닫기)
  if n_row == 0  or  dc.loc[n_row,"gKey"] != my_gKey:
    # CLOSE Previous contents
    if n_row != 0:  
      fw.write("</body>\n</html>\n") 
      fw.close()
    # NEW Open & Write Init
    fw = open(my_dir + "/../pyhtml/" + dc.loc[n_row,"gKey"] + ".html", 'w', encoding='utf-8')
    fw.writelines(fi_index_lines)
    my_gKey = dc.loc[n_row,"gKey"]
    fw_cnt += 1
  # 2.2 현재 파일 본문 쓰기
  # HTML URL인 경우 : ".html"로 끝나는 경우
  if dc.loc[n_row,"Key"].find(".html") >= 0:
    fw.write("<p><a href=\"" + "../" + dc.loc[n_row,"Key"] + "\">" + dc.loc[n_row,"Name"] +"</a></p>\n")    
  # 2. 중간 제목인 경우 : "T"로 시작하는 경우 (T 제외하게 출력함)            
  elif dc.loc[n_row,"Key"][0] == 'T':
    fw.write("<br>\n<h4>" + dc.loc[n_row,"Key"][1:] + "</h4>\n")                
  # 3. 나머지는 PDF 파일로 생각함
  else:
    fw.write("<p><a href=\"../contensts/" + dc.loc[n_row,"Key"] + ".pdf\">" + dc.loc[n_row,"Key"] + ". " + dc.loc[n_row,"Name"] +"</a></p>\n")  # PDF URL

  # 2.3 (임시) 두번째 파일 첫번째 내용 적고 빠져 나오기
  # if fw_cnt == 2:
  #   break

# 3. 마지막 파일 마무리 & 닫기
fw.write("</body>\n</html>\n") # 파일 끝 저장 : 마지막 파일
fw.close()
### EDN OF File Index
