# Class -> Library
# Layers of abstraction -> display available books, to lend a book, to add a book
class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks 

    def displayAvailableBooks(self):
        print()
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('You have now borrowed the book')
            self.availableBooks.remove(requestedBook)
        else:
            print('Sorry! The book is not available at the moment!')

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book. Thank you!!!')


# Class -> Customer
# Layers of abstraction -> request for a book, return a book
class Customer:
    def requestBook(self):
        print('-->Enter the name of a book you would like to borrow: ') 
        self.book = input()
        return self.book

    def returnBook(self):
        print(' -->Enter the name of the book you are returning: ')
        self.book = input()
        return self.book

# Main Program
library = Library(['- Think and Grow rich', '- For one more Day', '- Who will cry when you Die'])
customer = Customer() 
while True: 
    print('Enter 1 to display the available books')
    print('Enter 2 to request for a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit the program')
    userChoise = int(input('Option: '))
    if userChoise == 1:
        library.displayAvailableBooks()

    elif userChoise == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)

    elif userChoise == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)  # Add the book back to a library
    elif userChoise == 4:
        quit()