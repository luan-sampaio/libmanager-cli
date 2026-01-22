list_of_books = []


def save_book(book):
    list_of_books.append(book)
    return list_of_books


def show_list_of_books():
    return list_of_books


def remove_book(id):
    list_of_books.pop(int(id))


def edit_book(book, id):
    list_of_books[id]["title"] = book.get("title")
    list_of_books[id]["author"] = book.get("author")
    list_of_books[id]["date"] = book.get("date")

