# 5-3. 논리 데이터 모델링

<p> <a href="./study_dasp.html">DASP</a> </p>

**<p> 5. 데이터 모델링</p>**
<p> <a href="./study_0108.html">0108. 5-1. 데이터 모델링 이해</a> </p>
<p> <a href="./study_0109.html">0109. 5-2. 개념 데이터 모델링</a> </p>
<p> <a href="./study_0110.html">0110. 5-3. 논리 데이터 모델링</a> </p>
<p> <a href="./study_0111.html">0111. 5-4. 물리 데이터 모델링</a> </p>

<br>

### **가. 논리 데이터 모델링 이해** 

데이터 모델링이 최종적으로 완료된 상태

목적 및 효과
- 해당 비즈니스에 대한 데이터 관점에서의 명확한 이해
- 전사적인 통합 데이터 체계 확립
- 데이터의 일관성 및 정확성 유지를 위한 규칙 도출
- 안정적인 데이터베이스 설계의 토대 마련
- 사용자의 명확한 의사소통을 위한 수단으로 활용

필수 성공 요소
- 업무에 능통한 현업 사용자와 함께 데이터 모델링을 진행하라
- 절차보다는 데이터에 초점을 두고 모델링을 진행하라
- 데이터의 구조와 무결성을 함께 고려하라
- 개념화와 정규화 기법을 적용하라
- 가능하면 다이어그램을 이용하여 업무를 표현하라

<br>


### **나. 속성 정의** 

속성 정의한 후에 엔터티 상세화할 꺼예요

<br>

모든 인스턴스가 공통으로 가지고 있는 특성

속성 특징
- 속성의 어원적 의미 : 남의 도움을 받지 않더라도 자가만의 독자적인 성질 가짐
- 속성도 일종의 집합이다 : 속성값 집합
- 릴레이션십도 속성이다 : FK 형태로 나타날 수 있음
- 속성들 간은 서로 독립적이다 (식별자에 종속됨, 속성들 간의 종속 : 별도 분리 : 제3정규형)

속성 후보 도출
- 수집처 : 구시스템 문서, 현업장표/보고서, 사용자협의, DFD의 DD, 전문서적, 다른 시스템
- 선정원칙 : 버리지마라, 소그룹별로 후보군을 만들고 가장 근접한 엔터티에 할당
- 구성요소 : 속성명(명칭 어떻게 할까요), 도메인(도메인 가지나요), 선택성(꼭 값을 가지나요)

속성 검증 및  확정 (요구사항에 맞게 적용)
- 최소(atom) 단위까지 분할 : 분할 및 통합의 기준은 업무의 요구사항에 따른다
- 하나의 값만을 가지는지 검증(single value) : 차량 계약일 (여러 번 계약 가능), 차량번호(굳이 2대 이상 관리할 필요 없음)
- 추출 속성인지 검증 : 최초정보, 최종정보, 집계정보(합계금액), 릴레이션정보, 다른속성의일부
- 보다 상세하게 관리할 것인가

가공 속성 규칙
- 도출 또는 계산에 사용된 기준 속성(base attribute)
- 초기에는 가공속성을 중복으로 파악했으나, 요즘은,,,

속성 정의 시 유의 사항
- 의미가 명확한 속성 명칭 부여
- 유일한 복합명사 사용
- 순번(좀 더 명확하게), 상태(무슨 상태?), 보험기간(년?, 월?), 초회납방(말이 어렵잖아), 작의적인 전용 금지(ERP 전용 용도 속성 사전에 만들어져 있음^^)

<br>


### **다. 엔터티 상세화** 

속성 정의했으나 엔터티 상세화할 꺼예요

<br>

식별자 확정
- 본질 식별자
- 후보 식별자
- 대체(보조) 식별자
- 인조 식별자
- 식별자 확정

정규화
- 변경 이상으로부터 데이터 보호 (Modification = Insertion, Update, Deletion)
- 정규화 장점
  - 중복값 줄어듦, NULL 줄어듦, 복잡한코드해결, 새로운요구사항발견, 업무규칙포착, 데이터구조안정성
- 1차정규형 (1NF) : 하나의 속성이 여러 개의 값을 가진 경우 : 해당 속성 분리
- 2차정규형 : **식별자** 전체에 완전 종속 되어야 함 : 일부 종속 내역
- 3차정규형 : 식별자를 제외한 나머지 속성들 사이에서의 종속성
- BCNF정규형 : 모든 결정자가 키 (복합후보키가 2개, 1개 이상 공유, 1개 이상 일반 속성 가짐, 하나가 삭제될 경우 다른 후보키의 정보다 사람짐)

M:N 관계 해소
- 모델링이 덜 된 관계로 1:M 관계 2개로 정의함

참조 무결성 규칙 정의
- 입력 : dependent(있는 경우만), automatioc(무조건 삽입), nullify(to null), default(to default), customized(특정조건만족할경우만), no effect
- 삭제 : restrict(제한), cascade(다삭제), nullify, deault, cutomized, no effect
  
<br>


### **라. 이력 관리 정의** 

선분 이력관리를 해 보아요

<br>

이력 관리 대상 선정
- 종류 : 발생 이력(웹사이트 접근이력), 변경 이력(변경시마다), 진행 이력(주문상태)
- 관리형태 : 시점이력(매일첫번째고시환율), 선분이력
- 선분이력관리유형 
  - 인스턴스 : 스냅샷관리, 저장공간낭비, 찾기어려움 
  - 속성 : 매우 분명하게 관리됨, 변화 가능성 낮고 항목 많을 때 유리
  - 주제 : 연동될 확률이 높은 것별로 인스턴스 레벨 관리, 
  
선분 이력 관리용 식별자 확정
- 성능고려하여 설계 필요
- 점으로 처리시 유니크함 보존 힘듦 : 부서코드+시작일+종료일
- 종료점이 NULL 처리시 속도 저하 우려, 최대치로 처리함