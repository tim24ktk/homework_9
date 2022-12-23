import telebot
from telebot import types

bot = telebot.TeleBot('5926446319:AAGxiyAwb26vVgoNPftS2LTxreZFv7YrnWI')
total_objects = 117
flag = True


@bot.message_handler(commands=['start', 'help'])
def start_game(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}')
    msg = bot.send_message(message.chat.id, f'Первым делает ход Игрок 1')

    bot.register_next_step_handler(msg, first_move)


@bot.message_handler(content_types=['text'])
def first_move(message):
    global total_objects
    global flag

    move = int(message.text)

    if total_objects > 28:
        if move > total_objects or move > 28:
            bot.send_message(message.chat.id, f'Игрок 1 ввел недопустимое значение! Попробуйте снова!')
        else:
            total_objects -= move
            flag = False
            bot.send_message(message.chat.id,
                             f'Ходил Игрок 1, он взял {move}. На столе осталось {total_objects} конфет.')

            msg = bot.send_message(message.chat.id, f'Игрок 2 ваш ход')

            bot.register_next_step_handler(msg, second_move)
    else:
        if flag:
            bot.send_message(message.chat.id, f"Выиграл Игрок 1")
        else:
            bot.send_message(message.chat.id, f"Выиграл Игрок 2")


@bot.message_handler(content_types=['text'])
def second_move(message):
    global total_objects
    global flag

    if total_objects > 28:
        move = int(message.text)

        if move > total_objects or move > 28:
            bot.send_message(message.chat.id, f'Игрок 2 ввел недопустимое значение! Попробуйте снова!')
        else:
            total_objects -= move
            flag = True
            bot.send_message(message.chat.id,
                             f'Ходил Игрок 2, он взял {move}. На столе осталось  {total_objects} конфет.')
            bot.send_message(message.chat.id, f'Игрок 1 ваш ход')
    else:
        if flag:
            bot.send_message(message.chat.id, f"Выиграл Игрок 1")
        else:
            bot.send_message(message.chat.id, f"Выиграл Игрок 2")


bot.infinity_polling()
