import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


def telegram_bot_message(message):
    schema = config['TELEGRAM']['schema']
    host = config['TELEGRAM']['host']
    bot_token = config['TELEGRAM']['bot_token']
    bot_chat_id = config['TELEGRAM']['bot_chat_id']

    full_url = f'{schema}://{host}/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={message}'
    send_text = full_url
    response = requests.get(send_text)

    return response.json()
