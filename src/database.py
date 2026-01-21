list_of_books = []

def save_book(book):
    list_of_books.append(book)
    return list_of_books


def show_list_of_books():
    return list_of_books


def remove_book(id):
    list_of_books.pop(int(id))


