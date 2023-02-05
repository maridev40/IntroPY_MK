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
    
current_phonebook = ''
state = 'unknown'

first_name = ''
last_name = ''
phone_number = ''
discription = ''
new_phone = dict()

path = ''
file_type = ''

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}, для начала работы с телефонным справочником введите /start')

async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global state
    global first_name
    global last_name
    global phone_number
    global discription
    global new_phone
    global current_phonebook

    global path
    global file_type

    # print(f'28 next; state={state}; txt={update.message.text}')

    if update.message.text == '/start':
        state = 'choice'
        current_phonebook = functions.GetDataFromRowCol('phone\PBData.txt')

    if state == 'choice' and update.message.text == '4':
        functions.SaveData(current_phonebook)
        state = 'unknown'
        txt = 'Выход'
        await update.message.reply_text(txt) 

    # 1. Добавьте новый номер телефона
    if state == 'choice' and update.message.text == '1':
        state = 'phone'
        txt = '1. Добавить новый номер телефона'
        await update.message.reply_text(txt)  

    if state == 'phone':
        state = 'phone_name'
        txt = 'Имя:'
        await update.message.reply_text(txt)   
    elif state == 'phone_name':
        first_name = update.message.text
        state = 'phone_familia'
        txt = 'Фамилия:'
        await update.message.reply_text(txt) 
    elif state == 'phone_familia':
        last_name = update.message.text
        state = 'phone_number'
        txt = 'Телефон:'
        await update.message.reply_text(txt)  
    elif state == 'phone_number':
        phone_number = update.message.text
        state = 'phone_desc'
        txt = 'Описание:'
        await update.message.reply_text(txt) 
    elif state == 'phone_desc':
        discription = update.message.text

        new_phone[phone_number] = {'First Name': first_name, 'Last Name': last_name, 'Description': discription}
        functions.MatchingNumbers(current_phonebook, new_phone)

        state = 'choice'

    # 2. Импорт файла
    if state == 'choice' and update.message.text == '2':
        state = 'import'
        txt = '2. Импорт файла'
        await update.message.reply_text(txt)  

    if state == 'import':
        state = 'import_path'
        txt = 'Введите полный путь к файлу, например, phone\contacts.txt)'
        await update.message.reply_text(txt)

    elif state == 'import_path':
        path = update.message.text
        state = 'import_type'
        txt = 'Выберите тип данных, которые вы хотите импортировать:'
        await update.message.reply_text(txt)
        txt = '1. Фамилия_1;Имя_1;Телефон_1;Описание_1\n   Фамилия_2;Имя_2;Телефон_2;Описание_2\n2. Фамилия_1\n   Имя_1\n   Телефон_1\n   Описание_1\n\n   Фамилия_2\n   Имя_2\n   Телефон_2\n   Описание_2'    
        await update.message.reply_text(txt)

    elif state == 'import_type':
        if update.message.text == '1':
            new_phones = functions.GetDataFromRowCol(path)
        else:
            new_phones = functions.GetDataFromRowCol(path)
        functions.MatchingNumbers(current_phonebook, new_phones)

        state = 'choice'

    # 3. Экспорт файла
    if state == 'choice' and update.message.text == '3':
        state = 'export'
        txt = '3. Экспорт файла'
        await update.message.reply_text(txt)  

    if state == 'export':
        state = 'export_path'
        txt = 'Введите путь к файлу, например phone\ '
        await update.message.reply_text(txt)

    elif state == 'export_path':
        path = update.message.text
        if path[-1] != '\\':
            path += '\\'

        state = 'export_file_type'
        txt = 'Выберите тип файла:'
        await update.message.reply_text(txt)
        txt = '1. *.csv\n2. *.txt'    
        await update.message.reply_text(txt)

    elif state == 'export_file_type':
        file_type = update.message.text
        state = 'export_type'

        if file_type == '1':
            functions.ExportContactsInCVS(path, 'contacts31.csv', current_phonebook) 
            state = 'choice'
        else:
            txt = 'Выберите тип данных, которые вы хотите экспортировать:'
            await update.message.reply_text(txt)
            txt = '1. Фамилия_1;Имя_1;Телефон_1;Описание_1\n   Фамилия_2;Имя_2;Телефон_2;Описание_2\n2. Фамилия_1\n   Имя_1\n   Телефон_1\n   Описание_1\n\n   Фамилия_2\n   Имя_2\n   Телефон_2\n   Описание_2'    
            await update.message.reply_text(txt)

    elif state == 'export_type':
        if update.message.text == '1':
            functions.ExportContactsInCVS(path, 'contacts321.txt', current_phonebook)
        else:
            functions.ExportContactsInTxtColumns(path, 'contacts322.txt', current_phonebook)

        state = 'choice'

    if state == 'choice':
        txt = 'Выберите: \n1. Добавить новый номер телефона\n2. Импортировать файл\n3. Экспортировать файл\n4. Cохранить и выйти\n'
        await update.message.reply_text(txt)    


