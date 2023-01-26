import view
import functions

def Start():
    current_phonebook = functions.GetDataFromRows('PBData.txt')
    # print(f'6 con current_phonebook={current_phonebook}')
    stop = False

    while not stop:
        user_choice = view.GetUserChoice()
        # print(f'10 con user_choice={user_choice}')
        if user_choice == '1':
            new_phone = view.GetNewPhone()
            # print(f'13 con new_phone={new_phone}')
            functions.MatchingNumbers(current_phonebook, new_phone)
        elif user_choice == '2':
            path = view.GetFilePath()
            # print(f'18 con path={path}')
            if int(view.GetDataType('импортировать')) == 1:
                new_phones = functions.GetDataFromColumns(path)
                # print(f'23 con new_phones={new_phones}')
            else:
                new_phones = functions.GetDataFromRows(path)
            functions.MatchingNumbers(current_phonebook, new_phones)

        elif user_choice == '3':
            path = view.GetFilePath()
            '''1 - csv
                2 - txt'''
            if int(view.GetExportFileType()) == 2:
                if int(view.GetDataType('экспортировать')) == 2:
                    functions.ExportContactsInTxtColumns(path, 'contacts322.txt', current_phonebook)
                else:
                    functions.ExportContactsInCVS(path, 'contacts321.txt', current_phonebook)
            else:
                functions.ExportContactsInCVS(path, 'contacts31.csv', current_phonebook) 
        else:
            stop = True

    functions.SaveData(current_phonebook)
       
