# Git Study : 0.빠른 실습

## Git 이란, github 가입 

버전관리

Git을 통하여 협업 수행

인터넷을 통한 버전관리 : Git 호스팅 서비스 : 대표적인 사이트 github

Github에 올려두면 시간, 공간의 제약없이 협업이 가능해짐

가입절차 : 일반적인 가입이랑 유사, Free로 설치, 메일주소로 메일 보내고 인증코드 입력해야지 완료

<br><br> 

## 로컬 Git 설치 

로컬 git 설치 (2.33.0(2)  21.8.24) : 묻는 것 열나게 많다. 일단 다 디폴트로 설치

  - bash로 실행합니다 (유닉스 명령셀), cmd(원도우), gui(간단 gui)

git bash Here   (윈도우 탐색기)     /    커맨드 창에서는 폴더로 이동후

git init    (git 초기화, 지금부터 로컬저장소가 만들어져서 버전관리가 가능해짐)

  --> Initialized empty Git repository in D:/iTshirt-cat/.git/

  --> .git 라는 폴더가 생성됨  (ls -al 로 확인)

 
<br><br> 

## 첫 커밋,  두번째 커밋 

git config -global user.email "email"   -- 작성자 정보 남김

git config -global user.name "name" 

git add README.txt   -- 파일 추가

git commit -m "Readme 파일 추가"   -- 커밋을 하면서 comment 작성

  --> 1 file changed, 1 insertion(+)    -- 정상 수행 결과

  --> 1 file changed, 1 insertion(+), 1 deletion(-)   -- 기존 파일 변경후 다시 하니깐, 이렇게 나오네요

-- 이름 입력안하고 commit 하니깐, "Author identity unknown, *** Please tell me who you are."

 
<br><br> 

## 다른 커밋으로 이동 

git log    -- 커밋 내역 확인 (앞의 7자리 커밋 아이디, 설명 확인)

git checkout 7자리   -- 커밋 이동

git checkout -         -- 최신 커밋으로 이동, 숫자로 적어도 되지만 "-"

 
<br><br> 

## github push : 로컬 -> github

New Repository 생성   -- 다른 사람 보는 것 선택 (public vs private)

git remote add origin "https://github.com/name/iTshirt.git"  -- github와 연결  "는 빼고 작성해 주세요.

git push origin master   -- 로컬 -> github로 전송 

 
<br><br> 

## clone 

원격저장소의 코드와 버전 전체를 내 컴퓨터로 내려 받는 것  <--> [download zip]이랑은 다름

git clone "https://github.com/name/iTshirt.git"  .    -- 점은 현재 폴더에 생성,   아니면 iTshirt 폴더 만들어서 생성됨  

 

/* github pull : github -> 로컬 */

git pull origin master

