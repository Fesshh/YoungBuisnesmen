from aiogram import *
from aiogram.types.web_app_info import WebAppInfo
import sqlite3
import json
bot = Bot('7060653861:AAGwqUu6ez1x3cTswJfiNnztj8Kk7ocmV6c')
dp = Dispatcher(bot)
a=0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Авторизоваться!', web_app=WebAppInfo(url='https://pornovolk.info/videos/546/stroynuyu-ukrainku-ebet-nemeckaya-ovcharka-i-kommentarii-posle-zoo-seksa/')))
    await message.answer('Привет, мой друг, для дальнейшей работы тебе необходимо авторизоваться!', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def reg(message: type.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'FirstName: {res["FirstName"]}, LastName: {res["LastName"]}, Password: {res["password"]}, email: {res["email"]}, ClasLet: {res["ClasLet"]}, ClasNum: {res["ClasNum"]} ')
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO db (password,is superuser, first name, last name, email, is staf, clas let, clas num) VALUES ({res["password"]}, {a}, {res["FirstName"]}, {res["LastName"]},{res["email"]}, {a}, {res["ClasLet"]}, {res["ClasNum"]})")
    conn.commit()
    cur.close()
    conn.close()


async def menu(message: types.Message):
    message.answer('Регистрация успешно окончена!')
    message.answer('К сожалению основной функционал бота пока что ещё находится в разработке')
    


executor.start_polling(dp)