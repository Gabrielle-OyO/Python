


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%sxxx%s.' % (self.name, course_name))
    def watch_movie(self):
        if self.age < 18:
            print('%saaa.' % self.name)
        else:
            print('%sdddd.' % self.name)