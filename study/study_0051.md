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


## A11. always id 

- 자체 KEY, explict하게 사용하지 않아도 자체적으로 만들어짐, explict하게 사용하면 안됨

- 데이터 이행
  - default로 변경
  - 이행한 후에 always로 변경
  - 최종 sequence 값 설정
    - alter sequence sequence_name restart with new_start_number;


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
- (X) use bulk load (별로다. 죽는 경우가 있는데 왜 인지 확인을 못했다)
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


## C3. 프로세스 죽이기
  
### KILL

- 죽이기
  - select pg_cancel_backend(pid); -- 살살 죽이기, 현재 query만 죽이기
  - select pg_terminate_backend(pid); -- 강력하게 죽이기 (프로세스 죽이기)

- 한꺼번에 죽이기 : 특정 조건하의 모든 프로세스 죽이기 : 30분 동안 트랜잭션 중인 놈 죽이기
  - select pg_terminate_backend(pid) from pg_catalog.**pg_stat_activity**
  - where now() - query_start > '30 minutes' and client_addr::text like '10.%' and (backend_xid is not null or backend_xmin is not null)

- backend_xmin
  - 트랜잭션 중에서 현재 조회하고 있는 버전 관리 (트랜잭션 중에 유효)
  - 트랜잭션이 종료되지 않으면 이 값이 변화하지 않음 -> vacuum이 적절하게 작동하지 않음
  - 쉬고 있는 오래된 트랜잭션은 죽여줘야 겠네.


<br>


## D1. 맥스게이지

- Lock 조회 후 상세화면에서 Kill 가능


<br>


## E1. 기타등등

- DB Connection Timeout
- lock 현황
  - alter table add column / truncate / index : lock 주의
- 파티션 테이블 Purge
- Temp 영역을 사용하는 SQL
- 

