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
my_pyname = ["my_schedule_now","my_pgmb_v2","my_py_html"]
my_pydesc = ["일정관리","블로그만들기","소스보기"]

#########################
### 파이썬 소스 index file
html = gen_title("Python Source")

html += "<p><a href=\"" + "../py/" + my_pyname[0] + ".html\">" + my_pydesc[0] +"</a></p>\n"
html += "<p><a href=\"" + "../py/" + my_pyname[1] + ".html\">" + my_pydesc[1] +"</a></p>\n"
html += "<p><a href=\"" + "../py/" + my_pyname[2] + ".html\">" + my_pydesc[2] +"</a></p>\n"

html += gen_tail()

# HTML 내용을 파일로 저장
file_index = os.path.join(my_home, 'conhtml', 'my_pysource.html')
with open(my_home + '/../conhtml/my_pysource.html', "w", encoding="utf-8") as file:
  file.write(html)


#########################
### 진짜 소스 파일들
for file_name in my_pyname:   
  html = gen_title("Python Source")

# WOW.240623 : pre tag : html 문서에서 텍스트 문서를 표출할 때 사용
  html += "  <pre>"\
  # READ python source file
  with open(my_home + '/' + file_name + '.py', 'r', encoding='utf-8') as file:
    html += file.read()
  html += "  </pre>"
# WOW.240623 : pre tag : END

  html += gen_tail()

  # HTML 내용을 파일로 저장
  with open(my_home + '/' + file_name + '.html', "w", encoding="utf-8") as file:
    file.write(html)
