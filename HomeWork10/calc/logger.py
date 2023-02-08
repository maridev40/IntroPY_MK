from datetime import datetime

def Log(message):
    time = datetime.now().strftime('%D %H:%M:%S')
    with open('calc\log.txt', 'a') as file:
        file.write(f'{time} - {message}\n')