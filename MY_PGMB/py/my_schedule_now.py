# 보완 필요사항
# WOW NOT : LUNAR
# WOW NOT : 소스 별도 보관 : 소스, 인풋, 아웃풋
# WOW NOT : 실적 파일 별도 관리 (아웃품과 또 다른)
# WOW NOT : HTML 파일 이쁘게 만들기

__istest__ = True

import os
import sys
my_home, my_file = os.path.split(__file__)
my_lhome = 'D:\MY_BLOG_LOCAL_HOME\py'
my_src_file = '/my_schedule_input.txt'

print(my_home, my_file)
print(my_lhome,my_src_file)
#sys.exit()

os = os.name
# REAL & NOT Home (여기서는 안돼요)
if (__istest__==False) and (os!="nt") :
  print("-"*50)
  print("Not Allowed : Real Mode")
  print("-"*50)
  sys.exit() 
# REAL (in HOME)
elif (__istest__==False) and (os=="nt") :
  my_src_dir = my_lhome
  my_desc_dir = my_home
  my_desc_file = '/my_schedule_output.html'
# TEST Home / Full Version
elif  (__istest__==True) and (os=="nt") :
  my_src_dir = my_lhome
  my_desc_dir = my_lhome
  my_desc_file = '/my_schedule_output2.html'
# TEST Not Home / Short Version
elif  (__istest__==True) and (os!="nt") :
  my_src_dir = my_home
  my_desc_dir = my_home
  my_desc_file = '/my_schedule_output2.html'

from datetime import datetime
from dateutil.relativedelta import relativedelta  # 윤년 고려

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# DataFrameApp은 챗GPT로 작성
class DataFrameApp:
    def __init__(self, root, df):
        self.root = root
        self.df = df

        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.columns = list(df.columns)
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings')

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for index, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<ButtonRelease-1>", self.on_row_click)

        self.info_frame = tk.Frame(self.frame)
        self.info_frame.pack(fill=tk.X, expand=True)

        self.entry_vars = {col: tk.StringVar() for col in self.columns}
        for col in self.columns:
            tk.Label(self.info_frame, text=col).pack(side=tk.LEFT)
            entry = tk.Entry(self.info_frame, textvariable=self.entry_vars[col])
            entry.pack(side=tk.LEFT)

        self.update_button = tk.Button(self.info_frame, text="Update Row", command=self.update_row)
        self.update_button.pack(side=tk.LEFT)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_row_click(self, event):
        item = self.tree.selection()[0]
        row_values = self.tree.item(item, "values")
        for col, val in zip(self.columns, row_values):
            self.entry_vars[col].set(val)

    def update_row(self):
        item = self.tree.selection()[0]
        row_index = self.tree.index(item)
        updated_values = [self.entry_vars[col].get() for col in self.columns]

        # DataFrame 업데이트
        for col, val in zip(self.columns, updated_values):
            self.df.at[row_index, col] = val

        # Treeview 업데이트
        self.tree.item(item, values=updated_values)

    def on_closing(self):
        if messagebox.askyesno("Quit", "Do you want to save the DataFrame before quitting?"):
            # DataFrame 저장 (예: CSV 파일로 저장)
            self.df.to_csv("output.csv", index=False)
        self.root.destroy()

def show_df_window(df):
    root = tk.Tk()
    root.title("DataFrame Viewer")
    app = DataFrameApp(root, df)
    root.mainloop()

import pandas as pd
# CSV 파일을 읽어서 데이터프레임에 저장
#df = pd.read_csv(my_dir + '/my_schedule_input.txt')
df = pd.read_csv(my_src_dir + my_src_file, converters={'Date': lambda x: pd.to_datetime(x, format='%Y.%m.%d')})
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

# 연간 플랜 수립
def update_year(row):
  if row['Date'] >= today:
    return row['Date'], "This Year"
  else:
    return row['Date'] + relativedelta(years=row['Num']), "Next " + str(row['Num']) + " Year(s)"
  
dfy[['Date','CycleMemo']] = dfy.apply(update_year, axis=1, result_type='expand') # 각 행별로 날짜 변경

print("Yearly Plan")
#print(dfy)


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
#print(dfm)


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

# # 세번째 주간
# dfw3 = dfw2.copy()
# dfw3['Date'] = dfw3.apply(update_week, axis=1) # 각 행별로 날짜 변경
# dfw3['CycleMemo'] = 'Next ' + dfw3['Num'].astype(str) + ' Week(s)'


