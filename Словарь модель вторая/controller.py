import json
import add
import view
from pprint import pprint
from random import randint as rd, choice as ch
def work():
    add.add_random('Words.json')
    add.Write(add.data , 'Words.json')
    print('вы хотите видеть весь список, или конкретную позицию? ')
    print('если весь, то напишите print, а если что-то конкретное, то search')
    def choose(i):
        i = str(input)
        if i == "search":
            number = int ( input('какая позиция вас интересует'))
            view.search('Words.json', number)
        elif i =="print":
            view.show_base('Words.json')
