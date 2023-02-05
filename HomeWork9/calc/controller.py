from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters

import functions

def Start():
    # MyPython1234_bot
    app = ApplicationBuilder().token("6133154125:AAF7gggzxWTZSv5tMHoJliAiMASLdReN120").build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(MessageHandler(filters.TEXT, next))

    print('Start')
    app.run_polling()

state = 'unknown'
number_type = ''
number1 = ''
number2 = ''
oper = ''

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}, для начала работы с калькулятором введите /start')

async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global state
    global number_type
    global number1
    global number2
    global oper

    if update.message.text == '/start':
        state = 'choice'

    if state == 'choice' and update.message.text == '3':
        state = 'unknown'
        txt = 'Выход'
        await update.message.reply_text(txt) 

    if state == 'choice' and update.message.text in ('1', '2'):
        state = 'number_type'

    if state == 'number_type':
        state = 'number1'
        number_type = update.message.text
        
        if number_type == '3':
            state = 'choice'
        else:
            if number_type == '1':
                txt = 'Вы выбрали вещественные числа'
            elif number_type == '2':
                txt = 'Вы выбрали комплексные числа'
            await update.message.reply_text(txt)
            txt = 'Введите первое число'
            if number_type == '2':
                txt += ', например, (3 + 1i) :'
            await update.message.reply_text(txt)

    elif state == 'number1':
        state = 'oper'
        number1 = update.message.text
        txt = 'Введите операцию:\n'
        await update.message.reply_text(txt)
        txt = '+ \n- \n* \n/ '
        await update.message.reply_text(txt)

    elif state == 'oper':
        if update.message.text in ('+', '-', '*', '/'):
            state = 'number2'
            oper = update.message.text
            txt = 'Введите второе число'
            if number_type == '2':
                txt += ', например, (5 - 2i) :\n'
            await update.message.reply_text(txt)

    elif state == 'number2':
        state = 'choice'
        number2 = update.message.text
        txt = f'Результат: {number1} {oper} {number2} = '
        if number_type == '1':
            txt += f'{functions.getResult(oper, number1, number2)}'
        else:
            txt += f'{functions.getComplexResult(oper, number1, number2)}'
        await update.message.reply_text(txt)

    if state == 'choice':
        txt = 'Задать тип чисел: \n1. Выбрать вещественные числа\n2. Выбрать комплексные числа\n3. Выйти\n'
        await update.message.reply_text(txt)
