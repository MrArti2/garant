import telebot 
from telebot import types
import time

bot = telebot.TeleBot("7084861550:AAHbJ8hFye04pOOUDFCO-FC95aQd5sgOjEM")

@bot.message_handler(commands=['garant'])
def send_msg(message):
    markup = types.InlineKeyboardMarkup()
    delete = types.InlineKeyboardButton(text="Удалить", callback_data="delete")
    markup.add(delete)
    text = "Нужны гаранты\n@slowsunset, @MHE_OXOTA_TAKE, @yTeHochEK, @Vlad_Adventist"
    try:
        bot.reply_to(message, text, reply_markup=markup)
    except Exception as e:
        print(e)
        time.sleep(10)
        bot.reply_to(message, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    def del_msg(call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    
    try:
        if call.data == 'delete':
            user = bot.get_chat_member(call.message.chat.id, call.from_user.id)
            if user.status in ['administrator', 'creator']:
                del_msg(call)
                bot.answer_callback_query(call.id, "Сообщение удалено")
            else:
                bot.answer_callback_query(call.id, "Ты не админ")
    except Exception as e:
        None

bot.polling()