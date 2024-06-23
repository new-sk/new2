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
my_pyname = ["my2_schedule_now","my1_pgmb_v2","my3_py_html"]
my_pydesc = ["일정관리","블로그만들기","소스보기"]

#########################
### 파이썬 소스 index file
pyhtml = gen_title("Python Source")

pyhtml += "<p><a href=\"" + "../pyhtml/" + my_pyname[0] + ".html\">" + my_pydesc[0] +"</a></p>\n"
pyhtml += "<p><a href=\"" + "../pyhtml/" + my_pyname[1] + ".html\">" + my_pydesc[1] +"</a></p>\n"
pyhtml += "<p><a href=\"" + "../pyhtml/" + my_pyname[2] + ".html\">" + my_pydesc[2] +"</a></p>\n"

pyhtml += gen_tail()

# HTML 내용을 파일로 저장
with open(my_home + '/../pyhtml/my_pysource.html', "w", encoding="utf-8") as file:
  file.write(pyhtml)


#########################
### 진짜 소스 파일들
for file_name in my_pyname:   
  pyhtml = gen_title("Python Source")

# WOW.240623 
# : pre tag : html 문서에서 텍스트 문서를 표출할 때 사용
# : import html : html.escape를 사용하여 문제가 되는 부분들 제거하여 소스 다 보이게 함. 변수명으로 html을 사용하여 충돌나니깐 변수명 바꾸어 줄었음
  pyhtml += "  <pre>"\
  # READ python source file
  with open(my_home + '/' + file_name + '.py', 'r', encoding='utf-8') as file:
    html_read = file.read()
    pyhtml += escape_html(html_read)
  pyhtml += "  </pre>"
# WOW.240623 : END

  pyhtml += gen_tail()

  # HTML 내용을 파일로 저장
  with open(my_home + '/../pyhtml/' + file_name + '.html', "w", encoding="utf-8") as file:
    file.write(pyhtml)
