import os

import requests
from configparser import ConfigParser

config = ConfigParser()
config.read(os.environ.get('FILE_CONFIG_INI'))


def send_message_telegram_bot_api(message: str) -> dict:
    schema = config['TELEGRAM']['schema']
    host = config['TELEGRAM']['host']
    bot_token = config['TELEGRAM']['bot_token']
    bot_chat_id = config['TELEGRAM']['bot_chat_id']

    full_url = f'{schema}://{host}/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={message}'
    send_text = full_url
    response = requests.get(send_text)

    return response.json()


def format_message_for_trello_updates(action: dict) -> str:
    message = [
        'Atualização do Trello'.upper(),
        '',
        f'Nome %3A {action.get("memberCreator").get("fullName")}',
        f'Quadro %3A {action.get("data").get("board").get("name")}',
        f'Cartão %3A {action.get("data").get("card").get("name")}',
        f'Link %3A https://trello.com/b/SsLK6cGM/agile-scrum'
    ]

    message = "%0D%0A".join(message)
    return message
