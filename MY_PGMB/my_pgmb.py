#import platform
#my_os = platform.system()

import os
my_dir, my_file = os.path.split(__file__)

### 파일 읽기 1, 2
with open(my_dir + "/input_contents.txt", 'r', encoding='utf-8') as f:
	lines = f.readlines()
n_lines = len(lines)

first_name = "python"
with open(my_dir + "/input_index.txt", 'r', encoding='utf-8') as fi2:
  fi2_lines = fi2.readlines()

### 파일쓰기 : 앞부분
fmyindex = open(my_dir + "/index.html", 'w', encoding='utf-8')
fmyindex.writelines(fi2_lines)

### 파일쓰기2 : 실제 내용 : 소팅이 되어 있다고 가정
i = 0
my_name = "__isntmyname__"
while i < n_lines:                    # 1줄씩 읽으려고 함
  i_tokens = lines[i].split(',')      # 1줄씩 읽어서 리스트변수에 입력
  if i==0 or i_tokens[1]!=my_name:
      if i!=0:
        fw.write("</body>\n</html>\n")  # 파일 끝 저장
        fw.close()
      fw = open(my_dir + "/my_" + i_tokens[1] + ".html", 'w', encoding='utf-8')
      fw.writelines(fi2_lines)
      fw.write("<h2>" + i_tokens[1] + "</h2>\n</header>\n")  # 파일 시작 저장 : 공통   
      fmyindex.write("<p><a href=\"./my_" + i_tokens[1] + ".html\"" + ">" + i_tokens[1] + "</a></p>\n")
      my_name = i_tokens[1]

  if i_tokens[1]!="":                 # 기존 파일에 계속 출력함
    if i_tokens[0].find(".") >= 0:
      fw.write("<p><a href=\"" + i_tokens[0] + "\">" + i_tokens[2] +"</a></p>\n")                # HTML URL
    else:
      fw.write("<p><a href=\"./contensts/" + i_tokens[0] + ".pdf\">" + i_tokens[0] + ". " + i_tokens[2] +"</a></p>\n")  # PDF URL
  i += 1

### 파일쓰기3 : 마무리 & 닫기
fw.write("</body>\n</html>\n") # 파일 끝 저장 : 마지막 파일
fw.close()
fmyindex.write("</body>\n</html>\n") # 파일 끝 저장 : 마지막 파일
fmyindex.close()
