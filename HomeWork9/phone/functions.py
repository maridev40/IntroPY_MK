import logger

def ExportContactsInCVS(path, file_name, contacts):
    if path == '':
        path = 'phone\\'
    with open(path + file_name, 'w', encoding='utf-8') as file:
        file.write(f'First Name;Last Name;Phone Number;Description\n')

        for i in contacts:
            file.writelines(f"{contacts[i]['First Name']};{contacts[i]['Last Name']};{i};{contacts[i]['Description']}\n")
    
    logger.Log(f'Export completed in {path + file_name}')

def ExportContactsInTxtColumns(path, file_name, contacts):
    if path == '':
        path = 'phone\\'
    with open(path + file_name, 'w', encoding='utf-8') as file:
        for i in contacts:
            file.write(f"First Name: {contacts[i]['First Name']}\n")
            file.write(f"Last Name: {contacts[i]['Last Name']}\n")
            file.write(f"Phone Number: {i}\n")
            file.write(f"Description: {contacts[i]['Description']}\n")
            file.write('\n')

    logger.Log(f'Export completed in {path + file_name}')

def SaveData(phonebook):
    with open('phone\PBData.txt', 'w', encoding='utf-8') as file:
        file.writelines(f"Phone Number;First Name;Last Name;Description\n")
        for i in phonebook:
            file.writelines(f"{i};{phonebook[i]['First Name']};{phonebook[i]['Last Name']};{phonebook[i]['Description']}\n")
        
    logger.Log(f'Data saved in PBData.txt')

def GetDataFromRows(path):
    with open(path, 'r', encoding='utf-8') as file:
        pb = file.readline()

        new_pb = {}
        while pb:

            new_temp = {}

            temp = pb.replace('\n','').split(';')

            pb_key = temp[2]
            new_temp['First Name'] = temp[0]
            new_temp['Last Name'] = temp[1]
            new_temp['Description'] = temp[3]
            new_pb[pb_key] = new_temp 

            pb = file.readline()

    return new_pb

def MatchingNumbers(phonebook, new_phones):

    for key in new_phones:
        # overwrite = ''
        # print(f'60 fun key={key}')
        # print()

        # if key in phonebook and (overwrite.lower() != 'y+' or overwrite.lower() != 'n+'):
        #     overwrite = input(f"{key} уже существует как {phonebook[key]['First Name']} {phonebook[key]['Last Name']}. Хотители Вы переписать его?\nЧтобы изменить все телефоны нажмите Y+.\nДля выхода нажмите N+.\nY/N/Y+/N+ ")

        # if overwrite.lower() == 'n' or overwrite.lower() == 'n+':
        #     logger.Log(f'{key} change denied.')
        # else:
        phonebook[key] = new_phones[key]
        logger.Log(f'{key} change completed.')

def GetDataFromRowCol(path):
    with open(path, 'r', encoding='utf-8') as file:
        temp = ''.join(file.readlines()).replace('\n', ';').replace(';;', ';').split(';')
        while temp[-1] == '':
            temp.pop()
        new_pb = {}

        index_phone = temp.index('Phone Number')
        index_first = temp.index('First Name')
        index_last = temp.index('Last Name')
        index_desc = temp.index('Description')
        for i in range(4, len(temp), 4):
            q = {}
            for j in range(0, 4):
                if j == index_first:
                    q['First Name'] = temp[j + i].replace('\n', '')
                elif j == index_last:
                    q['Last Name'] = temp[j + i].replace('\n', '')
                elif j == index_desc:
                    q['Description'] = temp[j + i].replace('\n', '')

            new_pb[temp[index_phone + i].replace('\n', '')] = q

    logger.Log('Data (row version) copied. ')
    return new_pb