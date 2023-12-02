import json
from datetime import *
import requests

class Yandex:
    '''
    Функции:
    1) Функция upload_file выгружает из файла photos.json фотографии на Я.Диск.
    '''

    def __init__(self, access_token):
      self.token = access_token

    def upload_file(self, count_uploaded_images=5):
        with open("Files/photos.json", 'r', encoding='utf-8') as file:
            file = json.load(file)
            if 'error' in file:
                return '\nПроизошла Ошибка. Мы не смогли совершить резервное копирование'
            if file['response']['count'] == 0:
                return '\nУ вас нет фото для резервного копирования'
            file_photos = file['response']['items']
            photo_list = []
            for file_item in file_photos:

                file_sizes = file_item['sizes']
                max_size = {'height' : 0, 'width' : 0, 'url' : '', 'size': '', 'date' : file_item['date']}
                for file_size in file_sizes:
                    if file_size['height'] > max_size['height'] and max_size['width'] < file_size['width']:
                        max_size['height'] = file_size['height']
                        max_size['width'] = file_size['width']
                        max_size['url'] = file_size['url']
                        max_size['size'] = f"{file_size['height']}/{file_size['width']}"
                photo_list.append([{"likes": f"{file_item['likes']['count']}",
                                    "size" : max_size['size'],
                                    'date': max_size['date'],
                                    'url': max_size['url']}])
            final_dict = []
            file_name_list = set()
            print(len(photo_list))
            if len(photo_list) < count_uploaded_images and count_uploaded_images != 5:
                    return 'Вы ввели слишком большоое кол-во фото.'
            elif len(photo_list) < count_uploaded_images:
                count_uploaded_images = len(photo_list)
            for element in range(0, count_uploaded_images):
                element = photo_list[element]
                base_url = "https://cloud-api.yandex.net/v1/disk"

                if f"{element[0]['likes']}.jpg" not in file_name_list:
                    final_dict.append({"file_name": f"{element[0]['likes']}.jpg", 
                                    "size" : element[0]['size']})
                    file_name_list.add(f"{element[0]['likes']}.jpg")
                    params = {"path": f"Новая папка/{element[0]['likes']}.jpg",
                            "url": {element[0]['url']}}
                    header = {"Authorization": self.token}
                    requests.post(f"{base_url}/resources/upload", headers=header, params=params)
                
                else:
                    elem_date = str(datetime.fromtimestamp(element[0]['date'])).replace(':', '|')
                    final_dict.append({"file_name": f"{elem_date}.jpg",
                                        "size" : element[0]['size']})
                    file_name_list.add(f"{elem_date}.jpg")
                    params = {"path": f"Новая папка/{elem_date}.jpg",
                            "url": {element[0]['url']}}
                    header = {"Authorization": self.token}
                    requests.post(f"{base_url}/resources/upload", headers=header, params=params)
                        
                        
            with open('Files/upload_photos.json', 'w', encoding='utf-8') as file: # Запись данных в файл
                json.dump(final_dict, file, ensure_ascii=True, indent=4)
                return '\nFinished'