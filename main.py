from aiogram import *
from aiogram.types.web_app_info import WebAppInfo
import sqlite3
bot = Bot('7060653861:AAGwqUu6ez1x3cTswJfiNnztj8Kk7ocmV6c')
dp = Dispatcher(bot)
prof = 1 ###############################################################

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    conn = sqlite3.connect('yongbuisnes.sqlite3')
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Авторизоваться!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/')))
    await message.answer('Привет, мой друг, для дальнейшей работы тебе необходимо авторизоваться!', reply_markup=markup)


async def menu(message: types.Message):
    if prof == 1:
        btn1 = types.KeyboardButton('Личный кабинет', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn2 = types.KeyboardButton('Магазин!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn3 = types.KeyboardButtonn('Активности!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn4 = types.KeyboardButton('Выход')
    elif prof == 2:
        btn1 = types.KeyboardButton('Личный кабинет', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn2 = types.KeyboardButton('Магазин!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn3 = types.KeyboardButton('Активности!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/'))
        btn4 = types.KeyboardButton('Выход')
        btn5 = types.KeyboardButton('Добавить класс!')
        btn6 = types.KeyboardButton('Добавить учеников!')


executor.start_polling(dp)