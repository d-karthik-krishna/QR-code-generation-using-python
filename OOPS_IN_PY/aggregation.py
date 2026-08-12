#Aggreagation : represents a relationship where one object (the whole)
                #contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

Lib = Library("INDIA, Public Library")

b1 = Book("Harry Potter","JK Rowling")
b2 = Book("the seasons of blossom","Korean author")
b3 = Book("BhuvaE","Karthik")

Lib.add_book(b1)
Lib.add_book(b2)
Lib.add_book(b3)

print(Lib.name)
print(Lib.list_books())
print()
for book in Lib.list_books():
    print(book,"\n")
