import random
import cmath

class PERSON(object):
    age = None
    name = None
    gender = None
    def __init__(self, name=None, gender=None):
        self.age=random.randrange(17,26)
        if gender is None:
            self.gender= random.choices(['male','female'])
        if name is None:
            self.name='default name'

class STUDENT(PERSON):
    id = None
    room = None
    grade = None
    def __init__(self, number,grade,room):
        super()
        super().__init__()
        self.id = number
        self.grade = grade
        self.room = room
    @property
    def age(self):
        return super().age