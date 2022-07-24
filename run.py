from time import sleep
from api_trello import ApiTrello, get_details_message
from bot_telegram import telegram_bot_message
from state_manager import StateManager
import config

config.settings_env()
INTERVAL_CHECK_SECONDS = 1

if __name__ == '__main__':

    last_update_trello = ApiTrello().get_last_action()
    message = get_details_message(action=last_update_trello)
    send: dict = telegram_bot_message(message=message)
    print('send message:', send.get('ok'))

    manager = StateManager(actual={}, new=last_update_trello)
    manager.set_next_state()

    while True:
        last_update_trello = ApiTrello().get_last_action()
        manager.new = last_update_trello

        if manager.is_diff():
            message = get_details_message(action=last_update_trello)
            send: dict = telegram_bot_message(message=message)
            print('send message:', send.get('ok'))

            manager.set_next_state()

        sleep(INTERVAL_CHECK_SECONDS)