print("Weekly Plan")
#dfw = pd.concat([dfw,dfw2,dfw3,dfw4,dfw5])
dfw = pd.concat([dfw,dfw2])
#print(dfw)


# ONE-Time, Irregular PLAN
# 있는 그대로 복사
print("ONE-Time, Irregular Plan")
dfone = df[(df['Cycle'] == 'O') | (df['Cycle'] == 'X' )]


### TOTAL
df = pd.concat([dfy,dfm,dfw,dfone])
df = df.sort_values("Date")
df = df.reset_index(drop=True)   # re-index
print("Total Plan")
print(df)


# WOW 240620_mapping : pandas 기능. 간단하게 매핑에 유용하게 활용, apply 함수는 복잡한 경우 활용
# Define & Apply the mapping
cycle_mapping = {
    "W": "Weekly",
    "M": "Monthly",
    "Y": "Yearly",
    "O": "One-Time",
    "X": "Irregular"
}

df["Cycle"] = df["Cycle"].map(cycle_mapping)
# WOW 240620_mapping : END



# 제목 설정 : 현재 모드 출력 : Test & Not Test
if __istest__ :
  title = "일정관리 (Test Mode)"
else :
  title = "일정관리 (Real Mode)"
  



# Warning 
title_0 = "Warning"
df_0 = df[ df['Date'] < today ].copy()
df_0['Date'] = df_0['Date'].dt.strftime('%Y-%m-%d')

# This Month
title_1 = "이번달(" + today.strftime('%Y-%m') + ") 일정"
df_1 = df[ (df['Date'].dt.year == today.year) & (df['Date'].dt.month == today.month) ].copy()
df_1['Date'] = df_1['Date'].dt.strftime('%Y-%m-%d')

# Next Month
nextm_day = today + relativedelta(months=1)
title_2 = "다음달(" + nextm_day.strftime('%Y-%m') + ") 일정"
df_2 = df[ (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month == nextm_day.month) ].copy()
df_2['Date'] = df_2['Date'].dt.strftime('%Y-%m-%d')

# 이후 일정
title_3 = "이후 일정"
df_3 = df[ (df['Date'].dt.year > nextm_day.year)  |  (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month > nextm_day.month) ].sort_values(by=["Date"], ascending=[True]).copy()
df_3['Date'] = df_3['Date'].dt.strftime('%Y-%m-%d')

# HTML로 변환
def gen_title(title):
  return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid black; text-align: center; }}
        th[colspan="5"] {{ text-align: center; color: red;}}
    </style>
</head>
<body>
  <table>
"""

### WOW NOT colspan 5

### WOW.240619 f-string, zip 
### f-string : {}를 사용하여 string에 변수 추가하여 만들 수 있는 가능
### zip : zip 함수를 사용하여 간결하게 표현, 리스트를 묶어서 처리
def gen_table(title, df, col_width):
  html = f"""
    <tr>
        <th colspan="5">{title}</th>
    </tr>
    <tr>
    """
### WOW.240619 f-string, zip : END

  for width, col in zip(col_width, df.columns):
    html += f'<th style="width:{width}%; border: 1px solid black;">{col}</th>\n'

  html +=  "</tr>\n"

  # 데이터 행 추가
  for row in df.itertuples(index=False):
      html += "<tr>"
      for value in row:
          html += f'<td style="border: 1px solid black;">{value}</td>'
      html += "</tr>\n"

  return html


def gen_tail():
  return f"""
  </table>
  </body>
  </html>
  """

# 열 넓이 비율
col_width = [14,5,11,40,30]  

# 타이틀 (필수)
html = gen_title(title)
# Warning (선택)
if (__istest__==True) and (os=="nt"):
  if not df[ df['Date'] < today ].empty:
    html += gen_table(title_0, df_0, col_width)
# 당월 (필수)
html += gen_table(title_1, df_1, col_width)
# 익월 (필수)
html += gen_table(title_2, df_2, col_width)
# 이후 (선택)
if (__istest__==True) and (os=="nt"):
  html += gen_table(title_3, df_3, col_width)
# 마무리 (필수)
html += gen_tail()


# HTML 내용을 파일로 저장
with open(my_desc_dir + my_desc_file, "w", encoding="utf-8") as file:
    file.write(html)



# 24.06.18 잠시 이 기능은 막습니다. tkinter로 df 표출, 변경, 저장
# 데이터프레임 GUI 화면 출력
# show_df_window( df[ (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month == nextm_day.month) ])