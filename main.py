from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import  Command
from core.handlers.basic import get_start, get_photo, get_inline
from core.handlers.contact import get_fake_contact, get_true_contact
from core.handlers.callback import select_names
from core.middlewares.settings import settings
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands
from core.utils.callbackdata import UserInfo
import asyncio
import logging


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='botStart')
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='botStop')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token,parse_mode='HTML')
    dp = Dispatcher()
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_inline,Command(commands=['inline']))
    dp.message.register(get_photo,F.photo)
    dp.message.register(get_true_contact,F.contact,IsTrueContact())
    dp.message.register(get_fake_contact,F.contact)
    # dp.callback_query.register(select_names,F.data.startswith('name'))
    dp.callback_query.register(select_names,UserInfo.filter())
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())