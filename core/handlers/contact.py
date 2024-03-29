from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(msg:Message, bot: Bot):
    await msg.answer('You send your contact')

async def get_fake_contact(msg:Message, bot: Bot):
    await msg.answer('You send fake contact')