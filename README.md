# HoonLog - 개인 Blog

### 요약
##### Django를 활용한 개인 블로그 만들기  

### 주요모듈정리
```json
  "django": "^3.1.7",
  "django-allauth": "^0.44.0",
  "django-markdownx": "^3.0.1",
  "django-extensions": "^3.1.3"
```

### 주요기능
1. 로그인 / 로그아웃
- django-allauth를 통해 내장된 Authenticate 기능을 활용.
2. 게시물 입력
- Model(Post)을 만들고 GenericView를 활용한 CRUD 기능 생성.
- markdownx, crispy_forms를 활용한 POST입력 
3. 댓글 구현 (대댓글 X)
- Model(Comment)를 만들고 GenericView를 활용한 CRUD기능 생성.
4. Pagination
5. Tagging
- Model(Tag)를 활용.

### 추후 업데이트 요소
1. Docker 입히기
2. AWS 배포하기
