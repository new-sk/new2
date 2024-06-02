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
df = pd.read_csv(my_dir + '/input_group.txt')

# 컬럼 Order에서 중복된 값이 있는지 여부 확인
has_duplicates = df['Order'].duplicated().any()

df = df.sort_values(by='Order')
if has_duplicates:
  print("중복 O")
  df['Order'] = df.index * 10
  df.to_csv(my_dir + '/input_group2.txt', index=False)
else:
  print("중복 X")


# 데이터프레임 출력
df_shape = df.shape
print(f"데이터프레임의 크기: {df_shape}")
print(f"행의 수: {df_shape[0]}")

print(df_shape[0], df)


# HTML 앞부분 공통 내역 읽기
with open(my_dir + "/input_index.txt", 'r', encoding='utf-8') as fi_index:
  fi_index_lines = fi_index.readlines()

# HTML 앞부분 공통 내역 쓰기
fmyindex = open(my_dir + "/index.html", 'w', encoding='utf-8')
fmyindex.writelines(fi_index_lines)


### 파일쓰기2 : 실제 내용 : 소팅이 되어 있다고 가정
for n_row in range(df_shape[0]):                    # 1줄씩 읽으려고 함
  fmyindex.write("<p><a href=\"../my_" + df.iloc[n_row,2] + ".html\"" + ">" + df.iloc[n_row,2] + "</a></p>\n")


### 파일쓰기3 : 마무리 & 닫기
fmyindex.write("</body>\n</html>\n") # 파일 끝 저장 : 마지막 파일
fmyindex.close()
