# Stock Analyzer

## 1. 프로젝트 소개

Alpha Vantage API를 활용하여 실제 주식 데이터를 수집하고 분석하는 파이썬 프로그램입니다.

사용자가 주식 종목 코드를 입력하면 일별 주가 데이터를 가져와 최근 주가 변화와 통계 정보를 제공합니다.

## 2. 주요 기능

- 주식 종목 코드 검색
- 최근 7거래일 주가 조회
- 최근 30거래일 주가 분석
- 평균 종가 계산
- 최고가 및 최저가 계산
- 주가 변동률 계산
- 주가 그래프 시각화

## 3. 사용 기술

- Python
- UV
- Alpha Vantage API
- Requests
- Python-dotenv
- Matplotlib

## 4. 설치 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```powershell
uv sync
```

## 5. API Key 설정

프로젝트 최상위 폴더에 `.env` 파일을 생성합니다.

다음 형식으로 API Key를 입력합니다.

```text
ALPHA_VANTAGE_API_KEY=발급받은_API_KEY
```

API Key는 GitHub에 업로드하지 않습니다.

## 6. 실행 방법

```powershell
uv run python main.py
```

## 7. 주요 함수 설명

- `get_stock_data()`: API를 통해 주식 데이터를 요청합니다.
- `organize_data()`: JSON 데이터를 분석하기 쉬운 형태로 정리합니다.
- `show_weekly_data()`: 최근 7거래일 종가를 출력합니다.
- `analyze_stock()`: 최근 30거래일 주가 통계를 계산합니다.
- `show_graph()`: 주가 변화를 그래프로 표현합니다.
- `main()`: 전체 프로그램의 실행과 메뉴를 관리합니다.

## 8. 주의사항

본 프로그램은 Alpha Vantage의 일별 주가 데이터를 사용합니다. 실시간 주가를 제공하는 프로그램이 아니며, 투자 판단이나 매매 추천을 목적으로 하지 않습니다.