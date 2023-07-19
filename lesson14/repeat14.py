import json

with open("lesson14/text.txt",'w', encoding="UTF-8") as file:
    file.write("qwrty")

student_rating = {
    'Murad': 10,
    'Tamara': 7,
    'rtuu': 78
}

with open("lesson14/studs.json",'w', encoding="UTF-8") as file:
    json.dump(student_rating, file, indent=2, ensure_ascii=False)

print(json.dumps(student_rating))#?
