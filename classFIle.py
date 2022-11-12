class Person:
    def __init__(self, name, age, exam):
        self.name = name
        self.age = age
        self.exam = exam

    def showDetails(self):
        print('My name is ', self.name)

    def examList(abc):
        print('User is eligible for this exam', abc.exam)


p1 = Person('Sanny', 23, 'UPSCC')
p1.showDetails()
p1.examList()

