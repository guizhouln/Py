# Coding = UTF-8
class SchoolMember:
    '''As any school's Members'''

    def __int__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell me about my details'''

        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''As a teacher'''

    def __init__(self, name, age, salary):
        SchoolMember.__int__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}'.format(self.salary))


class Student(SchoolMember):
    '''AS a student'''

    def __init__(self, name, age, marks):
        SchoolMember.__int__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {}'.format(self.marks))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Syivia', 24, 30000)
s = Student('Gui Zhou', 25, 75)

# Print a blank line
print()

members = [t, s]
for member in members:
    # work for all the teachers and students.
    member.tell()
