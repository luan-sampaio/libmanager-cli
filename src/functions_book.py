import interface
import database

from api_client import get_book_api

AMOUNT_ATTRIBUTES_BOOK = 3
AUTO = "1"


def add_book(option):
    interface.display_screen("INSERT")
    
    if option == AUTO:
        interface.display_input("FILL")
        
        title = interface.get_title()
        if not title:
            return
            
        book = get_book_api(title)
    else:
        interface.display_input("FILL")
        book = interface.get_book()
    
    if book == "NOT API":
        return
    if not book:
        interface.display_screen("ERROR_BOOK")
        interface.display_input("ENTER")
        return

    database.save_book_csv(book)
    interface.display_screen("REGISTER")
    interface.display_input("ENTER")


def view_books():
    interface.display_screen("VIEW")
    database.show_table_of_books()


def verify_list_books():
    list_of_books = database.show_list_of_books()
    if not list_of_books:
        return False
    return True


def delete_book():
    list_of_books = database.show_list_of_books()

    interface.display_screen("DELETE")
    interface.display_input("EDIT")

    choice = interface.get_id()
    if choice is None:
        return

    interface.display_screen("CONFIRM_DELETE")
    interface.show_book_by_list(choice, list_of_books)
    interface.display_input("EXCLUDE")

    if not interface.checks_delete():
        interface.display_screen("N_DELETE")
        interface.display_input("ENTER")
        return

    book = database.remove_book(choice)

    interface.display_screen("DELETE_BOOK")
    interface.show_book(book)
    interface.display_input("ENTER")


def edit_book():
    list_of_books = database.show_list_of_books()

    interface.display_screen("EDIT")
    interface.display_input("EDIT")

    choice = interface.get_id()
    if choice is None:
        return

    interface.display_screen("EDIT_BOOK")
    interface.show_book_by_list(choice, list_of_books)
    interface.display_input("EDIT_BOOK")

    book = interface.get_field_book()
    if not checks_book(book):
        interface.display_screen("N_EDIT")
        interface.display_input("ENTER")
        return

    database.edit_book(book, choice)

    interface.display_screen("EDIT_OK")
    interface.display_input("ENTER")


def checks_book(book):
    count_empty = 0
    for value in book.values():
        if not value:
            count_empty += 1

    if count_empty == AMOUNT_ATTRIBUTES_BOOK:
        return False
    return True
