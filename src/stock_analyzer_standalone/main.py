
import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime


# .env 파일에서 API Key 불러오기
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

BASE_URL = "https://www.alphavantage.co/query"


def get_stock_data(symbol):
    """Alpha Vantage API에서 일별 주가 데이터를 가져온다."""

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    if "Error Message" in data:
        raise ValueError(data["Error Message"])

    if "Note" in data or "Information" in data:
        raise ValueError(
            data.get("Note") or data.get("Information")
        )

    if "Time Series (Daily)" not in data:
        raise ValueError("주가 데이터를 찾을 수 없습니다.")

    return data["Time Series (Daily)"]


def analyze_stock(time_series):
    """최근 30거래일의 주가 통계를 계산한다."""

    records = sorted(time_series.items())[-30:]

    dates = [datetime.strptime(date, "%Y-%m-%d")
             for date, values in records]

    closes = [float(values["4. close"])
              for date, values in records]

    highs = [float(values["2. high"])
             for date, values in records]

    lows = [float(values["3. low"])
            for date, values in records]

    average_close = sum(closes) / len(closes)
    highest_price = max(highs)
    lowest_price = min(lows)

    change_rate = (
        (closes[-1] - closes[0]) / closes[0]
    ) * 100

    print("\n===== 최근 30거래일 분석 =====")
    print(f"평균 종가: ${average_close:.2f}")
    print(f"최고가: ${highest_price:.2f}")
    print(f"최저가: ${lowest_price:.2f}")
    print(f"기간 변동률: {change_rate:.2f}%")

    print("\n===== 최근 7거래일 종가 =====")

    for date, close in zip(dates[-7:], closes[-7:]):
        print(f"{date.strftime('%Y-%m-%d')}: ${close:.2f}")

    return dates, closes


def draw_chart(symbol, dates, closes):
    """최근 30거래일 종가 그래프를 그린다."""

    plt.figure(figsize=(10, 5))

    plt.plot(dates, closes, marker="o")

    plt.title(f"{symbol} - Daily Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """프로그램의 시작점."""

    if not API_KEY:
        print("API Key가 없습니다. .env 파일을 확인하세요.")
        return

    symbol = input("분석할 주식 종목 코드를 입력하세요: ")
    symbol = symbol.strip().upper()

    if not symbol:
        print("종목 코드를 입력해야 합니다.")
        return

    try:
        print(f"\n{symbol} 주가 데이터를 가져오는 중입니다...")

        time_series = get_stock_data(symbol)

        if len(time_series) < 30:
            print("분석에 필요한 데이터가 30거래일보다 적습니다.")
            return

        dates, closes = analyze_stock(time_series)

        draw_chart(symbol, dates, closes)

    except requests.exceptions.RequestException as error:
        print(f"네트워크 오류: {error}")

    except (ValueError, KeyError) as error:
        print(f"데이터 처리 오류: {error}")


if __name__ == "__main__":
    main()

