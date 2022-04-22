import telebot;
bot = telebot.TeleBot('5371063394:AAEewzFPDqPjMSYhvvwvbZznzspoWIb3m5I');

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Напиши /info!")

@bot.message_handler(commands=['info'])
def start_command(message):
    bot.send_message(message.chat.id, "Наш огромный проект предоставляет вам чит за маленькую сумму🙀 что бы увидеть больше функций напишите /help")
	
@bot.message_handler(commands=['help'])
def start_command(message):
    bot.send_message(message.chat.id, "/buy купить чит /help2 Связаться с админ. /info информация☀️")
	
@bot.message_handler(commands=['buy'])
def start_command(message):
    bot.send_message(message.chat.id, "После покупки свяжитесь с и отравьте кму чек платежа😼 @kuwekitty Ссылка для платежа: https://yoomoney.ru/bill/pay/crd6TQJPds0.220422 ")
	
@bot.message_handler(commands=['help2'])
def start_command(message):
    bot.send_message(message.chat.id, "Пишите @kuwekitty или @Jofi0")
	
bot.polling()
