from aiogram import types

from aiogram.dispatcher.filters.builtin import  CommandStart

from loader import dp

@dp.messgae_handler(CommandStart())
async def bot_start(message: types.Message):
    name= messgae.from_user.fullname