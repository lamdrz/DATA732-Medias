import json 

FILE_NAME = 'data/fr.sputniknews.africa-all.json'

def load_data(file_name=FILE_NAME):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data