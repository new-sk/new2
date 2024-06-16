# 보완 필요사항
# 1. LUNAR
# 2. 1회성 이벤트
# 3. 소스 별도 보관 : 소스, 인풋, 아웃풋
# 4. 실적 파일 별도 관리 (아웃품과 또 다른)

__istest__ = True

import os
import sys
my_dir, my_file = os.path.split(__file__)

os = os.name

if os != "nt" and (not __istest__):
  print("Not Allowed : Real Mode")
  sys.exit()

from datetime import datetime
from dateutil.relativedelta import relativedelta  # 윤년 고려

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

# # 세번째 주간
# dfw3 = dfw2.copy()
# dfw3['Date'] = dfw3.apply(update_week, axis=1) # 각 행별로 날짜 변경
# dfw3['CycleMemo'] = 'Next ' + dfw3['Num'].astype(str) + ' Week(s)'


print("Weekly Plan")
#dfw = pd.concat([dfw,dfw2,dfw3,dfw4,dfw5])
dfw = pd.concat([dfw,dfw2])
print(dfw)


### TOTAL
df = pd.concat([dfy,dfm,dfw])
df = df.sort_values("Date")
df = df.reset_index(drop=True)   # re-index
print("Total Plan")
print(df)

# 현재 모드 출력 : Test & Not Test
if __istest__ :
  current_mode_print = "Test Mode"
  fn_output = ""
else :
  current_mode_print = "Real Mode"


with open(my_dir + '/my_schedule_output.txt', 'w', encoding='utf-8') as f:
  print("-"*50, file=f)
  print(current_mode_print, file=f)
  print("-"*50, file=f)
  

# Only Test Mode : (WARNING) 오늘 이전날짜 계획이 있는가? 
if __istest__ :
  if not df[ df['Date'] < today ].empty:
    with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
      print("WARNING", file=f)
      print( df[ df['Date'] < today ], file=f)
      print("-"*50, file=f)

# This Month
with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
  print ("이번달(" + today.strftime('%Y-%m') + ") 일정", file=f)
  print( df[ (df['Date'].dt.year == today.year) & (df['Date'].dt.month == today.month) ], file=f)
  print("-"*50, file=f)

# Next Month
with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
  nextm_day = today + relativedelta(months=1)
  print ("다음달(" + nextm_day.strftime('%Y-%m') + ") 일정", file=f)
  print( df[ (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month == nextm_day.month) ], file=f)
  print("-"*50, file=f)

# Only Test Mode : 이건 잠시만 막는거야...
if __istest__ :
  with open(my_dir + '/my_schedule_output.txt', 'a', encoding='utf-8') as f:
    print("-"*50, file=f)
    print("이후 일정", file=f)
    print( df[ (df['Date'].dt.year > nextm_day.year)  |  (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month > nextm_day.month) ].sort_values(by=["Cycle","Date"], ascending=[False,True]), file=f)
    print("-"*50, file=f)


# 데이터프레임 생성
dftk = pd.DataFrame({
    "Name": ["John", "Jane", "Jim"],
    "Age": [32, 28, 42],
    "City": ["New York", "London", "Paris"]
})

# 데이터프레임 GUI 화면 출력
show_df_window( df[ (df['Date'].dt.year == nextm_day.year) & (df['Date'].dt.month == nextm_day.month) ])