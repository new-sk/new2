# 보완 필요사항
# 1. LUNAR
# 2. 1회성 이벤트
# 3. 소스 별도 보관 : 소스, 인풋, 아웃풋
# 4. 실적 파일 별도 관리 (아웃품과 또 다른)

import os
my_dir, my_file = os.path.split(__file__)

from datetime import datetime
from dateutil.relativedelta import relativedelta  # 윤년 고려

import pandas as pd
# CSV 파일을 읽어서 데이터프레임에 저장
#df = pd.read_csv(my_dir + '/my_schedule_input.txt')
df = pd.read_csv(my_dir + '/my_schedule_input.txt', converters={'Date': lambda x: pd.to_datetime(x, format='%Y.%m.%d')})
df['CycleMemo'] = ''
print(type(df), df)

# 오늘 날짜를 가져오기
today = datetime.today()
print("today : " , today)
today = datetime(today.year, today.month, today.day)
print("today : " , today)


# YEARLY PLAN
# 연간계획 추출
dfy = df[(df['Cycle'] == 'Y')]
dfy = dfy.copy()

# 최근 1년 이내의 값이 아닌 것이 있는지 확인 : 조사안함 : NY일 경우 처리 방법이 모호함
'''
year1_ago = today - relativedelta(years=1)
year1_next = today + relativedelta(years=1)
year1_range = (dfy['Date'] < year1_ago) | (dfy['Date'] > year1_next)

if year1_range.any():
  print("="*50)
  print("WARNING : 최근 1년 이내의 값이 아닌 데이터가 있습니다.")
  print(dfy[year1_range])
  print("="*50)
'''

# 연간 플랜 수립
def update_year(row):
  if row['Date'] >= today:
    return row['Date'], "This Year"
  else:
    return row['Date'] + relativedelta(years=row['Num']), "Next " + str(row['Num']) + " Year(s)"
  
dfy[['Date','CycleMemo']] = dfy.apply(update_year, axis=1, result_type='expand') # 각 행별로 날짜 변경

print("Yearly Plan")
print(dfy)


# MONTHLY PLAN
# 월간계획 추출
dfm = df[(df['Cycle'] == 'M')]
dfm = dfm.copy()

# 월간 플랜 수립
def update_month(row):
  return row['Date'] + relativedelta(months=row['Num'])

# 첫 월간
dfm['CycleMemo'] = 'This Month'

# 두번째 월간
dfm2 = dfm.copy()
dfm2['Date'] = dfm2.apply(update_month, axis=1) # 각 행별로 날짜 변경
dfm2['CycleMemo'] = '2nd ' + dfm2['Num'].astype(str) + ' Month'

## 세번째 월간
#dfm3 = dfm2.copy()
#dfm3['Date'] = dfm3.apply(update_month, axis=1) # 각 행별로 날짜 변경
#dfm3['CycleMemo'] = 'Next ' + dfm2['Num'].astype(str) + ' Month(s)'

# 월간 종합
print("Monthly Plan")
#dfm = pd.concat([dfm,dfm2,dfm3])
dfm = pd.concat([dfm,dfm2])
print(dfm)


# WEEKLY PLAN
# 주간계획 추출
dfw = df[(df['Cycle'] == 'W')]
dfw = dfw.copy()

# 주간 플랜 수립
def update_week(row):
  return row['Date'] + relativedelta(weeks=row['Num'])

# 첫 주간
dfw['CycleMemo'] = 'This Week'

# 두번째 주간
dfw2 = dfw.copy()
dfw2['Date'] = dfw2.apply(update_week, axis=1) # 각 행별로 날짜 변경
dfw2['CycleMemo'] = '2nd ' + dfw2['Num'].astype(str) + ' Week'

# 세번째 주간
dfw3 = dfw2.copy()
dfw3['Date'] = dfw3.apply(update_week, axis=1) # 각 행별로 날짜 변경
dfw3['CycleMemo'] = 'Next ' + dfw3['Num'].astype(str) + ' Week(s)'

## 네번째 주간
#dfw4 = dfw3.copy()
#dfw4['Date'] = dfw4.apply(update_week, axis=1) # 각 행별로 날짜 변경
#dfw4['CycleMemo'] = 'Next ' + dfw4['Num'].astype(str) + ' Week(s)'
#
## 다섯번째 주간
#dfw5 = dfw4.copy()
#dfw5['Date'] = dfw5.apply(update_week, axis=1) # 각 행별로 날짜 변경
#dfw5['CycleMemo'] = 'Next ' + dfw5['Num'].astype(str) + ' Week(s)'

print("Weekly Plan")
#dfw = pd.concat([dfw,dfw2,dfw3,dfw4,dfw5])
dfw = pd.concat([dfw,dfw2,dfw3])
print(dfw)


### TOTAL
df = pd.concat([dfy,dfm,dfw])
df = df.sort_values("Date")
print("Total Plan")
print(df)

# (WARNING) 오늘 이전날짜 계획이 있는가? 
file_mode = 'w'
if not df[ df['Date'] < today ].empty:
  with open(my_dir + '/my_schedule_output.txt', 'w', encoding='utf-8') as f:
    print("-"*50, file=f)
    print("WARNING", file=f)
    print( df[ df['Date'] < today ], file=f)
  file_mode = 'a'

# Generate OUTPUT file
with open(my_dir + '/my_schedule_output.txt', file_mode, encoding='utf-8') as f:
  print("-"*50, file=f)
  print ("이번달(" + today.strftime('%Y-%m') + ") 일정", file=f)
  print( df[ (df['Date'].dt.year == today.year) & (df['Date'].dt.month == today.month) ], file=f)

with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
  print("-"*50, file=f)
  nextm_day = today + relativedelta(months=1)
  print ("다음달(" + nextm_day.strftime('%Y-%m') + ") 일정", file=f)
  print( df[ (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month == nextm_day.month) ], file=f)

# 이건 잠시만 막는거야...
with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
  print("-"*50, file=f)
  print("이후 일정", file=f)
  print( df[ (df['Date'].dt.year > nextm_day.year)  |  (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month > nextm_day.month) ].sort_values(by=["Cycle","Date"], ascending=[False,True]), file=f)
  print("-"*50, file=f)

