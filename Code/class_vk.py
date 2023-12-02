import requests

class VK:
    '''
    Функции:
    1) Функция get_photo получает фотографии с VK
    2) Функция get_all_photos все фотографии с VK
    '''
    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, access_token, user_id, version='5.131'):
      self.token = access_token
      self.id = user_id
      self.version = version
      self.params = {'access_token': self.token,
                    'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        self.params.update({'user_id' : self.id})
        response = requests.get(url, params=self.params)
        return response.json()
    

    def get_status(self):
        self.params.update({'user_id' : self.id})
        response = requests.get(f'{self.API_BASE_URL}/status.get', params=self.params)
        return response.json()['response']['text']
    

    def set_status(self, new_status):
        self.params.update({'user_id' : self.id, 'text' : new_status})
        response = requests.get(f'{self.API_BASE_URL}/status.set', params=self.params)
        response.raise_for_status()


    def replace_status(self, target, replace_str):
        status = self.get_status()
        new_status = status.replace(target, replace_str)
        self.set_status(new_status)


    def get_photo(self):
        self.params.update({'owner_id' : self.id, 'album_id': 'wall', 'extended':1, 'count': 1000})
        response = requests.get(f'{self.API_BASE_URL}/photos.get', params=self.params)
        return response.json()
    
    def get_all_photos(self): # Дополнительная функция, которая позволяет взять фото не только с профился пользователя, но и с его фотографий вне профиля
        self.params.update({'owner_id' : self.id, 'extended':1, 'count': 200}) # Максимальное кол-во фото - 200. Больше не позволяет метод photos.getAll
        response = requests.get(f'{self.API_BASE_URL}/photos.getAll', params=self.params)
        return response.json()