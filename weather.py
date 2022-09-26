"""Print weather of London, svo and Cherepovets"""
from urllib.error import HTTPError
import requests


def print_response(url, payload):
    """Prints response from http request GET to website url with payload params"""
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


def main() -> None:
    """Main method"""
    url = 'https://wttr.in/'
    places = ['london', 'svo', 'Cherepovets']
    payload = {'m': '', 'M': '', 'n': '', 'T': '', 'q': '', 'lang': 'ru'}
    for place in places:
        try:
            print_response(f"{url}{place}", payload)
        except HTTPError:
            print("HTTPError occure")


if __name__ == '__main__':
    main()
