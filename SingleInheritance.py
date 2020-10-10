class Apple:    # Basic class
    manufacturer = 'Apple Inc.'
    contactWebsite = 'www.apple.com/contact'

    def contactDetails(self):
        print('To contact us, log on to' , self.contactWebsite)

class MacBook(Apple):     #Derivative class
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print(f'This MacBook was manufactured in {self.yearOfManufacture} by {self.manufacturer}') 
#first will check if self.manufacturer is present as an instance attribute when found
#out that is not, next sptep is check if is a class attribute, by found out is not. Will go and 
#check in your base class which has inheritance, so the value present there will be printed.
macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()