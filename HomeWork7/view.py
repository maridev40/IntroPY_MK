def GetNewPhone():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    phone_number = input('Телефон: ')
    discription = input('Описание: ')
    new_phone = dict()
    # new_phone[phone_number] = [first_name, last_name, discription]
    new_phone[phone_number] = {'First Name': first_name, 'Last Name': last_name, 'Description': discription}
    
    return new_phone

def GetUserChoice():
    return input('Выберите: \n1. Добавьте новый номер телефона\n2. Импорт файла\n3. Экспорт файла\n4. Выход\n')    

def GetFilePath():
    return input('Введите путь к файлу: ')

def GetExportFileType():
    return input('Выбрать тип файла.\n1. *.csv\n2. *.txt\n')

def GetDataType(message):
    print('1. Фамилия_1;Имя_1;Телефон_1;Описание_1')
    print('   Фамилия_2;Имя_2;Телефон_2;Описание_2')
    print()
    print('2. Фамилия_1') 
    print('   Имя_1') 
    print('   Телефон_1') 
    print('   Описание_1')  
    print()
    print('   Фамилия_2') 
    print('   Имя_2') 
    print('   Телефон_2') 
    print('   Описание_2') 
    return input(f'Выберите тип данных, которые вы хотите {message}: ')
