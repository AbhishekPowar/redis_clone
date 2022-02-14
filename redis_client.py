import requests
import json

class Redis_client():
    def __init__(self, host:str, port:int, index:str = 'index') -> None:
        self.host = host
        self.port = port
        self.index = index
        self.base_url = f'{self.host}:{self.port}/{self.index}/'

    def set(self, key, value):
        data = {'key' : key, 'value': value}
        params = {}

        response = requests.post(url=self.base_url , params=params, json=data)
        if response.status_code in [200]:
            return response.json().get('status', False)
        return False

    def get(self, key):
        url = self.base_url + f'get/{key}' 
        response = requests.get(url=url)

        value = None
        if response.status_code in [200]:
            value = response.json().get('value')
            return value
        return value

    def get_all(self):
        url = self.base_url + f'get_all' 
        response = requests.get(url=url)

        value = None
        if response.status_code in [200]:
            value = response.json().get('value')
            return value
        return value

    def remove(self, key):
        url = self.base_url + f'remove/{key}' 
        response = requests.get(url=url)
        
        value = None
        if response.status_code in [200]:
            value = response.json().get('value')
            return value
        return value
