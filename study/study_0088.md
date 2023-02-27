# Git Study : 7. 브랜치 CLI

/* 언제 브랜치 사용하나? */

새로운 기능 추가  : 안정적인 master에 추가 기능 반영

버그 수정  : 당연

병합과 리베이스 테스트  : 임시 브랜치를 만들어서 병합과 리베이스 테스트

이전 코드 개선

특정 커밋으로 돌아가고 싶을 때

 

/* git branch : 현재 브랜치 확인 */

* 찍힌 것이 현재 브랜치임

 

/* git branch branch_name : 신규 브랜치 생성 */

 

/* HEAD */

HEAD는 현재 작업 중인 브랜치의 최근 커밋을 가르킴

 

/* git checkout : HEAD 이동 */

git checkout master  # 7자리 숫자보다는 이름으로 이동해요

 

/* git merge branch_name : merge */

  - 현재 HEAD가 있는 곳에서 branch_name과 merge 하는 것임

  - Fast-forward : 단순하게 파일이 추가되는 경우로 branch_name에서 추가된 파일만 merge되는 경우

 

/* git reset --hard : 되돌리기 */

--hard : 변경된 파일들도 무시하고 이전 상태로 되돌림

checksum : 커밋 체크섬을 통해 해당 위치로 이동 (git log로 확인 가능)