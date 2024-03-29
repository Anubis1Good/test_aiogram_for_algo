from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Btn1'
        ),
        KeyboardButton(
            text='Btn2'
        ),
        KeyboardButton(
            text='Btn3'
        )
    ],
    [
        KeyboardButton(
            text='Btn4'
        ),
        KeyboardButton(
            text='Btn5'
        ),
    ]
], resize_keyboard=True,one_time_keyboard=True,input_field_placeholder='Press any button!', selective=True)

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='btn1')
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.button(text='Отправить свой контакт',request_contact=True)
    keyboard_builder.button(text='Создать викторину',request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3,2,1)
    return keyboard_builder.as_markup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder='gooo')


