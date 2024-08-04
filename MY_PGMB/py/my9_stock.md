
종목
- 종목별 가격
  - 모드 : Test/Real
  - 종목정보가져오기(sCode,'FILE')
  - 종목정보가져오기(sCode,'DF')
  - 종목최근정보가져오기(Recently)

- 초기데이터 구축방법 검토 필요
  - 2023년말 
  - 2024 진행사항
  - 현재 사항

- 데이터
  - 종목(Item) : 종목코드(siCode), 종목명(siName), 종목약어명
  - 가격(Price) : 종목코드(spCode), 일자(spDate), 가격(spPrice)
  - 계좌(Account) : 계좌코드(saAccount), 계좌설명(saName), 예수금(saAmt), 계좌구분
  - 입출금(Deposit&Withdrawal) : 입금계좌(sdAccount), 출금계좌(swAccount), 구분(sdwType : D, W, X), 비고
  - 목표수익률(Yield) : 년도(syYear), 수익률(syYield)
  - 배당금(Dividends) : 종목코드(sdCode), 배당금(sdAmt), 배당금세전(sdAmtBf), 배당금세금(sdamtTax), 배당일자(sdDate), 주당배당금(sdPer)
  - 매매(Trade) : 매매번호(stNo,2024-XXX), 매매구분(stType: B, S), 계죄코드(stAccount), 종목코드(stCode), 거래수량(stQty), 단가(stAmtUnit), 거래금액(stAmt), 거래금액세전(stAmtBf),  거래세금(stAmtTax), 상태(stStatus:0 X, 1...n), 잔고수량(stQtyRemain), 잔고금액(stAmtRemain)
  - 매도매핑(Mapping) : 매도번호(smNoS), 매수번호(smNoB), 수량(smQty), 단가(smAmtUnit), 매수금액(smAmtB), 매도금액(smAmtS), 수익금(smProfit), 매수도일련번호

**진행현황**
- 7월5주
  - 모드에 따른 전체 가져오기 
  - 이번주 자료가 가져오기
  - 특정날짜 정보만 추출하기
- 8월1주
  - 설정파일 읽기 (INI)
  - 기초 데이터 읽기 (TXT -> XLXS) 
  - XLXS 기초 데이터 읽기 (컬럼 -> 이름영역) (그냥 컬럼으로 읽는 것으로 하려함)