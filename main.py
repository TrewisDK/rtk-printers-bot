import aiogram
from datetime import datetime
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6286754904:AAHjfcWwUi_dU2htpA6CtEWe9GsqGH23ZIU")
dp = Dispatcher(bot)

mainboard = ReplyKeyboardMarkup(resize_keyboard=True)
kabsboard = ReplyKeyboardMarkup(resize_keyboard=True)
katboard = ReplyKeyboardMarkup(resize_keyboard=True)
zamena_kb = KeyboardButton('Замена')
mainboard.add(zamena_kb)
with open("kabs.txt", "r") as f:
    kabs = f.readlines()
    for i in kabs:
        kab_kb = KeyboardButton(f"kab_{i}")
        kabsboard.add(kab_kb)
with open("katridj", "r") as f:
    kats = f.readlines()
    for i in kats:
        kat_kb = KeyboardButton(f"kat_{i}")
        katboard.add(kat_kb)
ids = []
with open("accounts", "r") as f:
    id = f.readlines()
    for i in id:
        ids.append(ids.append(i.split(":")[1]))

kab = ""
kat = ""
user = ""


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Приветсвуем в боте!\n\nЧто хотите купить?", reply_markup=mainboard)
    await bot.send_message(940043266, "Пожалуйста не ломайте меня")


@dp.message_handler(commands=['get'])
async def process_start_command(message: types.Message):
    print(message.from_user.id)


@dp.message_handler()
async def echo_message(msg: types.Message):
    global kab
    global kat
    if msg.text == 'Замена':
        await msg.reply("В каком кабинете?", reply_markup=kabsboard)
    if msg.text.startswith("kab_"):
        kab = msg.text
        await msg.reply("Какой катридж?", reply_markup=katboard)
    if msg.text.startswith("kat_"):
        kat = msg.text
        with open("log.txt", "a+") as f:
            f.write(f"Кабинет {kab}, Катридж {kat}, Пользователь {msg.from_user.id}, Дата {datetime.now()}\n")
            await msg.reply(f"Кабинет {kab}, Катридж {kat}, Пользователь {msg.from_user.id}, Дата {datetime.now()}")
            await bot.send_document(msg.from_user.id, open("log.txt", 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp)
