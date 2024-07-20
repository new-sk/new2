import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime

import ssl
import re

import pandas as pd

# 초기화 : 비어있는 배열
result_date = []
result_index = []

is_first = True
c_pnum = 0       # 다음 페이지부터 처리함
l_pnum = c_pnum + 1 # 최소 1페이지 처리
# sName = "KOSPI"
sName = "005930"  # 삼성전자

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.272 Whale/2.9.118.16 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

n_loop = 0

# 페이지는 1번부터
while (c_pnum+1) <= l_pnum:
  c_pnum += 1
  n_loop += 1
  # 읽어야 하는 곳 (KOSPI)
  # basic_url = "https://finance.naver.com/sise/sise_index_day.naver?code=KOSPI&page=" + str(c_pnum)

  if n_loop == 2: # 1개만 처리 : 테스트용
     break  

  # 읽어야 하는 곳 (삼성전자)
  basic_url = "https://finance.naver.com/item/sise_day.naver?code=005930&page=" + str(c_pnum)
  print(basic_url)               
               
  # 웹 페이지 열기 / SOUP까지 수행
  context = ssl._create_unverified_context()
  req = urllib.request.Request(basic_url, headers = headers);  # 개별종목 처리 위해서는 이것이 필요함 : 아마도 막은 듯
  with urllib.request.urlopen(req, context=context) as response:
    # 바이너리 데이터 읽기
    data = response.read()
    # euc-kr 인코딩으로 디코딩  (NAVER에서 사용한 것임)
    source = data.decode('euc-kr')
    # source = data.decode('utf-8')

  soup = BeautifulSoup(source, 'html.parser')

  
  # 첫번째 페이지 열고서 하는 작업들
  if is_first == True:
    print(c_pnum)
    print(source)
    is_first = False

    # 클래스가 'pgRR'인 <td> 태그 찾기
    td_tag = soup.find('td', class_='pgRR')

    # <td> 태그 내부의 <a> 태그에서 'href' 속성 추출
    if td_tag:
        a_tag = td_tag.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href = a_tag['href']
            # 페이지 번호 추출 (예: "/sise/sise_index_day.naver?code=KOSPI&page=1492")
            match = re.search(r'page=(\d+)', href)
            if match:
                l_pnum = int(match.group(1))
                print(type(l_pnum))
                print("맨뒤의 페이지 번호는:", l_pnum)
            else:
                print("페이지 번호를 찾을 수 없습니다.")
        else:
            print("<a> 태그를 찾을 수 없습니다.")
    else:
        print("클래스가 'pgRR'인 <td> 태그를 찾을 수 없습니다.")

  if sName == "KOSPI":
    # soup를 2번하다. 날짜 / 숫자값
    # 1. 날짜
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
  else:
    # soup를 2번하다. 날짜 / 숫자값
    # 1. 날짜
    # soup1 = soup.findAll("tr")
    # onmouseout 및 onmouseover 속성을 가진 <tr> 태그 찾기
    soup1 = soup.find_all('tr', attrs={'onmouseout': True, 'onmouseover': True})

    print('')
    print(soup1)
    print('')

    # soup1 = soup.findAll("span",class_="tah p10 gray03")
    # text_date = [tag.get_text(strip=True) for tag in soup1]
    
    text_date  = []
    text_index = []
    soup1 = soup.find_all('tr', attrs={'onmouseout': True, 'onmouseover': True})
    for row in soup1:
      # 타겟 <span> 요소 다음의 형제 요소들 찾기
      row_date = row.find('span', class_='tah p10 gray03')
      text_date.append(row_date.text)
      print(row_date.text)

      row_index = row.find('span', class_='tah p11')  # 여러개 나오지만, 첫번째 것만 활용
      text_index.append(row_index.text)
      print(row_index.text)
     

  if c_pnum == l_pnum:
     text_date = list(filter(None, text_date))
     text_index = list(filter(None, text_index))

  if (c_pnum % 100) == 0:
     print(c_pnum)

  if not result_date:
    result_date = text_date
    result_index = text_index
  else:
    result_date += text_date
    result_index += text_index

  
# 배열 출력 : for문 밖에서
print(result_date)
print(result_index)

import os
my_dir, my_file = os.path.split(__file__)

# 데이터프레임 생성
df = pd.DataFrame({
    'sName': sName,
    'Date': result_date,
    'Price': result_index
})

# 데이터프레임을 CSV 파일로 저장
df.to_csv(my_dir + '/my9_stock_out.txt', index=False)

print("DataFrame을 'data.csv' 파일로 저장했습니다.")