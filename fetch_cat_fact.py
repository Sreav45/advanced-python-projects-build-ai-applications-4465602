import requests


def get_cat_fact():
    """Fetch a random cat fact from the catfact.ninja API."""
    url = "https://catfact.ninja/fact"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data.get("fact")


def main():
    try:
        fact = get_cat_fact()
        print(f"Random cat fact: {fact}")
    except requests.RequestException as err:
        print(f"API request failed: {err}")


if __name__ == "__main__":
    main()
