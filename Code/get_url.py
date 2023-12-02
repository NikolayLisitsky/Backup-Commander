APP_ID = '51799989'
OUATH_BASE_URL = 'https://oauth.vk.com/authorize'
params = {
    'client_id' : APP_ID,
    'redirect_uri' : 'https://oauth.vk.com/blank.html',
    'display' : 'page',
    'scope' : 'photos, offline', 
    'response_type' : 'token'
}

from urllib.parse import urlencode
oath_url = f"{OUATH_BASE_URL}?{urlencode(params)}"
print(f"1) Пройдите по ссылке - {oath_url}\n2) Дайте доступ к своим фото")
print(f'3) Вставьте ссылку из адресной строки сюда')
input_url = str(input())
TOKEN = input_url.split('=')[1][:-11]
print(f"\nВаш токен - {TOKEN}")
print(f"\nВаш id - {input_url.split('=')[-1]}\n")