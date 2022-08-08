import os
from time import sleep
from configparser import ConfigParser
import config

config.set_file_config('config.ini')
config.settings_env()

from src.api.api_trello import ApiTrello
from src.api.api_telegram import send_message_telegram_bot_api, format_message_for_trello_updates
from src.state_manager import StateManager

config_p = ConfigParser()
config_p.read(os.environ.get('FILE_CONFIG_INI'))

if __name__ == '__main__':

    # SEND FIRST LAST UPDATE
    last_update_trello = ApiTrello().get_last_action()
    message = format_message_for_trello_updates(action=last_update_trello)
    send: dict = send_message_telegram_bot_api(message=message)
    print('send message:', send.get('ok'))

    manager = StateManager(new=last_update_trello)
    manager.set_next_state()

    # CHECK NEW UPDATE (LAST != NEW)
    while True:
        last_update_trello = ApiTrello().get_last_action()
        manager.new = last_update_trello

        if manager.is_diff():
            message = format_message_for_trello_updates(action=last_update_trello)
            send: dict = send_message_telegram_bot_api(message=message)
            print('send message:', send.get('ok'))

            manager.set_next_state()

        sleep(float(config_p['SYSTEM']['update_delay_sec']))
