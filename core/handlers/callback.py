from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callbackdata import UserInfo

# async def select_names(call: CallbackQuery, bot: Bot):
#     data = call.data.split(" ")
#     name = data[1]
#     age = data[2]

#     answer = f'This is {name} - {age}'

#     await call.message.answer(answer)
#     await call.answer()

async def select_names(call: CallbackQuery, bot: Bot, callback_data: UserInfo):
    
    name = callback_data.name
    age = callback_data.age

    answer = f'This is {name} - {age}'

    await call.message.answer(answer)
    await call.answer()
