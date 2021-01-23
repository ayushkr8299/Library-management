books=[]

def add_book(name,author):
    read=False
    books.append([name,author,read])
    print(books)

def list_book():
    print("here is the last of book : ")
    for i in range(len(books)):
        print(f'{i+1}. {books[i][0]}')    

def book_search(book_search):
    for i in range(len(books)):
        if book_search == books[i][0]:
            print(f' book_name: {books[i][0]} \n author_name: {books[i][1]} \n read_status: {books[i][2]}')

def mark_book_fn(mark_book_name):
    for i in range(len(books)):
        if mark_book_name == books[i][0] :
            books[i][2] = True
            print(books[i])

def delete_book_fn(delete_book_name):
    for i in range(len(books)):
        if delete_book_name == books[i][0] :
            books.pop(i)
            print(books)
            break


