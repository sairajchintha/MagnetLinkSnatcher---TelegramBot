from flask import Flask, request, jsonify
from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL
import requests,json,urllib.parse

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/')
def home():
    return "<h1>hello2</h1>"


@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json() 
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    
    if bot.incoming_message_text == '/start':
            message = '🤙Enter search in format /search "text"🤙'
            success=bot.send_msg(bot.chat_id,message)
            return jsonify(success=success)

    elif bot.incoming_message_text[0:7]=="/search":
            if bot.incoming_message_text[8:].strip(" ")==False:
                success=bot.send_msg(bot.chat_id,"please enter some text")
                return jsonify(success=success)
            searching_text=bot.incoming_message_text[8:]
            print(searching_text)
            message=""
            response=requests.get(f"https://api.sumanjay.cf/torrent/?query={searching_text}")
            for x in response.json()[0:3]:
                message+=f"'name' : {x['name']} \n age:{x['age']} \n 'magnet' : {x['magnet']} \n\n "
            print(str(message))
            success=bot.send_msg(bot.chat_id,urllib.parse.quote(message))
            return jsonify(success=success)
    else:
            message = "invalid command"
            success=bot.send_msg(bot.chat_id,"Invalid Command")
            return jsonify(success=success) 

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=80)


# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<secret key>/getme
# check webhook url: https://api.telegram.org/secret key/getWebhookInfo
