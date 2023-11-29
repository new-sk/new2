# DB

## A01. array

### 1.1 any

a = any (배열) : 배열 속에서 특정 값이 있는지 여부를 확인

a <> all (배열) : 논리연산이라 단순하게 not이 아님

### 1.2 array -> unnest

array 풀어서 저장

### 1.3 array_cat : 두 개의 array 합침

### 1.4 string_to_array : string을 array로 변환

array_cat(string_to_array('a,b,c',','), string_to_array('d:e:f',':'))


<br>


## A02. case when then end

**case** contype **when** 'p' **then** 'PK' **when** 'u' **then** 'UK' **end** 


<br>


## A03. string_agg()

 - group by SQL문 중에서 select문에서 사용 가능함
 - string_agg(indtype || '-' || sno, ', ' **order by** indtype)

<br>


## A04. with 

with aaa as ( with절 NESTED ) select * from aaa;

with aaa as ( sql문 ), ccc as ( sql문2 ) select * from aaa, ccc;  -- 여러개도 가능


<br>


## A05. outer join

from A full outer join B on A.x = B.x
where ...


<br>


## A06. block sql

**do $$**

begin

select now();  -- select문장은 안 좋아함

end; $$;


<br>


## A07. 문자 비교 (오라클 vs PostgreSQL)

오라클 : 
- varchar2(바이트단위) : nvarchar2(문자단위)   (lengthb vs length)
- char : 스페이스를 채움

PostgreSQL :
- 문자갯수로 처리함


<br>


## A08. 한꺼번에 테이블 처리

- select * into new_table from old_table;

- insert into new_table select * from old_table;


<br>


## A09. 권한부여

- grep fl_from to fl_to;
- grant truncate on all tables in schema fl_from to tmp_user;
- alter default privileges in schema fl_from grant truncate on tables to tmp_user;


<br>


## A10. comment 

- comment on table table_name is '테이블명';
- comment on column tabnm.colnm is '컬럼명';


<br>


## B1. 디비버 리드오니

- 화면 상단 열쇄 클릭

- Connetion 정보 변경 : General - Security
  - Restrict data edit
  - Restrict structure edit

- 트랜잭션 모드
  - auto commit : 실수로 잘못 바꿀 위협
  - manual commit : 가동계 데이터 lock 발생 우려

<br>


## B2. 디비버 팀워크

- 유료버전에서만 가능 
- Network 안되는 곳에서 사용 불가


<br>


## B3. Database Tasks

- 디비버에서 작업 관리
    - 무료버전에서는 1개씩만 가능 (1개씩 여러 개 실행하면 됨)
    - Script 실행 가능 
    - import/export 실행 가능
- 표준 점검 실행(script)  -> export 실행 -> excel 업로드

<br>


## B4. 디비버 : import 

- table or script to table 가능
- 타입 정확하게 못 잡을 수 있으니깐, 사전 확인 필요
- trucate lock 주의
- (?) use bulk load
- 시작 후 진행상태 확인 가능 (오른쪽 아래에 메시지 같은 것 클릭하면 창이 뜸)


<br>


## C1. postgresql.conf

- port = 1111           # 포트번호
- max_connection = 100  # 최대 connection 수
- log_directory         # 로그 파일 위치
- log_filename          # 로그 파일 생성 규칙 (날짜)
- log_file_mode         # 0600 
- log_min_duration_statement  # 3000(3초) : Long SQL
- log_line_prefix       # 어떤 내용이 담기나
- edb_audit
- autovacuum = on
- autovacuum_freeze_max_age  (change requires restart)


<br>


## C2. DB 로그 분석 
  
### grep

- grep -n xxx 로그파일명 | grep duration

- tail -f 로그파일명 | grep 서버IP | grep -e ERROR -e FATAL, ShareLock, ExclusiveLock, deadlock, "Wait queue"
  
### findstr

- A 또는 B
  - findstr "123 456 789" > processes.log

- 특정문자열 찾기 (. 한글자, .* 여러글자)
  - findstr "duration.*" > "fl..." > output.filename

- 숫자 [0-9]{6}\.[0-9]{3} : 100초 이상 밀리초 (long sql 찾기)

### VSC 

- 찾기 (찾기 창 오른쪽에 옵션 있음 : 대소문자구분/정규식 )


<br>


## D1. 맥스게이지

- Lock 조회 후 상세화면에서 Kill 가능


<br>


## E1. 기타등등

- DB Connection Timeout
- lock 현황
  - alter table add column / truncate / index : lock 주의
- 파티션 테이블 Purge
- SEQ 초기화



