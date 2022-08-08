import json
import os
from json import JSONDecodeError
from typing import List
from configparser import ConfigParser
import requests

config = ConfigParser()
config.read(os.environ.get('FILE_CONFIG_INI'))


class ApiTrello:

    URL = config['TRELLO']['url']
    params_auth = {
        'key': config['TRELLO']['api_key'],
        'token': config['TRELLO']['api_token']
    }

    def get_last_action(self) -> dict:

        query = self.params_auth.copy()
        query['actions'] = 'commentCard'
        query['actions_limit'] = '1'

        response = requests.request(
            "GET",
            self.URL,
            params=query
        )

        try:
            response_dict: dict = json.loads(response.text)
        except JSONDecodeError:
            raise ValueError('Erro no JSON DECODER, verificar se api está bem formatada:' + response.text)

        list_actions: List[dict] = response_dict.get('actions')

        if len(list_actions) > 0:
            return list_actions[0]
        return {}




