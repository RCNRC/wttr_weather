import requests

def get_resonse(url, payload):
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        print(response.text)
    except Exception:
        print("Response error")


url = 'https://wttr.in/'
places = ['london', 'svo', 'Cherepovets']
payload = {"m":"", "M":"", "n":"", "T":"", "q":"", "lang":"ru"}
for place in places:
    get_resonse(url+place, payload)