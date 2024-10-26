'''
Magnus Chiu
CIS 41A Spring 2022
Unit I Problem I
'''
class LibraryPatron:
    def __init__(self, name):
        self.name = name
        self.bookCheckedOut = []
        
    def checkOutBook(self, checkOutLimit, bookTitle):
        if (len(self.bookCheckedOut) < checkOutLimit):
            print(self.name, "has checked out", bookTitle[0])
            (self.bookCheckedOut).append(bookTitle[0])
        else:
            print("Sorry",self.name,"you are at your limit of", checkOutLimit)
            
    def returnBook(self, book):
        (self.bookCheckedOut).remove(book[0])
        print(self.name,"has returned", book[0])
        
    def printCheckedOutBooks(self):
        print(self.name,"has the following books checked out:")
        for i in self.bookCheckedOut:
            print(i)
class AdultPatron(LibraryPatron):
    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 4
    
    def checkOutBook(self, book):
        LibraryPatron.checkOutBook(self, self.checkOutLimit, book)
        
class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 2
    
    def checkOutBook(self, book):
        if (book[1] == "Juvenile"):
            LibraryPatron.checkOutBook(self, self.checkOutLimit, book)
        else:
            print("Sorry", self.name, book[0],"is an adult book")
        
book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")
        
patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()

'''
Execution results:
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
'''