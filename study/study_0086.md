# Git Study : 1. ~ (작성중)

## 1. GUI 환경설정

### 1.1 소스트리

○ 사용하기 싫어요

### 1.2 비주얼 스튜디오 코드 (VSC)

○ 이쪽으로 가세요.

### 1.3 Github 둘러보기

상단 : 

  - Pull requests : 관련된 모든 pull request 보여줌

  - Issues : 해결해야 할 과제 

  - Maketplace : 플러그인 구입

  - Explore : 관련된 블로그 등

  - Notifications : 알림

  - New : 새로운 리파지토리 등을 만들 때

  - Sign : sign-in, out, 설정

왼쪽 :

  - Repositories : 저장소 목록

  - Recent activity : 팔로우 저장소 활동 내역

  ※ 팀관련 정보 : 대시보드 컨텍스트(표시 기준), 팀 목록(단체 계정 안의 작은 팀)

<br> 

## 2. 혼자서 Git으로 버전 관리하기

2.1 로컬저장소를 소스트리에 불러오기  

2.2 소스트리로 커밋 만들고 푸시하기  (넘어갑니다)

○ 사용하기 싫어요

2.3 그림으로 Git 뜯어보기 

라이프 싸이클

(untracked)    (tracked)               

                  Working Area  ->  Staging Area  ->  Repository Area

                   (modified)                (staged)             (unmodified)

                                 git add                 git commit

                                 git status              git log

 

## 3. 여러 명이 함께 Git으로 협업하기

### 3.1 원격저장소에서 협업하기 : 브랜치(Branch)

가장 기본이 되는 브랜치 : master

HEAD를 이용해서 브랜치 사이를 마음대로 넘나들 수 있음

feature/기능이름

merge : 두 브랜치를 합치는 것

  - fast forward (한 쪽만 수정이 이루어진 경우)

  - conflict (동시에 수정한 경우 : 충돌난 파일만 어느 것으로 할지 수동으로 선택하면 됨)

    -- git status (충돌난 파일 확인) --> 선택한 파일 add 후 commit