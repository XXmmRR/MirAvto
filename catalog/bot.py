import telebot
from django.core.management.base import BaseCommand

bot = telebot.TeleBot('5374226274:AAHUaEuBDvr3rHNHAuzPAlg7aKALh089uoY')

group = -795067208


def send_message(id, number, name, text):
    bot.send_message(group,   f'Заказ Номер: {id}\n'
                                     f'Телефон: {number}\n'
                                     f'Имя:{name}\n'
                                     f'{text}')


if __name__ == '__main__':
    bot.infinity_polling()
    print('я тут')