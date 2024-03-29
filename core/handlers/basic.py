from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard,get_reply_keyboard
from core.keyboards.inline import select_info, get_inline_keyboard


async def get_start(msg: Message, bot: Bot):
    await msg.answer(text='hello',reply_markup=get_reply_keyboard())
    # await bot.send_message(msg.from_user.id, f'Hello {msg.from_user.first_name}. ')
    # await msg.answer(f'<b>Hello {msg.from_user.first_name}.</b>')
    # await msg.reply(f'Hello {msg.from_user.id}. ')


async def get_photo(msg: Message, bot: Bot):
    await msg.answer('nice photo')
    file = await bot.get_file(msg.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_inline(msg:Message,bot:Bot):
    await msg.answer(f'Hello {msg.from_user.first_name}. Показываю инлайн кнопки',reply_markup=get_inline_keyboard())