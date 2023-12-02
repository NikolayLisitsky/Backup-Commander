import json
from class_vk import VK
from class_yandex import Yandex

print('Введите свой vk_id:')
user_id = int(input())
VK_TOKEN = "vk1.a.ncUoMCJFJWjQIJ9s27_erbD2FRype5N6ZztAZ1aMGg3sOu3-t2lBsCE_zqA7xFAylHR49bzH9XIf8H2qyHqlp2eViltnlyDfgnGslCO3IqdMKi5xTcmMLsBnPRmnlTI4Za87gTw83Qv6StoD2AgeYfNehnEmD_Hg07V7sujwfHXP5DCJsuOP3xzxyF0zRwCYu2mHfVchV4OnnryF-zlm7w"
client = VK(VK_TOKEN, user_id)
file = client.get_photo()

print('Введите свой Яндекс токен:')
YANDEX_TOKEN = input()
client_yandex_disk = Yandex(YANDEX_TOKEN)

with open('Files\photos.json', 'w', encoding='utf-8') as f:
    json.dump(file, f, ensure_ascii=False, indent=4)

print(client_yandex_disk.upload_file())