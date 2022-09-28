import requests


def main() -> None:
    url = 'https://wttr.in/'
    places = ['london', 'svo', 'Cherepovets']
    payload = {'m': '', 'M': '', 'n': '', 'T': '', 'q': '', 'lang': 'ru'}
    for place in places:
        response = requests.get(f"{url}{place}", params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
