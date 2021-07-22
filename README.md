#  📝 My PhotoDiary Project

- 웹사이트 이름 : [Beans Diary]
- 설명 : LikeLion at SCH project-based session11 assignment [나만의 사진 일기장 사이트 만들기]
- 소개 : 구글 계정으로 로그인하여 자신만의 사진 일기들을 작성할 수 있는 공간

<br>

## 기능

- 일기 작성
- 작성된 일기 수정/삭제
- paginator 구현 (페이지당 3개 리스트 출력)
- Google Social Account LogIn
  - [x] 로그인 기능 구현
  - [ ] 로그인 상태에서만 개인 다이어리 열람 가능 구현 
  - [ ] 로그아웃 기능 구현
  - [ ] header menu bar 수정 필요

<br>

## UI
<details>
  <summary> Home Page </summary>
  <img width="600" alt="home1" src="https://user-images.githubusercontent.com/71310074/126589471-4cf5ba58-4296-494e-a606-d5c44331e1e7.PNG"> 
</details>

<details>
  <summary> Detail Page </summary>
  <img width="600" alt="detail" src="https://user-images.githubusercontent.com/71310074/126589479-e30f74a0-e4d0-4ea5-8aa9-b761db87d83e.PNG">
</details>

<details>
  <summary> Edit Page </summary>
  <img width="600" alt="edit" src="https://user-images.githubusercontent.com/71310074/126589484-1aa32ade-1740-4159-b2b4-bb592f0656f7.PNG">
</details>

<details>
  <summary> New-Diary Page </summary>
  <img width="600" alt="new" src="https://user-images.githubusercontent.com/71310074/126589494-6fe00684-0dcc-40a2-bff2-2691abbf39e5.PNG">
</details>

<br>

## DB UML

<img width="300" src="https://user-images.githubusercontent.com/71310074/126590718-b397aa1e-a764-4ff7-a99d-28e49e2500c1.png">

다이어리
- 일기 제목
- 날짜
- 오늘의 기분
- 오늘 날씨
- 일기 내용
- 일기 사진

<br>

## 서버 실행법

서버 주소 [localhost 주소] : 127.0.0.1:8000/

1. 가상환경 설정 (python -m venv [가상환경이름])
2. 가상환경 활성화 (. [가상환경이름]/Scripts/actiavte) - Windows용
3. django 설치 (pip install django)
4. 서버 실행 (python manage.py runserver)
5. 계정 로그인 or 생성
  - admin 계정 생성
    - python manage.py createsuperuser -> id, pw 생성
    - 127.0.0.1:8000/admin/ 에서 로그인
  - 구글 로그인
    - 상단 header bar의 로그인 버튼 클릭 후 구글 소셜 계정으로 로그인




<br>
