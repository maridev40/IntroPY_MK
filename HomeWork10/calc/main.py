import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import kb_main
import functions


logging.basicConfig(level=logging.INFO)

# MyPython1234_bot
API_TOKEN = '6133154125:AAF7gggzxWTZSv5tMHoJliAiMASLdReN120'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

print('Start')

class Calc(StatesGroup):
    number_type = State()
    number_1 = State()  
    oper = State()
    number_2 = State() 

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Calc.number_type.set()
    await message.answer('Задать тип чисел: \n1. Выбрать вещественные числа\n2. Выбрать комплексные числа\n3. Выйти\n', reply_markup=kb_main)  

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=Calc.number_type)
async def process_number_type(message: types.Message, state: FSMContext):
    if message.text == '3':
        await state.finish()
        await message.reply('Отменено.', reply_markup=types.ReplyKeyboardRemove())
        return

    async with state.proxy() as data:
        if message.text == 'Вещественные числа':
            data['number_type'] = '1'
        elif message.text == 'Комплексные числа':
            data['number_type'] = '2'
        elif message.text in ('1', '2', '3'):
            data['number_type'] = message.text
        else:
            return

    txt = ''
    if data['number_type'] == '2':
        txt = ', например, (3 + 1i)'
    await Calc.next()    
    await message.answer(f'Введите первое число{txt}', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=Calc.number_1)
async def process_number_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_1'] = message.text

    await Calc.next()
    await message.reply(f'Вы ввели первое число: {message.text}')

    await message.answer('Введите операцию: "+", "-", "*", "/" ')

@dp.message_handler(lambda message: message.text in ('+', '-', '*', '/'), state=Calc.oper)
async def process_oper(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['oper'] = message.text

    await Calc.next()
    await message.reply(f'Вы ввели операцию: {message.text}')

    txt = ''
    if data['number_type'] == '2':
        txt = ', например, (5 - 2i)'
    await message.answer(f'Введите второе число{txt}')

@dp.message_handler(state=Calc.number_2)
async def process_number_2(message: types.Message, state: FSMContext):

    await message.reply(f'Вы ввели второе число: {message.text}')

    txt = 'Результат: '
    async with state.proxy() as data:
        data['number_2'] = message.text
        txt += data['number_1'] + ' ' + data['oper'] + ' ' + data['number_2'] + ' = '

        if data['number_type'] == '1':
            txt += functions.getResult(data['oper'], data['number_1'], data['number_2'])
        else:
            txt += functions.getComplexResult(data['oper'], data['number_1'], data['number_2'])
    
    await message.answer(txt)

    await state.finish()

    await Calc.number_type.set()
    await message.answer('Задать тип чисел: \n1. Выбрать вещественные числа\n2. Выбрать комплексные числа\n3. Выйти\n', reply_markup=kb_main)  


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)          
