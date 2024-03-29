from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import UserInfo

select_info = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Ivan',
            callback_data='name Ivan 19'
        )
    ],
    [
        InlineKeyboardButton(
            text='Oleg',
            callback_data='name Oleg 19'
        )
    ],
    [
        InlineKeyboardButton(
            text='Peter',
            callback_data='name Peter 19'
        )
    ],
    [
        InlineKeyboardButton(
            text='google',
            url='https://google.com'
        )
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            url='tg://user?id=1083538799'
        )
    ],

])

def get_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Ivan',callback_data=UserInfo(name='Ivan', age=19))
    kb.button(text='Oleg',callback_data=UserInfo(name='Oleg', age=19))
    kb.button(text='Vasya',callback_data=UserInfo(name='Vasya', age=19))
    kb.button(text='search',url='https://google.com')
    kb.adjust(3,1)
    return kb.as_markup()