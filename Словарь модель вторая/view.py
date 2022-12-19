import json
import add
from pprint import pprint

def read (file_name):
    with open (file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def search (file_name,number):
    new_data = read(file_name)
    print(new_data['Users'][number])

def show_base(file_name):
    pprint(read(file_name))