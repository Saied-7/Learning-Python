
students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name":"Ron", "house": "Gryffindor", "patronus": "stag"},
    {"name":"Harry", "house": "Gryffindor", "patronus": "jack russel terrir"},
    {"name":"Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    # print student index like ron,harry and value like gryffindor,slytherin
    print(student["name"] , student["house"], student["patronus"], sep = ", ")