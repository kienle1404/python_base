# 5.	Define class Dog with the following requirements:
# Attributes:
# •	Name
# •	size
# •	Breed Default: ‘Unknown’
# •	Date of birth in DD/MM/YYYY format  Default: ‘Unknown’
# Methods:
# •	Bark
# o	This should get the dog to bark (print out the word ‘woof!’)
# •	get_name
# o	This should return the dog’s name
# •	set_name
# o	This should allow the user to set an alphabetical name between 2 and 30 characters.
# o	Convert the name to title case before setting
# •	dog_years
# o	This should calculate a dog’s age in dog years (use 1 year = 7 dog years)

class Dog:
    def __init__(self, name, size, breed='Unknown', dob='Unknown'):
        self.name = name
        self.size = size
        self.breed = breed
        self.dob = dob
        
    def Bark(self):
        print("woof!")
    
    def get_name(self):
        return self.name
    
    def set_name(self, name:str):
        print(f"previous name: {self.get_name()}")
        self.name = name.title()
        
    def dog_years(self):
        age = (2024 - int(self.dob[-4:])) * 7
        return age
    
    @staticmethod
    def rename(name: str):
        return name.upper()
    
    @classmethod
    def callname(cls):
        print(cls.rename())
    
# class method & static method
a = Dog("Cho", 3, 'Poodle', '07/01/2016')
a.Bark()
print(a.get_name())
a.set_name('meO')
print(a.get_name())
print(a.dog_years())
print(a.rename("sutu"))
print(a.callname())