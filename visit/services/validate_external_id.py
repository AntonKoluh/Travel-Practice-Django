from functools import lru_cache
import requests


@lru_cache(maxsize=256)
def check_external_api(artwork_id):
    url = f"https://api.artic.edu/api/v1/artworks/{artwork_id}"

    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        return False, "Request failed"

    if response.status_code != 200:
        return False, f"Bad status code: {response.status_code}"

    try:
        data = response.json()
    except ValueError:
        return False, "Invalid JSON"

    return True, data
