class Animal(object):
    def __init__(self, startname, age):
        self.name = startname #attribute1
        self.age = age #attribute2
    def description(self): #method1
        print("this is " + self.name)
        print("he/she is " + str(self.age) + "years old")