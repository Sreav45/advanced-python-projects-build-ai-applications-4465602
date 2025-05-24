import requests


def get_price(symbol="BTCUSDT"):
    """Fetch the latest price for a given symbol from Binance."""
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data.get("price")


def main():
    symbol = "BTCUSDT"
    try:
        price = get_price(symbol)
        print(f"Current price of {symbol}: {price}")
    except requests.RequestException as err:
        print(f"API request failed: {err}")


if __name__ == "__main__":
    main()
