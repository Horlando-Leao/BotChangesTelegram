import os
import os.path as path
from configparser import ConfigParser

config = ConfigParser()


def write_config(filepath):
    config.add_section('TELEGRAM')
    config.set('TELEGRAM', 'schema', '')
    config.set('TELEGRAM', 'host', '')
    config.set('TELEGRAM', 'bot_token', '')
    config.set('TELEGRAM', 'bot_chat_id', '')

    config.add_section('TRELLO')
    config.set('TRELLO', 'url', '')
    config.set('TRELLO', 'api_key', '')
    config.set('TRELLO', 'api_token', '')

    # Write the new structure to the new file
    with open(filepath, 'w') as configfile:
        config.write(configfile)


def set_file_config(filename: str):
    os.environ['FILE_CONFIG_INI'] = filename


def settings_env():

    os.environ['PATH_ROOT_PROJECT'] = path.dirname(os.path.abspath(__file__))
    path_config = path.join(os.environ.get('PATH_ROOT_PROJECT'), os.environ.get('FILE_CONFIG_INI'))

    if not path.isfile(path_config):
        write_config(path_config)
        raise EnvironmentError(f"Set or make file in {path_config}")


