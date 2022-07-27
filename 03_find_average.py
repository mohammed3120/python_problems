def avg(students, name):
    print(students)
    marks = students[name]
    print(sum(marks)/len(marks))

if __name__ == "__main__":
    students = {'Harry': [10,20, 37.21], 'Berry': [30,40, 39.21], 'Tina': [50,70, 65.21], 'Akriti': [65,55, 43.21], 'Harsh': [2,7, 0.21]}
    name = 'Berry'
    avg(students, name)