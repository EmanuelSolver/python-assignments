class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print("Hi, I'm " + self.name + ", a "+ self.gender + ", and I'm " + str(self.age) + " years old.")
        
person1 = Person("Alice", 25, "female")
person1.introduce()
