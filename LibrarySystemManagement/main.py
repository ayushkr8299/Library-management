import Ayush.LibrarySystemManagement.app as operations

user = '''HII WELCOME TO LIBRARY SYSTEM MANAGEMENT

        Enter your choices :
         A - Add the book
         L - List all the book
         M - Mark all the book
         D - Delete the book
         Q - Quite the application

         NOW ENTER YOUR CHOICES HERE : '''

def menu():
    choices = input(user)

    while choices.upper() != "Q" :
        if choices.upper() == "A" :
            add_book_prompt()
        elif choices.upper() == "L" :
            list_book_prompt()
        elif choices.upper() == "M" :
            mark_book_prompt()
        elif choices.upper() == "D" :
            delete_book_prompt()
        choices = input("Enter the another choice : ")

def add_book_prompt():
    book_name = input("Enter the book name : ")
    author_name = input("Enter the author name : ")
    operations.add_book(book_name,author_name)

def list_book_prompt():
    list_call= operations.list_book()
    for i in range(len(list_call)):
        if list_call[i]['read'] == "False":
            read_s = "No"
        elif list_call[i]['read'] == "True":
            read_s = "Yes"
        detail = (str(i+1) + ". " + "Book name : " + list_call[i]['name'] + "\n" + "   Author name : " + list_call[i]['author'] + "\n" + "   read : " + read_s + "\n")
        print(detail)

def mark_book_prompt():
    list_book_prompt()
    book_name = input("Enter the book name you want to a mark : ")
    operations.mark_book(book_name)

def delete_book_prompt():
    list_book_prompt()
    book_name = input("Enter the book you want to delete : ")
    operations.delete_book(book_name)


menu()