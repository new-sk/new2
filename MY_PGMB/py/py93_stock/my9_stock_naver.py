# NAVER에서 주가지수 스크롤링

import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
import os
from datetime import datetime, timedelta
import pandas as pd
import configparser  # 24.07.28 추가 : INI 설정
import sys

class cMy9Stock:

  def __init__(self):
    self.sMode = ""
    self.max_loop = 3                        # Test Mode인 경우 3페이지만 가져옴
    self.my_dir = ""                         # os
    self.my_xfile = '/my9_stock_sData.xlsx'  # excel file

    self.set_mode()
    self.get_excel()

  def set_mode(self):
    ### 1. set mode
    # 1.1 INI파일에서 mode 설정
    self.my_dir, my_file = os.path.split(__file__)
    my_os = os.name

    # WOW : 설정 파일 만들고 읽기
    config_file = my_file.rsplit('.', 1)[0] + '.ini'
    config = configparser.ConfigParser()  # 객체 생성
    config.read(self.my_dir + '/' + config_file)  # 설정 파일 읽기 (파일 위치)
    self.sMode = config.get('mode', 'smode')

    # 1.3.1 Real 모드만 허용
    if self.sMode != "Real":
      # self.max_loop = 3  # 2페이지만 가져오기 (1,2)
      sys.exit("Real에서만 수행합니다.")

    # 1.3.2 윈도우즈에서만 수행 허용
    if my_os != "nt":
      sys.exit("윈도우즈에서만 수행합니다.")

    # 1.3.3 변수 정의
    self.max_loop = 0  # 전체 가져오기
    self.my_dir = 'D:\MY_BLOG_LOCAL_HOME\py'
    

  def get_excel(self): 
    # WOW : 엑셀 읽기 : 
    #     : 파일명, 시트명(sheet_name)
    #     : 열명(usecols) : 컬럼영문알파벳, 인덱스(숫자0부터), 컬럼명  : 'A:E', range(0,4), ['saAccount','saName'] 
    # WOW : 데이터타입(dtype) 숫자로 지정해도 엑셀에 저장된 값이 float이면 intger로 변환되지 않는다고 함 : 음... 엑셀에서 int로 변환한것도 float로 저장되는데, 

    sheet_names = ["sData", "4.sData.so"]  # 사용할 시트 이름들을 여기에 추가

    # 모든 시트에 대해 반복 실행
    for sheet in sheet_names:
      df = pd.read_excel(self.my_dir + self.my_xfile, sheet_name=sheet, usecols='A:E', na_values=["N/A", "NA", "-", "", "none"])
      df = df.dropna()
      print(df)

      for sName in df['spName']:
        startN = df.loc[df['spName'] == sName, 'spStart'].iloc[0].astype('int32')
        endN   = df.loc[df['spName'] == sName, 'spEnd'].iloc[0].astype('int32')
        # print(startN, ' : ', endN)
        dfx = pd.read_excel(self.my_dir + self.my_xfile, sheet_name=sheet, usecols=range(startN-1, startN+endN-1), header=3, na_values=["N/A", "NA", "-", "", "none"])
        # WOW : 모든 값이 na인 경우에만 행을 삭제하도록 개선
        # dfx = dfx.dropna()
        all_na_rows = dfx.isna().all(axis=1) # 모든 값이 NaN인 행을 식별
        dfx = dfx[~all_na_rows]  # 모든 값이 NaN인 행만 제거
        print(sName, " : ", df.loc[df['spName'] == sName, 'spDescK'])
        print(dfx)
        # WOW : global 변수 이름에 해당 데이터 저장 : sName에 저장된 값으로 변수를 만들어서 저장
        globals()[sName] = dfx


    # 데이터타입 지정
    df9y["syYear"] = df9y["syYear"].astype(str)
    df9y["syYield"] = df9y["syYield"].astype(float)
    df9y["syDesc"] = df9y["syDesc"].astype(str)

    df9i["siName"] = df9i["siName"].astype(str)
    df9i["siCode"] = df9i["siCode"].astype(str)
    df9i["siNameF"] = df9i["siNameF"].astype(str)

    df9o["soName"] = df9o["soName"].astype(str)
    df9o["soCode"] = df9o["soCode"].astype(str)
    df9o["sozAmt"] = df9o["sozAmt"].astype(float)
    df9o["sozDate"] = df9o["sozDate"].astype(str)
    df9o["sosPrice"] = df9o["sosPrice"].astype(float)
    df9o["sosDate"] = df9o["sosDate"].astype(str)
    df9o["sobPrice"] = df9o["sobPrice"].astype(float)
    df9o["sobDate"] = df9o["sobDate"].astype(str)
    df9o["soDesc"] = df9o["soDesc"].astype(str)

    df9d["sdName"] = df9d["sdName"].astype(str)
    df9d["sdCode"] = df9d["sdCode"].astype(str)
    df9d["sdAccount"] = df9d["sdAccount"].astype(str)
    df9d["sdDate"] = df9d["sdDate"].astype(str)
    df9d["sdAmt"] = df9d["sdAmt"].astype(float)

    df9a["saAccount"] = df9a["saAccount"].astype(str)
    df9a["saName"] = df9a["saName"].astype(str)
    df9a["saAmt"] = df9a["saAmt"].astype(float)

    df9dw["sdwAccount"] = df9dw["sdwAccount"].astype(str)
    df9dw["sdwDate"] = df9dw["sdwDate"].astype(str)
    df9dw["sdwType"] = df9dw["sdwType"].astype(str)
    df9dw["sdwAmt"] = df9dw["sdwAmt"].astype(float)
    df9dw["sdwDesc"] = df9dw["sdwDesc"].astype(str)


  def get_all(self, sCode, oType):
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

      if n_loop == self.max_loop: # 2(1개만처리), 3(2개만 처리), 마지막만 처리 : 테스트용
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
      df.to_csv(self.my_dir + my9_fname, index=False)

  def get_one(self, sCode):
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
    dfall = pd.read_csv(self.my_dir + my9_fname, dtype={'sCode': str})

    # 추가할 내역만 추출
    dfone = dfone[~dfone['Date'].isin(dfall['Date'])]

    if not dfone.empty:
      # 데이터프레임을 CSV 파일로 저장
      my9_fname2 = '/my9_stock_out2_' + sCode + '.txt'
      dfone.to_csv(self.my_dir + my9_fname2, index=False, header=False)

      # 추가할 파일을 기존 파일에 병합
      with open(self.my_dir + my9_fname2, 'r') as fone:
        new_data = fone.read()
        with open(self.my_dir + my9_fname, 'a') as fall:
          fall.write(new_data)

      # 임시 파일 삭제
      os.remove(self.my_dir + my9_fname2)

  def get_stocks(self):
    for sCode in df9i['siCode']:
      # 파일 존재 여부 확인
      my_filename = self.my_dir + '/my9_stock_out_' + sCode + '.txt' 
      if os.path.exists(my_filename):
        self.get_one(sCode)
        print(sCode + " : 파일이 존재합니다.")
      else:
        self.get_all(sCode, 'FILE')   
        print(sCode + " : 파일을 새로 만들었습니다")

  def xyz(self, str_date):
    dfall = pd.DataFrame() # 초기화

    for sCode in df9i['siCode']:
      # 종목명 정보 읽어오기
      my9_fname = '/my9_stock_out_' + sCode + '.txt'
      dfs = pd.read_csv(self.my_dir + my9_fname, dtype={'sCode': str})
      # 특정 날짜 정보만 취합하기
      dfs = dfs[dfs['Date'].isin(str_date)]
      dfall = pd.concat([dfall, dfs], ignore_index=True)

    # 취합정보 출력
    print(dfall)
    dfall.to_csv(self.my_dir + '/my9_stock_out_all.txt', index=False)

    print(df9o)


  def ssStdAmt(self):

    # 날짜가 지난 조건을 찾아서 출력해줌 : 바꿔 주세요.
    # 오늘
    today = datetime.now()
    # 주말이면 금요일
    if today.weekday() == 5:  # 토요일
        result_date = today - timedelta(days=1)  # 금요일
    elif today.weekday() == 6:  # 일요일
        result_date = today - timedelta(days=2)  # 금요일
    else:
        result_date = today  # 평일은 오늘 날짜 그대로
    # YYYY.MM.DD 형식으로 출력
    wDate = result_date.strftime("%Y.%m.%d")

    filtered_df = df9o[
        (df9o['soUseYN'] == "Y") &
        ((df9o['sosDate'] < wDate) | (df9o['sobDate'] < wDate))
    ]

    # Display the filtered rows
    print()
    if filtered_df.empty:
      print("목표관리 기준일자를 초과한 내역이 없습니다.")
    else:
      print("목표관리 기준일자가 초과되었습니다. 새로 만들어 주세요.:")
      print(filtered_df)   


    # Initialize an empty list to store results
    result = []

    # Loop through each row in df9o to apply filters
    for _, row in df9o[df9o['soUseYN'] == "Y"].iterrows():
        my9_fname = f"/my9_stock_out_{row['soCode']}.txt"
        dfs = pd.read_csv(self.my_dir + my9_fname, dtype={'sCode': str})
        dfs["Price"] = dfs["Price"].str.replace(",", "").astype(float)

        # Filter dfs based on conditions without date conversion
        matched_dfs = dfs[
            (dfs['sCode'] == str(row['soCode'])) &                                  # 종목코드 동일하고
            ((dfs['Date'] >= row['sozDate']) | (dfs['Date'] >= row['sozDate'])) &     # 기준일자보다 크거나 같고
          #  ((dfs['Date'] <= row['sosDate']) | (dfs['Date'] <= row['sobDate'])) &     # 종료일자는 체크 안하는 것으로, 24.12.26
            ((dfs['Price'] >= row['sosPrice']) | (dfs['Price'] <= row['sobPrice']))   # 목표가 이상(이하)
        ]

        # matched_dfs에 row의 데이터 추가
        # row를 DataFrame으로 변환하고, matched_dfs의 행 개수만큼 반복
        selected_row = row[['soName', 'sobPrice', 'sosPrice', 'soDesc']]  # 원하는 컬럼만 선택
        row_df = pd.DataFrame([selected_row] * len(matched_dfs), index=matched_dfs.index)

        # row와 matched_dfs를 수평으로 결합 (열 방향으로 합침)
        joined_df = pd.concat([matched_dfs, row_df], axis=1)

        # 결합된 결과를 result에 추가
        result.append(joined_df)

    # 결과를 하나의 DataFrame으로 결합
    final_result = pd.concat(result, ignore_index=True)
    print()
    if final_result.empty:
      print("목표 기준에 도달한 내역이 없습니다.")
    else:
      print("목표 기준에 부합한 내역이 있습니다. 확인후 조치부탁합니다.:")
      with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(final_result)  # 설정이 이 블록 안에서만 적용됨

