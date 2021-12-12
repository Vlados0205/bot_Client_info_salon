# bot_Client_info_salon
#Thats very easy bot, which you can check small info, see a few pictures, and one link to the google translation form
import telebot
from telebot import types
# Название телеграм бота Client_info_salonbot
TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_text(message):
        bot.send_message(message.chat.id, 'Приветствую, данный бот является экспериментальной разработкой по записи клиентов в салон через телеграм,! По всем вопросам обращайтесь в лс @jerome0205')

@bot.message_handler(commands=['record'])
def handle_text(message):
        bot.send_message(message.chat.id, 'Приветствую , заполнив данную форму вы можете записать к нам на услугу : https://forms.gle/8Nguehjqrmiptoxw7' )

@bot.message_handler(commands=['payment'])
def handle_text(message):
        bot.send_message(message.chat.id,'Мы принимаем наличку, безналичный расчёт по терминалу и перевод на карту Сбербанк/Тинькофф')

@bot.message_handler(commands=['info'])
def text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

    item1 = types.KeyboardButton('💵Прайс и мастера')
    item2 = types.KeyboardButton('📍🗺️Адрес')
    item3 = types.KeyboardButton('🕒Время работы')

    
    markup.add(item1,item2,item3)
    
    bot.send_message(message.chat.id, 'Приветствую ,{0.first_name}, при помощи данных кнопок ты можешь узнать немного о нас'.format(message.from_user),reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == '💵Прайс и мастера': 
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUhWVAr' ) 
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUu0nFx' )
			bot.send_message(message.chat.id, 'данные фото были взяты у реальных мастеров с их согласия' )
	
		if message.text == '📍🗺️Адрес':
			bot.send_message(message.chat.id, ' Г.Москва, Ленинский проспект дом 90 (данный салон больше не работает, взят для примера).')
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUu23ef' )
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUjN7C7' )
		if message.text == '🕒Время работы':
			bot.send_message(message.chat.id, 'c 10:00 до 22:00' )

bot.polling(none_stop= True)
