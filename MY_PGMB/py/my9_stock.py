import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime

import urllib.request
import ssl

# 초기화 : 비어있는 배열
result_date = []
result_index = []

# 페이지는 1번부터
for pnum in range(1491,1495):
  # 읽어야 하는 곳
  basic_url = "https://finance.naver.com/sise/sise_index_day.naver?code=KOSPI&page=" + str(pnum)

  # SSL 인증서 안 거치는 것 권장하지 않는다고 함
  context = ssl._create_unverified_context()
  fp = urllib.request.urlopen(basic_url, context=context)
  # fp = urllib.request.urlopen(basic_url)
  source = fp.read()
  print(source)
  fp.close()

  # soup를 2번하다. 날짜 / 숫자값
  # 1. 날짜
  soup = BeautifulSoup(source, 'html.parser')
  soup1 = soup.findAll("td",class_="date")
  text_date = [tag.get_text(strip=True) for tag in soup1]
  # 2. 숫자
  soup2 = soup.findAll("td",class_="number_1")
  text_index = [tag.get_text(strip=True) for tag in soup2]

  # 겁나 짜증난다. 숫자는 종류가 많다. 매 4번째만 진짜다
  # 추출할 인덱스 설정: 첫 번째 인덱스(0번 인덱스)와 매 4번째 인덱스
  index_extract = list(range(0, len(text_index), 4))
  # 새로운 배열에 추출된 값 저장
  text_index = [text_index[i] for i in index_extract]

  if not result_date:
    result_date = text_date
    result_index = text_index
  else:
    result_date += text_date
    result_index += text_index

# 배열 출력 : for문 밖에서
print(result_date)
print(result_index)
