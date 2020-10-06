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
        #first will check as 
