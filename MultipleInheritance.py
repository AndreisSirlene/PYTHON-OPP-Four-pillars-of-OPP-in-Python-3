# Here we will have 3 class, the first 2 will be the basic class of your third class
class OperatingSystem:
    multitasking = True
    name = 'Mac Os'

class Apple:
    website ='www.apple.com'
    name = 'Apple'
#Its possible to see that the program read 'MacOs instead of 'Apple',
# in case there is a conflict as the same attribute (name) this happends 
# because dependes of the order of the inheritance below.
class MacBook(OperatingSystem, Apple): 
    def __init__(self): 
        if self.multitasking is True:
            print(f'This is a multi tasking system. Visit {self.website} for more details.')
            print('Name: ',self.name)

macBook = MacBook()           