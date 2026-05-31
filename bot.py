import telebot
import importlib
import sys

# Принудительно импортируем файл с русским названием
import кара 
import graf

TOKEN = '8359412450:AAG3GXz1F-JVLcGdFips6l-DWECk26NLD0c'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Пришли мне дату в формате: день.месяц.год")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    try:
        parts = message.text.split('.')
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        
        # Обновляем данные в файле кара.py
        кара.user_day = day
        кара.user_month = month
        кара.user_year = year
        importlib.reload(кара)
        
        # Генерируем график из файла graf.py
        img = graf.generate_star(message.text)
        
        bot.send_photo(message.chat.id, img)
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
print("Бот успешно запущен и слушает Telegram...")