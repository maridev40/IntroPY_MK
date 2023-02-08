from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

real_data = KeyboardButton('Вещественные числа')
complex_data = KeyboardButton('Комплексные числа')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(real_data).add(complex_data)