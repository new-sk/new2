# Git Study : 6. 기본 명령어 CLI

/* git bash로 해요 */

bash로 실행합니다

  - 유닉스 명령어 습득 : pwd, ls -a, cd, mkdir, echo

 

/* git status : 현재 디렉토리 git 상태 확인 */

fatal: not a git repository (or any of the parent directories): .git

  --> git을 만든적이 없네요.

On branch master
nothing to commit, working tree clean

  --> 정상 상태

 

/* git init : git 저장소 생성 */

Initialized empty Git repository in ...

  -->git 정상 생성

Reinitialized existing Git repository in

  --> 

 

/* git config : 설정값 지정 */

git config  --list   # 현재 config 설정값 보임

editor 변경 가능 : 디폴트로 vim

 

/* git add : 파일 추가  (git reset 추가된 파일 제거) */

### untracked file이 있어요. (git add 수행전)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        HTML_001.html

### commit가 필요한 파일이 있어요 (git add 수행후)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   HTML_001.html

 

/* git commit : add된 파일 커밋 */

vim 등 editor가 뜸 / 그냥 닫으면 안되고 아래 내역 작성해야 함

첫줄 : 작업 요약

둘째줄 : 빈 칸

셋째줄 : 상세 작업 내역

 

이후에 git status하면 깨끗한 상태로 보임 (staging 영역에 아무것도 없음)ㅡㅁ

 

/* git log : commit log 내역 확인 */

git log

git log -n2   : 최신 2개 보여줌

git log -oneline  : 1줄로 요약해서 보여줌

git log --graph  : 그래프 형식

git log --oneline --graph --decorate --all

 

/* git help : 도움말 */

브라우저에서 로컬에 있는 도움말이 영어로 열림 ^^

 

/* remote : remote repository 연결 */

git remote add origin URL (https://github.com/)    # github URL

git remote -v      # 연결된 내역 확인

 

/* git push : 원격저장소로 저장 */

git push [-u] [원격저장소별명] [브랜치이름]

  --> (HEAD -> master, origin/master)  # (gihub의 마스터 브랜치인) 새로운 브랜치가 생긴 것을 확인할 수 있습니다.

Everything up-to-date  # 모든 것이 최신일 경우에

[-u] 옵션 사용하면 이후에는 git push 이후의 내역 없이도 자동으로 처리됨

 

/* git pull : 원격저장소 변경사항 반영 (fetch + merge) */

 

/* git clone */  # 맥에서 합시당 p239

 

/* git commit -a : 몰라요 */

 

 

/* git fetch : 원격저장소의 브랜치와 커밋들을 로컬저장소로 동기화 */

 

/* git merge */ commit