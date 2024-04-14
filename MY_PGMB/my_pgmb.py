### 파일 읽기 1, 2
with open("d:/MY/new2/new2/MY_PGMB/input_contents.txt", 'r', encoding='utf-8') as f:
	lines = f.readlines()
n_lines = len(lines)

first_name = "python"
with open("d:/MY/new2/new2/MY_PGMB/input_index.txt", 'r', encoding='utf-8') as fi2:
  fi2_lines = fi2.readlines()

### 파일쓰기 : 앞부분
fw = open("d:/MY/new2/new2/MY_PGMB/inex.html", 'w', encoding='utf-8')
fw.writelines(fi2_lines)

### 파일쓰기2 : 실제 내용
i = 0
while i < n_lines:
  i_tokens = lines[i].split(',')
  if i_tokens[0]=="python":
    if i==0:
        fw.write("<h2>" + i_tokens[0] + "</h2>\n</header>\n")   
    fw.write("<p><a href=\"./contensts/" + i_tokens[1] + ".pdf\">" + i_tokens[1] + ". " + i_tokens[2] +"</a></p>\n")
  i += 1

### 파일쓰기3 : 마무리 & 닫기
fw.write("</body>\n</html>\n")
fw.close()
