class Gateshead:

    def __init__(self, name, number, interest):
        self.name = name
        self.number = number
        self.interest = interest


class Student(Gateshead):

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.number)

    def get_interest(self):
        print(self.interest)


students = [
    Student('Mehdi', '20001052', 'coding'),
    Student('Jack', '19002616', 'bird_watching'),
    Student('Ryan', '19002096', 'Gym'),
    Student('Aaron', '558357', 'Gym'),
    Student('Leo','21004716', 'Burgers')
]

student_number = input('Enter your student_number: ')

for _ in range(len(students)):
    if student_number == students[_].number:
        print(students[_].name, students[_].number, students[_].interest)
        break
else:
    print('Not Found')