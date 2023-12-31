# 3.	Define a class called Lunch. Its __init__() method should have two arguments: self and menu.Where menu is a string. Add a method called menu_price. It will involve a if statement:
# •	if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
# To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().

class Lunch():
    def __init__(self, menu:str):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            print(f"Your choice: {self.menu} Price 12.00")
        elif self.menu == "menu 2":
            print(f"Your choice: {self.menu} Price 13.40")
        else:
            print("Error in menu")
            
Paul = Lunch("menu 1")
Paul.menu_price()

class Dinner(Lunch):
    def __init__(self, menu: str):
        # super().__init__(menu)
        self.menu = menu
        self.exp = Lunch("abc")

Micheal = Lunch('menu 2')
Paul = Dinner('menu 1')
print(Paul.menu)
print(Micheal.menu)
print(Paul.exp.menu)

class Night(Dinner, Lunch):
    def __init__(self, menu: str):
        super().__init__(menu)