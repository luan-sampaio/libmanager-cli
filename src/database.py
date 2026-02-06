list_of_books = []


def save_book(book):
    list_of_books.append(book)
    return list_of_books


def show_list_of_books():
    return list_of_books


def remove_book(id_book):
    return list_of_books.pop(int(id_book))


def edit_book(book, id_book):
    if book.get("title"):
        list_of_books[id_book]["title"] = book.get("title")
    
    if book.get("author"):
        list_of_books[id_book]["author"] = book.get("author")

    if book.get("date"):
        list_of_books[id_book]["date"] = book.get("date")
        
        
