import view

student_id_counter = 0
students = {}
classes = {}

def AddNewStudent():
    new_student = dict()
    new_student['Id'] = GetNewId()
    new_student['First_Name'] = view.GetNewStudentInfo('student`s first name')
    new_student['Last_Name'] = view.GetNewStudentInfo('student`s last name')
    new_student['Birthday'] = view.GetNewStudentInfo('student`s birthday')
    AddStudentsInClasses(new_student['Id'])
    return new_student

def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter

def SaveStudents(student):
    with open('HomeWork8\students.csv', 'a') as file:
        file.write(f"{student['Id']};{student['First_Name']};{student['Last_Name']};{student['Birthday']}\n")

def AddStudentsInClasses(student_id):
    global classes
    student_class = view.GetNewStudentInfo("student's class")
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]

def GetLastStudentId():
    global student_id_counter
    with open('HomeWork8\last_student_id.txt', 'r') as file:
        student_id_counter = int(file.read())

def SaveLastStudentId():
    global student_id_counter
    with open('HomeWork8\last_student_id.txt', 'w') as file:
        file.write(str(student_id_counter))

def SaveClasses():
    global classes
    with open('HomeWork8\classes.txt', 'w') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')

def GetClasses():
    with open('HomeWork8\classes.txt', 'r') as file:
        global classes
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = list(map(int, element[element.index('[') + 1:-2].split(', ')))
