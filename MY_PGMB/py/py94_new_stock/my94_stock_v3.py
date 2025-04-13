import my94_stock_naver as c94s

my94 = c94s.cMy94Stock()

# 실제 작업은 다 막아
my94.get_stocks()
my94.xyz(['2025.04.11'])

# 목표가 확인
# my94.ssStdAmt()
my94.ssStdAmt2()
