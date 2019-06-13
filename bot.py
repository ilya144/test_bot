import telebot
import requests
import json

token = ""

bot = telebot.TeleBot(token, threaded=False)

@bot.message_handler(commands=["start"])
def main_handler(message):
    raw = message.from_user
    user_data = {}
    user_data['id'] = raw.id
    user_data['username'] = raw.username
    user_data['first_name'] = raw.first_name
    user_data['last_name'] = raw.last_name
    payload = json.dumps(user_data)
    requests.post("http://localhost:8000/setUser/", data=payload)

    reply_message = requests.get("http://localhost:8000/getMessage/")
    bot.send_message(raw.id, reply_message)

if __name__ == '__main__':
    bot.polling()