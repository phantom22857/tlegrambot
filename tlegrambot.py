from telebot import types
import telebot
bot = telebot.TeleBot('1444084741:AAEdotKF3pxiaQzm5gOYP5rJ5mVxUGOt0SM')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, 'Слушаю...(Если хотите узнать что я за бот напишите /help)')
@bot.message_handler(commands=['help'])
def send_welcome(message):
        print(message)
        bot.send_message(message.chat.id,'Здраствуй,я бот,который может переводить разные приставки в стандартный вид,для этого нужно написать /info')
@bot.message_handler(commands=['info'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Дека", callback_data="deka")
    callback_button2 = types.InlineKeyboardButton(text="Гекто", callback_data="gekto")
    callback_button3 = types.InlineKeyboardButton(text="Кило", callback_data="kilo")
    callback_button4 = types.InlineKeyboardButton(text="Мега", callback_data="mega")
    callback_button5 = types.InlineKeyboardButton(text="Гига", callback_data="giga")
    callback_button6 = types.InlineKeyboardButton(text="Терра", callback_data="tera")
    callback_button7 = types.InlineKeyboardButton(text="Пета", callback_data="peta")
    callback_button8 = types.InlineKeyboardButton(text="Экса", callback_data="eksa")
    callback_button9 = types.InlineKeyboardButton(text="Зетта", callback_data="zetta")
    callback_button10 = types.InlineKeyboardButton(text="Иотта", callback_data="iotta")
    callback_button11 = types.InlineKeyboardButton(text="Деци", callback_data="deci")
    callback_button12 = types.InlineKeyboardButton(text="Санти", callback_data="santi")
    callback_button13 = types.InlineKeyboardButton(text="Милли", callback_data="mili")
    callback_button14 = types.InlineKeyboardButton(text="Микро", callback_data="micro")
    callback_button15 = types.InlineKeyboardButton(text="Нано", callback_data="nano")
    callback_button16 = types.InlineKeyboardButton(text="Пико", callback_data="piko")
    callback_button17 = types.InlineKeyboardButton(text="Фремто", callback_data="fremto")
    callback_button18 = types.InlineKeyboardButton(text="Атто", callback_data="atto")
    callback_button19 = types.InlineKeyboardButton(text="Зепто", callback_data="zepto")
    callback_button20 = types.InlineKeyboardButton(text="Иокто", callback_data="iokto")
    keyboard.add(callback_button1,callback_button2,callback_button3,callback_button4,callback_button5,callback_button6,callback_button7,callback_button8,callback_button9,callback_button10,callback_button11,callback_button12,callback_button13,callback_button14,callback_button15,callback_button16,callback_button17,callback_button18,callback_button19,callback_button20)
    bot.send_message(message.chat.id, "Вот все приставки величин", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def value(call):
    if call.data == 'deka':
        bot.send_message(call.message.chat.id,'10 в степени 1')    
    elif call.data == 'gekto':
        bot.send_message(call.message.chat.id,'10 в степени 2')
    elif call.data == 'kilo':
        bot.send_message(call.message.chat.id,'10 в степени 3')
    elif call.data == 'mega':
        bot.send_message(call.message.chat.id,'10 в степени 6')
    elif call.data == 'giga':
        bot.send_message(call.message.chat.id,'10 в степени 9')
    elif call.data == 'tera':
        bot.send_message(call.message.chat.id,'10 в степени 12')
    elif call.data == 'peta':
        bot.send_message(call.message.chat.id,'10 в степени 15')
    elif call.data == 'eksa':
        bot.send_message(call.message.chat.id,'10 в степени 18')
    elif call.data == 'zetta':
        bot.send_message(call.message.chat.id,'10 в степени 21')
    elif call.data == 'iotta':
        bot.send_message(call.message.chat.id,'10 в степени 24')
    elif call.data == 'deci':
        bot.send_message(call.message.chat.id,'10 в степени -1')
    elif call.data == 'santi':
        bot.send_message(call.message.chat.id,'10 в степени -2')
    elif call.data == 'mili':
        bot.send_message(call.message.chat.id,'10 в степени -3')
    elif call.data == 'micro':
        bot.send_message(call.message.chat.id,'10 в степени -6')
    elif call.data == 'nano':
        bot.send_message(call.message.chat.id,'10 в степени -9')
    elif call.data == 'piko':
        bot.send_message(call.message.chat.id,'10 в степени -12')
    elif call.data == 'femto':
        bot.send_message(call.message.chat.id,'10 в степени -15')
    elif call.data == 'atto':
        bot.send_message(call.message.chat.id,'10 в степени -18')
    elif call.data == 'zepto':
        bot.send_message(call.message.chat.id,'10 в степени -21')
    elif call.data == 'iokto':
        bot.send_message(call.message.chat.id,'10 в степени -24')
if __name__ == '__main__':
    bot.polling(none_stop=True)
 