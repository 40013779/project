'''class member'''
class Member():# pylint: disable=too-few-public-methods
    '''class member'''
    def __init__(self, name):
        self.full_name = name
    def introduce(self):
        '''introduction'''
        print(f'Hi, I\'m {self.full_name}!')
class Student(Member):# pylint: disable=too-few-public-methods
    '''student'''
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason
payvand = Student('Payvand', 'Money')
class Instructor(Member):
    '''instructor'''
    def __init__(self, name, bio, skillset):
        super().__init__(name)
        self.bio = bio
        self.skillset = skillset
    def add_skill(self, skill):
        '''adding skills'''
        self.skillset.append(skill)
brandon = Instructor('Brandon', 'I am a genius', ['React', 'Node', 'C'])
class Workshop():
    '''workshop'''
    def __init__(self, date, subject, instructors, students):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students
    def add_participant(self, participant):
        '''participants'''
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)
    def print_details(self):
        '''printing details'''
        print(f'Date: {self.date}\nSubject: {self.subject}\n')
        print('Instructors:')
        for i in self.instructors:
            print(f'\n{i.full_name}\n{i.bio}')
            print('Skills:')
            for skill in i.skillset:
                print(skill)
        print('\nStudents:')
        for students in self.students:
            print(f'\n{students.full_name}\n{students.reason}\n')
sei = Workshop('12/12/19', 'SEI', [], [])
sei.add_participant(brandon)
sei.add_participant(payvand)
sei.print_details()
