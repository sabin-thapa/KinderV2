
class Teacher:

    def __init__(self,first,last,contact):
        self.first = first
        self.last = last
        self.contact = contact

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def __repr__(self):
        return "Teacher('{}', '{}', '{}')".format(self.first, self.last, self.contact)