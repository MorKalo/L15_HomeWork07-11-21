#create a Book class. now, create an instance of your favorite book with the following data fields: title
# , author, genre, year_of_publish, no_of_pages (1) create the instance data using dictionary
# [for example: myBook.__dict__[‘year_of_publish’] = 1961] (2) create the instance data using dot
# [for example: myBook.title = ‘catch 22’] (3) create a method which creates a new books instance and data
# (see the create_Person method we did in lesson)
#create a UML for your book class
# *etgar: create a list of 3 three books. now create a dictionary which contains these 3 books where
# the key is the book- title and the value is the book instance.
# now input a string from the user (the title) and try to pop the book out of the dictionary using the title as the key
# (and print the book.__dict__ you just poped)

class Book:
    pass
mybook=Book()
mybook.__dict__['title']='i didnt read'
mybook.__dict__['author']='mor k.moshe'
mybook.__dict__['genre']='something'
mybook.__dict__['year_of_publish']='1987'
mybook.__dict__['no_of_page']='198'


mybook2=Book()
mybook2.title='i didnt read again'
mybook2.author='somebody'
mybook2.genre='love'
mybook2.year_of_publish='1986'
mybook2.no_of_page='23'

class Book:
    pass

def create_mybook(title, author, genre, year_of_publish, no_of_page):
    new_book = Book()
    new_book.title = title
    new_book.author =author
    new_book.genre = genre
    new_book.year_of_publish = year_of_publish
    new_book.no_of_page = no_of_page
    return new_book

my_book_fun = create_mybook('Harry Potter and the Sorcerer\'s Stone',
                            'J.K.rowling'
                          , 1999, 'fantazy', 1003)
print(my_book_fun.__dict__)

book_lst=['i didnt read', 'i didnt read again', 'Harry Potter and the Sorcerer\'s Stone' ]

# create a class Car. now create a new instance and generate data fields for the car as you like

print('******************************************* /')
print('Car')

class Car:
    pass

mycar=Car()
mycar.color='red'
mycar.year='2015'

print(mycar.__dict__)