from pymongo import MongoClient

client = MongoClient('mongodb+srv://410921335:<password>@cluster0.fqttxfx.mongodb.net/?retryWrites=true&w=majority')

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
print()
db = client.get_database('students_db')

students_collection = db.students
classes_collection = db.classes
grades_collection = db.grades

# insert other documents in the classes collection
new_classes = [
    {
        'class_id': 'c2',
        'class_name': 'Home fusion made easy'
    },
    {
        'class_id': 'c3',
        'class_name': 'How to train an attack iguana'
    },
    {
        'class_id': 'c4',
        'class_name': 'Learn SQL for fun and profit'
    }
]

# classes_collection.insert_many(new_classes)
for class_ in new_classes:
    check = classes_collection.find_one({'class_id': class_['class_id']})
    if check == None:
        classes_collection.insert_one(class_)
    else:
        print(f"A class with the ID: {class_['class_id']} already exists")

# print all the data in classes collection
print(list(classes_collection.find()))
print()

# inserting new documents in the students collection
new_students = [
    {
        'student_id': 's2',
        'student_name': 'Rick'
    },
    {
        'student_id': 's3',
        'student_name': 'Susanna'
    },
    {
        'student_id': 's4',
        'student_name': 'Jennifer'
    }
]

# students_collection.insert_many(new_students)
for student in new_students:
    check = students_collection.find_one({'student_id': student['student_id']})
    if check == None:
        students_collection.insert_one(student)
    else:
        print(f"Student with the ID: {student['student_id']} already exists")

# print all the data in students collection
print(list(students_collection.find()))
print()

# inserting new documents in the grades collection
new_scores = [
    {
        'student_id': 's2',
        'grade' : {'c1': 99, 'c2': 38, 'c4': 63}
    },
    {
        'student_id': 's3',
        'grade' : {'c1': 65, 'c2': 88, 'c4': 75}
    },
    {
        'student_id': 's4',
        'grade' : {'c1': 3, 'c2': 48, 'c3': 32, 'c4': 20}
    }
]

for score in new_scores:
    check = grades_collection.find_one({'student_id': score['student_id']})
    if check == None:
        grades_collection.insert_one(score)
    else:
        print(f"Scores for student ID {score['student_id']} already exists")

#display all the data in grades collection
print(list(grades_collection.find()))
print()

# Query students who took the course ”Home fusion made easy”
result = list(classes_collection.find({'class_name': 'Home fusion made easy'}))
class_id = result[0]['class_id']

scores = list(grades_collection.find())
took_course = []
for student in scores:
    if class_id in student['grade']:
        result = list(students_collection.find({'student_id': student['student_id']}))
        name = result[0]['student_name']
        took_course.append(name)

print(f"The students who took the course ”Home fusion made easy” are {took_course}")
print()

# Query Jennifer’s grade on the course named ”Learn SQL for fun and profit.”
result = list(students_collection.find({'student_name': 'Jennifer'}))[0]
student_id = result['student_id']

result = list(classes_collection.find({'class_name': 'Learn SQL for fun and profit'}))[0]
class_id = result['class_id']

result = list(grades_collection.find({'student_id': 's4'}))[0]
score = result['grade'][class_id]
print(f"Jennifer's grade on the course ”Learn SQL for fun and profit” is {score}")
