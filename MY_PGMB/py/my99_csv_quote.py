### df 파일을 읽어서 일부만 저장하고파요.

import os
import pandas as pd

my_dir, my_file = os.path.split(__file__)

# 파일읽기
df = pd.read_csv(my_dir + '/my1_input_group2.txt')

# 첫 번째 컬럼 값이 0이 아닌 행만 필터링
df_filtered = df[df.iloc[:, 0] != 0]
# 첫 번째 컬럼으로 오름차순 정렬
df_sorted = df_filtered.sort_values(by=df_filtered.columns[0])
# 첫 번째와 세 번째 컬럼만 추출
df_subset = df_sorted.iloc[:, [0, 2]]

# 각 값을 문자열로 변환하고 따옴표를 추가하여 b.txt로 저장
df_subset = df_subset.astype(str)
df_subset.to_csv(my_dir + '/my1_input_group3.txt', index=False, header=True, quoting=1)  # quoting=1은 각 값을 큰따옴표로 묶는 옵션

print("파일이 새롭게 저장되었습니다.")
