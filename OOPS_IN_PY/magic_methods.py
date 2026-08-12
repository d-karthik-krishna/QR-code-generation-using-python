# methods having __ is called as magic methods, such as __init__
class Book:
    
    def __init__(self, title, author, noPages):
        self.title = title
        self.author = author
        self.noPages = noPages
    
    def __str__(self): #used to get the data which is declared in the obj instead of its memory address
        return f"{self.title} by {self.author} has {self.noPages} pages"
    
    def __eq__(self, other):
        return self.title == other.title 
    
    def __lt__(self, other):
        return self.noPages< other.noPages
    
    def __add__(self, other):
        return self.noPages + other.noPages # other operators also can be used here lik e-+*
    
    def __contains__(self, item):
        # return True if item is in title or author
        return item in self.title or item in self.author
    
book1 = Book("KJJHI","HUGHKJHK",10000)
book2 = Book("shddfkj","ausgdfk",12000)
book3 = Book("sidfhio","asddifhi",5000)

print(book1)
print(book2 == book3)
print(book3<book1)
print(book3+book1)
print("KJJHI" in book1)