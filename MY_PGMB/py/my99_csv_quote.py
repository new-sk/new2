### df 파일을 읽어서 일부만 저장하고파요.

import os
import pandas as pd

my_dir, my_file = os.path.split(__file__)

# 파일읽기
df = pd.read_csv(my_dir + '/py10/my10_input_contents_cd.txt')  # 숫자로 읽어야 정렬이 되지 dtype={0: str})

# 두 번째 컬럼의 첫 번째 문자가 "T"가 아닌 경우 필터링
# filtered_df = df[df.iloc[:, 2].str[0] != "T"]

# 중복된 행 추출
duplicated_df = df[df.iloc[:, 1].duplicated(keep=False)]


# 첫 번째 컬럼으로 오름차순 정렬
# df_sorted = df.sort_values(by=df.columns[0])

# 첫 번째와 세 번째 컬럼만 추출
# df_subset = df_sorted.iloc[:, [0, 2]]

# 각 값을 문자열로 변환하고 따옴표를 추가하여 b.txt로 저장
# df_subset = df_sorted.astype(str).replace("nan",'')
# df_subset['NKey'] = "C2020" + (df.index + 1).astype(str).str.zfill(4) + "0"

# 원하는 순서로 컬럼 재배치 (B, A, C, New_Column)
# df_subset = filtered_df[['cKey', 'cURL', 'cName']]
# "Order","Key","gKey","Name","NKey"

# CSV
duplicated_df.to_csv(my_dir + '/py10/my10_input_contents_dup.txt', index=False, header=True, quoting=1)  # quoting=1은 각 값을 큰따옴표로 묶는 옵션

print("파일이 새롭게 저장되었습니다.")
