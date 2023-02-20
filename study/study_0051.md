# DB

## 1. array

### 1.1 any

a = any (배열) : 배열 속에서 특정 값이 있는지 여부를 확인

a <> all (배열) : 논리연산이라 단순하게 not이 아님

### 1.2 array -> unnest

array 풀어서 저장

### 1.3 array_cat : 두 개의 array 합침

### 1.4 string_to_array : string을 array로 변환

array_cat(string_to_array('a,b,c',','), string_to_array('d:e:f',':'))

<br>

## 2. case when then end

**case** contype **when** 'p' **then** 'PK' **when** 'u' **then** 'UK' **end** 

<br>

## 3. string_agg()

group by SQL문 중에서 select문에서 사용 가능함

<br>

## 4. with 

with aaa as ( with절 NESTED ) select * from aaa;

with aaa as ( sql문 ), ccc as ( sql문2 ) select * from aaa, ccc;  -- 여러개도 가능

<br>

## 5. outer join

<br>

## 6. block sql

**do $$**

begin

select now();  -- select문장은 안 좋아함

end; $$;

<br>

## 7. 디비버 리드오니

화면 상단 열쇄 클릭

<br>


## 8. 디비버 팀워크

Network 안되는 곳에서 사용 불가



