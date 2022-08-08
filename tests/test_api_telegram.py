import os
from unittest import TestCase, mock


class TestSendMessageTelegramBotApi(TestCase):

    def test_send_message_telegram_bot_api_is_send_and_return_status_ok(self):
        pass


class TestFormatMessageForTrelloUpdates(TestCase):

    @mock.patch.dict(os.environ, {'FILE_CONFIG_INI': '/home/horlando/PycharmProjects/BotChangesTelegram/config.ini'})
    def test_format_message_for_trello_updates_is_string(self):
        from src.api.api_telegram import format_message_for_trello_updates

        mock_action = {
            'memberCreator': {
                'fullName': ''
            },
            'data': {
                'board': {
                    'name': ''
                },
                'card': {
                    'name': ''
                }
            }
        }

        result = format_message_for_trello_updates(action=mock_action)

        self.assertTrue(isinstance(result, str))
