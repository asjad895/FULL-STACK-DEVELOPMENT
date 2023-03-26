class Book:
    def __init__(self,title,author,isbn,access_level):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.access_level=access_level
        self.checked_out_by=None
        
    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Access Level: {self.access_level}"
    
    def checkout(self, user):
        if not self.checked_out_by:
            self.checked_out_by = user
            #database for storing information
            print(f"{self.title} has been checked out by {user.username}")

    
    def return_book(self):
        self.checked_out_by = None
        #data base for storing information
        print(f"{self.title} has been returned to the library")


class User:
    def __init__(self, username, age, access_level):
        self.username = username
        self.age = age
        self.access_level = access_level
        self.books_checked_out = []
    
    def checkout_book(self, book):
        if self.access_level >= book.access_level:
            book.checkout(self)
            self.books_checked_out.append(book)
        else:
            print(f"You do not have permission to check out {book.title}")
    
    def return_book(self, book):
        if book in self.books_checked_out:
            book.return_book()
            self.books_checked_out.remove(book)
        else:
            print(f"You have not checked out {book.title}")
            



class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, isbn, access_level):
        book = {'title': title, 'author': author, 'isbn': isbn, 'access_level': access_level}
        self.books.append(book)
        print(f"{title} by {author} has been added to the library")

    def search_books(self, keyword):
        matches = []
        for book in self.books:
            if keyword in book['title'] or keyword in book['author']:
                matches.append(book)
        if len(matches) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for book in matches:
                print(Book(**book))
#we create a dictionary book with the book information, and append it to the books list of the Library class. 
#In the search_books method, we search for books using the title and author keys of the dictionaries in the books list.

#Also note that we define the __str__ method in the Book class, which returns a string representation of the book object. 
#In the search_books method, we create a Book object from the dictionary using the ** syntax, which unpacks the dictionary into keyword arguments,
 #and then print the string representation of the Book object
    def checkout_book(self, index, user):
        book = self.books[index]
        book.checkout(user)
        user.books_checked_out.append(book)
        print(f"{book.title} has been checked out by {user.username}")

    def return_book(self, index):
        book = self.books[index]
        book.return_book()
        user = book.checked_out_by
        user.books_checked_out.remove(book)
        print(f"{book.title} has been returned by {user.username}")
# Here, the checkout_book method takes an index parameter to select the book to checkout and a user parameter to specify the user 
# checking out the book. The method calls the checkout method of the selected Book object and adds the book to the books_checked_out list of 
# the user.

# The return_book method takes an index parameter to select the book to return. The method calls the return_book method of the selected Book 
# object and removes the book from the books_checked_out list of the user who checked it out.

# With these changes, you can allow the user to search for books, select a book, and checkout or return it using the checkout_book and return_book 
# methods of the Library class.

# Connect to the MySQL database
import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="data895@AS",
  database="FAMILY_SHARE"
)
fname='s'
lname='b'
email='c'
mob=123999999
user_name ='as'
password='12'
query = "INSERT INTO user_info (fname, lname, email, mob, user_name, password) VALUES (%s, %s, %s, %s, %s, %s)"
values = (fname, lname, email, mob, user_name, password)







library = Library('asjad')
print("adding a book")
library.add_book('nlp on urdu', 'asjad', '1', 1)
library.add_book('statistic for data science', 'asjad', '11', 2)
print("searching a book")
library.search_books('asjad')
try:
    # Execute the query and commit the changes
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    print("sucess")
except Exception as e:
    print("Error:", e)
    db.rollback()

