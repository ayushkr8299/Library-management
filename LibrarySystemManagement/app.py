
def add_book(name,author):
    read = False
    with open("books.txt", "a" ) as books:
        books.write(name + "," + author + "," + str(read) + "\n")

def list_book():
    with open("books.txt", "r") as books:
        line = books.readlines()
        books = [line.strip().split(",") for line in line]
    book_list = []
    for book in books:
        book_list.append({'name' : book[0],'author' : book[1],'read' : book[2]})
    return  book_list


def mark_book(book_name):
    books_call = list_book()
    for book in books_call:
        if book['name'] == book_name :
            book['read'] = True
    with open("books.txt", "w") as books:
        for book in books_call:
            books.write(book['name'] + "," + book['author'] + "," + str(book['read']) + "\n")

def delete_book(book_name):
    books_call = list_book()
    with open("books.txt", "w") as books :
        pass
    for book in books_call:
        if book['name'] != book_name :
            with open("books.txt", "a") as books:
                books.write(book['name'] + "," + book['author'] + "," + str(book['read']) + "\n")




















