import json

with open("lesson13/data.json", encoding='UTF-8') as file:
    info = json.load(file)
print(info)
print(info["FIO"])

film_info = {
    'genre': ['drama', 'horror', 'fantasy', 'Sci-fi'],
    'title': ['1+1','Пила','Хоббит','Интерстеллар']
}

with open('lesson13/films.json', 'w', encoding='UTF-8') as file:
    json.dump(film_info, file, ensure_ascii=False, indent=2 )