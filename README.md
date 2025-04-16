# Crawler

Python 기반 웹 크롤러 프로젝트입니다.

## 🚀 실행 방법

가상환경 생성 + 패키지 설치 + 크롤러 실행

```bash
python run.py
```

## 📁 프로젝트 구조
```
├── configs/
│   └── settings.py
├── data/ # 크롤링 데이터 임시 저장소
│   └── popply/
├── sources/  # 데이터 수집
│   └── popply_crawler.py
├── uploaders/  # 데이터 업로드
│   ├── elasticsearch_client.py
│   ├── popply_index.py
│   └── popply_uploader.py
├── base/  # 공통 베이스 클래스
│   ├── base_crawler.py
├── .venv/
├── main.py # 크롤러 실행 진입점
├── requirements.txt
├── run.py # 가상환경 자동 관리 및 실행 스크립트

```

## 📝 Commit Convention

- `feat:`     새로운 기능
- `fix:`      버그 수정
- `docs:`     문서 수정 (README 등)
- `style:`    코드 포맷팅, 세미콜론 누락 등 (기능 변경 없음)
- `refactor:` 코드 리팩토링
- `test:`     테스트 코드 관련
- `chore:`    기타 작업 (빌드, 패키지 관리 등)