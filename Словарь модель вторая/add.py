import json
from pprint import pprint
from random import randint as rd, choice as ch
global data
def Write (data, file_name):
    data = json.dumps(data)
    data = json.loads(str (data))
    with open(file_name, 'a' , encoding='utf-8') as file:
        json.dump(data,file , indent=3)
    # class Users:
    #     def __init__(self) :
    #         self.ID =  range(1,100)
    #         self.First_name = ch (['Кузьма', 'Свяполк' , 'Акакий' , 'Васян' , 'Олег', 'Ярокус' , 'Вкуселав' , 'Вуглусрат'])
    #         self.Last_name  = ch (['Пупкин' , 'Пушкин' , 'Смоллет' , 'Хопкинс' , 'Исаев' , 'Рожков' , 'Мясников', 'Соколов'])
    #         self.Age = rd(0,70)
    #         self.Telephone_number = '+7'+rd(0,9)*10
    # data = {
    # 'users': []}
    # data['users'].append(Users().__dict__)
    


def add_random( file_name):
    class Users:
        def __init__(self) :
            self.ID =  range(1,100)
            self.First_name = ch (['Кузьма', 'Свяполк' , 'Акакий' , 'Васян' , 'Олег', 'Ярокус' , 'Вкуселав' , 'Вуглусрат'])
            self.Last_name  = ch (['Пупкин' , 'Пушкин' , 'Смоллет' , 'Хопкинс' , 'Исаев' , 'Рожков' , 'Мясников', 'Соколов'])
            self.Age = rd(0,70)
            self.Telephone_number = '+7'+rd(0,9)*10
    data = {
        'Users': []
    }
    for i in range (100):
        data['Users'].append(Users().__dict__)

def Save_in_file(data,file_name):
    with open(file_name, 'a' , encoding='utf-8') as file:
        json.dump(data, file, indent=2)
