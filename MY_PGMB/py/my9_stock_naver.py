# NAVER에서 주가지수 스크롤링

import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
import os
from datetime import datetime
import pandas as pd

if __name__ == "__main__":
    print("변수가 정의되어 있지 않습니다. \n독립적으로 실행되지 못합니다.")

def get_all(sCode, oType):
  # 아래 2개 변수는 my9_stock에서 정의함
  from my9_stock import my_dir
  from my9_stock import max_loop

  # 초기화 : 비어있는 배열
  result_date = []
  result_index = []

  is_first = True
  c_pnum = 0       # 다음 페이지부터 처리함
  max_pnum = c_pnum + 1 # 최소 1페이지 처리
  # sCode = "KOSPI"
  # sCode = "005930"  # 삼성전자

  # WOW : 브라우저로 읽는 것처럼 변환
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.272 Whale/2.9.118.16 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

  n_loop = 0

  # 페이지는 1번부터
  while (c_pnum+1) <= max_pnum:
    c_pnum += 1
    n_loop += 1

    if n_loop == max_loop: # 2(1개만처리), 3(2개만 처리), 마지막만 처리 : 테스트용
      break  

    # 읽어야 할 페이지
    #   : KOSPI
    if sCode == "KOSPI":
      basic_url = "https://finance.naver.com/sise/sise_index_day.naver?code=KOSPI&page=" + str(c_pnum)
    #   : 개별종목
    else:
      basic_url = "https://finance.naver.com/item/sise_day.naver?code=" + sCode + "&page=" + str(c_pnum)
    #print(basic_url)               
                
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

    ##########################
    # 첫번째 페이지에서만 하는 작업 : 마지막 페이지 확인 (max_pnum)
    if is_first == True:
      print(c_pnum, ':', sCode)
      #print(source)
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
                  max_pnum = int(match.group(1))
                  #print(type(max_pnum))
                  print("맨뒤의 페이지 번호는:", max_pnum)
              else:
                  print("페이지 번호를 찾을 수 없습니다.")
          else:
              print("<a> 태그를 찾을 수 없습니다.")
      else:
          print("클래스가 'pgRR'인 <td> 태그를 찾을 수 없습니다.")

    ##########################
    # 공통내역 : KOSPI
    if sCode == "KOSPI":
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

    # 공통내역 : 개별종목
    else:
      # soup를 2번하다. 날짜 / 숫자값
      # 1. TR 전체를 읽어들임
      text_date  = []
      text_index = []
      soup1 = soup.find_all('tr', attrs={'onmouseout': True, 'onmouseover': True})
      # print('')
      # print(soup1)
      # print('')

      # 2. 날자와 지수 받아 오다
      for row in soup1:
        # 타겟 <span> 요소 다음의 형제 요소들 찾기
        row_date = row.find('span', class_='tah p10 gray03')
        row_index = row.find('span', class_='tah p11')  # 여러개 나오지만, 첫번째 것만 활용

        if row_date is not None:
          text_date.append(row_date.text)
          text_index.append(row_index.text)
          #print(row_date.text, row_index.text)
      

    # 한 페이지 다 읽은 후 : 마지막 페이지 빈칸들 제거
    if c_pnum == max_pnum:
      text_date = list(filter(None, text_date))
      text_index = list(filter(None, text_index))

    # 한 페이지 다 읽은 후 : 100페이지마다 메시지 : 잘 실행되고 있어요 
    if (c_pnum % 100) == 0:
      print(c_pnum, " ", datetime.now())

    # 한 페이지 다 읽은 후 : 결과값 추가
    if not result_date:
      result_date = text_date
      result_index = text_index
    else:
      result_date += text_date
      result_index += text_index

    
  # WOW : 데이터프레임 생성
  df = pd.DataFrame({
      'sCode': sCode,
      'Date': result_date,
      'Price': result_index
  })

  if oType == 'FILE':
    # 데이터프레임을 CSV 파일로 저장
    my9_fname = '/my9_stock_out_' + sCode + '.txt'
    df.to_csv(my_dir + my9_fname, index=False)


def get_one(sCode):
  # 아래 2개 변수는 my9_stock에서 정의함
  from my9_stock import my_dir

  # 초기화 : 비어있는 배열
  result_date = []
  result_index = []

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.272 Whale/2.9.118.16 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

  # 읽어야 할 페이지
  #   : KOSPI
  if sCode == "KOSPI":
    basic_url = "https://finance.naver.com/sise/sise_index_day.naver?code=KOSPI&page=1"
  #   : 개별종목
  else:
    basic_url = "https://finance.naver.com/item/sise_day.naver?code=" + sCode + "&page=1" 
  #print(basic_url)               
              
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


  # 공통내역 : KOSPI
  if sCode == "KOSPI":
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

  # 공통내역 : 개별종목
  else:
    # soup를 2번하다. 날짜 / 숫자값
    # 1. TR 전체를 읽어들임
    text_date  = []
    text_index = []
    soup1 = soup.find_all('tr', attrs={'onmouseout': True, 'onmouseover': True})
    # print('')
    # print(soup1)
    # print('')

    # 2. 날자와 지수 받아 오다
    for row in soup1:
      # 타겟 <span> 요소 다음의 형제 요소들 찾기
      row_date = row.find('span', class_='tah p10 gray03')
      row_index = row.find('span', class_='tah p11')  # 여러개 나오지만, 첫번째 것만 활용

      if row_date is not None:
        text_date.append(row_date.text)
        text_index.append(row_index.text)
        #print(row_date.text, row_index.text)
      

  result_date = text_date
  result_index = text_index

    
  # 데이터프레임 생성
  dfone = pd.DataFrame({
      'sCode': sCode,
      'Date': result_date,
      'Price': result_index
  })

  my9_fname = '/my9_stock_out_' + sCode + '.txt'
  dfall = pd.read_csv(my_dir + my9_fname, dtype={'sCode': str})

  # 추가할 내역만 추출
  dfone = dfone[~dfone['Date'].isin(dfall['Date'])]

  if not dfone.empty:
    # 데이터프레임을 CSV 파일로 저장
    my9_fname2 = '/my9_stock_out2_' + sCode + '.txt'
    dfone.to_csv(my_dir + my9_fname2, index=False, header=False)

    # 추가할 파일을 기존 파일에 병합
    with open(my_dir + my9_fname2, 'r') as fone:
      new_data = fone.read()
      with open(my_dir + my9_fname, 'a') as fall:
        fall.write(new_data)

    # 임시 파일 삭제
    os.remove(my_dir + my9_fname2)
