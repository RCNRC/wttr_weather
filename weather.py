'''
Скрипт запрашивает прогноз погоды с сайта https://wttr.in/.
Скрипт не обрабатывает переданные ему парметры.
'''
import requests


def main() -> None:
    '''
    По уже установленным адрессам и набору параметров отправляются 3 запрроса GET.
    Если запрос был удачным, то выводится текст ответа, иначе текст ошибки.
    '''
    url = 'https://wttr.in/'
    places = ['london', 'svo', 'Cherepovets']
    payload = {'m': '', 'M': '', 'n': '', 'T': '', 'q': '', 'lang': 'ru'}
    for place in places:
        response = requests.get(f"{url}{place}", params=payload)
        if response.ok:
            print(response.text)
        else:
            print(response.raise_for_status())


if __name__ == '__main__':
    main()
