import telebot;
bot = telebot.TeleBot('5389475164:AAG14m2Q3XLrylbH9gzUhYz_RgucLRReaww');

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Напиши /info!")

@bot.message_handler(commands=['info'])
def start_command(message):
    bot.send_message(message.chat.id, "Наш огромный проект предоставляет вам чит за бесплатно🙀 что бы увидеть больше функций напишите /help")
	
@bot.message_handler(commands=['help'])
def start_command(message):
    bot.send_message(message.chat.id, "/buy купить чит /help2 Связаться с админ. /info информация☀️")
	
@bot.message_handler(commands=['buy'])
def start_command(message):
    bot.send_message(message.chat.id, "Что бы скачать чит переходите по этой ссылке ")
	
@bot.message_handler(commands=['help2'])
def start_command(message):
    bot.send_message(message.chat.id, "Пишите @kuwekitty или @Jofi0")
	
bot.polling()
