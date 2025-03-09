###
# 텍스트 파일로 된 것을 SQLite로 옮기기
###

import my11_pgmb_class as c11p

# 1. 초기화 
my11 = c11p.cMy11pgmB()

# 2. BLOG 만들기 : 동일하게 생성된 것 확인
my11.gen_group()
 

# 3. 텍스트입력모드 : 조회하고 변경하고
my11.input_command()