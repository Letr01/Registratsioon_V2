Users=open('Users.txt', 'r')
Passw=open('Password.txt','r')
status = ''
def Registratsioon():
    status = input('Вы уже зарегестрированы? Да или Нет? Для выхода пишите "Выход"\n')
    if status == 'Да':
        Vana_Kasutaja()
    elif status == 'Нет':
        Uus_Kasutaja()
 
def Uus_Kasutaja():
    Login = input('Введите свой логин:')
    if Login in Users:
        print('Данный логин уже занят.')
    else:
        Password = input('Придумайте пароль: ')
        Users.write(Login)
        Passw.write(Password)
        print('Добро пожаловать',Login)
 
def Vana_Kasutaja():
    login = input('Введите логин: ')
    passw = input('Введите пароль: ')
 
    if login in Users and passw in Passw:
        print('С возвращением,',login)
    else:
        print('Неверные данные!')
 
 
while status != 'Выход':
    Registratsioon()
else:
    print('Выходим')
    quit() 