# 파이썬 

[파이썬 학습내역](file/PY.zip)

[파이썬 교재](file/파이썬강사.tar)

<br>

파이썬 3.6.5(18.03.26) 32bit 설치용 다운로드 설치 : add python path 체크 했음 : 32비트 / 64비트 확인 꼭
파이참(pycharm) 설치

print('hello python')

### 자료형
- 숫자형
  - 정수
  - 실수 : 1.2, 4.2e-10 (e 또는 E, 10진수임)
  - 8진수 : 0o (o 또는 O)
  - 16진수 : 0x (x 또는 X)
  - 사칙연산(산술연산자)
    - 4칙연산(+,-,*,/), **(지수), //(몫), %(나머지)
- 문자열
  - 큰따옴표, 작은따옴표 외에 큰따옴표3개, 작은따옴표3개로도 가능
  - "Python's favorite food is perl"
  - 'Python\'s favorite food is perl'
  - 이스케이프 코드 : n, t, \, ', ", r, f, a, b, 000
  - 연산 (+,*) : *는 반복횟수 print("="*10)
  - 인덱싱
  - 슬라이싱
  - 포맷팅
- 리스트
- 튜플
- 딕셔너리
- 집합
- 불린
- 자료형의 값을 저장하는 공간, 변수

함수와 데이터(변수)

연산자 : 산술, 관계, 논리

관계연산자 : >, >=, <, <=, ==, !=

논리연산자 : and or not (단어로 표시됨)

파이썬 들여쓰기 중요하게 생각함 (첫번째 컬럼부터 적어야만 함 -> 그렇지않으면, Error 발생시킴)

들여쓰기 내역으로 같은 레벨의 문장인지 여부 판단

<br>

### 제어문
조건문 : if, else, elif

if a :

    print("홀수")

else:

    print("짝수")

함수 : def, return, 여러개 return 가능 (할당자)

def f(a,b) :

    return b,a

a,b = f(a,b)

라이브러리 설치 : requests
 - File - Settings   -->  Project - Project Interpreter  --> 초록색 플러스 버튼  --> requests 입력 --> Install Package

Loop

for i in range(5):

while True:

    break

collection : list, tuple, set, dictionary

              []    ()     {}    {}

tuple : read only (list의 상수형 버전)

d = { "name":"hoon", "age":20}  # 표현법 1

d = dict(name="hoon", age=20)   # 표현법 2

JSON 형태로 데이터 송수신 : (텍스트)

file 처리 : C함수 유사


#파일 쪼개서 관리할 때 유용한 코드

if __name__ == "__main__":


import csv

함수 정의 : positional, keyword

class

import sqlite3 : 파일형 DB

flask : 간단한 웹서비스

slicing