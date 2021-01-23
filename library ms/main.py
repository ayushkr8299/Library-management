from app import *

user='''Hi Welcome to LMS-:
    Enter your choice:
        A- Add the Book
        L - List all the books             
        R- Mark Book as read
        D- Delete the book
        Q- Quit the application
    now enter your choice : '''


def menu():
    choices=input(user)

    while choices.upper() != "Q":
        if choices.upper() == "A":
            add_book_prompt()
        elif choices.upper() == "L":
            list_book_prompt()
        elif choices.upper() == "R":
            mark_book_prompt()        
        elif choices.upper() == "D":
            delete_book_prompt()
        choices=input("enter the another choice: ")        

def add_book_prompt():
     book_name=input("enter the book name : ")
     author_name=input("enter the author name : ")
     add_book(book_name,author_name)
    
def list_book_prompt():
    list_book()
    book_search_name=input("enter the book name you want to search the book : ")
    book_search(book_search_name)
     
def mark_book_prompt():
    list_book()
    mark_book=input(" enter the book name you want to mark as read : ")
    mark_book_fn(mark_book)

    
def delete_book_prompt():
    list_book()
    delete_book=input(" enter the book you want to delete : ")
    delete_book_fn(delete_book)
    

menu()

