def GetNewPhone():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    phone_number = input('Телефон: ')
    discription = input('Описание: ')
    new_phone = dict()
    new_phone[phone_number] = {'First Name': first_name, 'Last Name': last_name, 'Description': discription}
    
    return new_phone
