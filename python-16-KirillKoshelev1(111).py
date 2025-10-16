class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def fullname(self):
        return f"{self.name} {self.surname}"
    
    @fullname.setter
    def fullname(self, value):
        self.name, self.surname = value
        
person = Person('Mike', 'Pondsmith')
print(person.name)        
print(person.surname)     
print(person.fullname)    