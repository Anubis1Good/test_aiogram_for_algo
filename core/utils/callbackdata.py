from aiogram.filters.callback_data import CallbackData

class UserInfo(CallbackData, prefix='name'):
    name: str
    age: int