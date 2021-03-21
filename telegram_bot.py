import requests
from config import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:

    def __init__(self):

        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None


    def parse_webhook_data(self, data):

        message = data['message']
        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        #self.first_name = message['from']['first_name']
        #self.last_name = message['from']['last_name']


    def forward_message(self,chat_id):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(chat_id,"Stranger : "+self.incoming_message_text))
        return True if res.status_code == 200 else False

    def send_msg(self,id,msg):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(id,msg))
        return True if res.status_code == 200 else False


    @staticmethod
    def init_webhook(url):
        print(requests.get(url))


