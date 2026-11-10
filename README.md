# codyssey-python-quiz
# Codyssey Python Quiz

## 1. 프로젝트 개요
Python 기초 문법과 객체지향 프로그래밍을 활용한
터미널 기반 퀴즈 게임입니다.

## 2. 퀴즈 주제
Python 프로그래밍 기초

### 선정 이유
Python 문법을 퀴즈로 복습하며 프로그래밍 개념을
체계적으로 학습하기 위해 선정했습니다.

## 3. 개발 환경
- Python 3.10 이상
- Visual Studio Code
- Git / GitHub
- 외부 라이브러리 사용 없음

## 4. 실행 방법
```bash
py main.py
```

## 5. 기능 목록
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- 프로그램 종료

현재 기본 메뉴와 입력 검증 기능 구현 완료.
나머지 기능은 개발 예정입니다.

## 6. 파일 구조
- main.py : 프로그램 시작 및 메뉴
- quiz.py : 개별 퀴즈 관리 (예정)
- quiz_game.py : 게임 전체 관리 (예정)
- state.json : 퀴즈와 점수 저장 (예정)

## 7. 데이터 파일
state.json은 프로젝트 루트에 UTF-8로 저장합니다.

예정 스키마:
- quizzes : 문제 목록
- best_score : 최고 점수
```
