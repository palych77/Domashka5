# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def deleteabv():
    s = input("Введите слова через пробел: ").split()
    spisok = list(filter(lambda x: 'абв' not in x, s))
    print (spisok)

try:
    deleteabv()
except:
    print('Введите слова через пробел!')


