# HTML Escape 함수 정의
import html

def escape_html(text):
  return html.escape(text, quote=False)
    
    
# 파이썬 소스를 html 문서로 보여주기
import os
import sys
my_home, my_file = os.path.split(__file__)

print(my_home, my_file)

# file header
def gen_title(title):
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
def gen_tail():
  return f"""
</body>
</html>
"""


#########################
### 소스 파일 리스트
my_pyname = ["my2_schedule_now","my1_pgmb_v2","my3_py_html","my9_stock"]
my_pydesc = ["일정관리","블로그만들기","소스보기","투자관리"]

#########################
### 파이썬 소스 index file
pyhtml = gen_title("Python Source")

for i in range(len(my_pyname)):
  pyhtml += "<p><a href=\"" + "../pyhtml/" + my_pyname[i] + ".html\">" + my_pydesc[i] +"</a></p>\n"

pyhtml += gen_tail()

# HTML 내용을 파일로 저장
with open(my_home + '/../pyhtml/my_pysource.html', "w", encoding="utf-8") as file:
  file.write(pyhtml)


#########################
### 진짜 소스 파일들
for file_name in my_pyname:   
  pyhtml = gen_title("Python Source")

# WOW.240623 
# WOW : pre tag : html 문서에서 텍스트 문서를 표출할 때 사용, pre tag를 조절해서 WOW가 있는 줄만 강조해서 보이게 조정함
# WOW : import html : html.escape를 사용하여 문제가 되는 부분들 제거하여 소스 다 보이게 함. 변수명으로 html을 사용하여 충돌나니깐 변수명 바꾸어 줄었음
  # READ python source file
  with open(my_home + '/' + file_name + '.py', 'r', encoding='utf-8') as file:
    lines = file.readlines()

  # 각 줄을 확인하고 특정 문자가 포함된 줄을 강조합니다. "W O W"
  pyhtml += "  <pre>\n"
  for line in lines:
    if 'WOW' in line  and  "'WOW'" not in line:
        pyhtml += '</pre>\n'
        pyhtml += f'<span style="color:red;">{line}</span>\n'
        pyhtml += '<pre>\n'
    else:
        pyhtml += escape_html(line)
  pyhtml += "  </pre>\n"
# WOW.240623 : END

  pyhtml += gen_tail()

  # HTML 내용을 파일로 저장
  with open(my_home + '/../pyhtml/' + file_name + '.html', "w", encoding="utf-8") as file:
    file.write(pyhtml)


