import my10_pgmb_class as c10p

my10 = c10p.cMy10pgmB()

# 전체 파일 새로 만들기
# my10.gen_group()
 
# 작성중이거나 매핑안된 파일 찾기
# 전체 내용중에서 특정 내역 찾기  (GG기준, 관련 내용, contents)
# 

import subprocess

# 편집할 파일 경로
file_path = "../../../book/book_0138.md"

# VSCode에서 파일 열기
subprocess.run(["code", file_path])