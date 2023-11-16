students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def func(dictionary):
    interests = set(interest for student_id in students.keys() for interest in students[student_id]['interests'])
    surnamesLength = sum(len(students[student_id]['surname']) for student_id in students)
    return interests, surnamesLength

print(list(zip(students.keys(), [students[student_id]['age'] for student_id in students.keys()])))
print(func(students))
