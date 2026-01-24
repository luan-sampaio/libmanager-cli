import interface
import database
from interface import Type_screen

AMOUNT_ATTRIBUTES_BOOK = 3


def add_book(book): 
    if not checks_empty_title(book):
        return

    database.save_book(book)
    interface.default_screen(Type_screen.REGISTER.value)
    interface.display_input("ENTER")



def view_books():
    list_of_books = database.show_list_of_books()
    interface.default_screen(Type_screen.VIEW.value)
    interface.show_list_books(list_of_books)


def verify_list_books():
    list_of_books = database.show_list_of_books()
    if not len(list_of_books):
        return False
    return True


def delete_book():
    list_of_books = database.show_list_of_books()

    interface.default_screen(Type_screen.DELETE.value)
    interface.display_input("EDIT")


    choice = interface.get_id()
    if choice == None:
        return 

    interface.default_screen(Type_screen.CONFIRM_DELETE.value)
    interface.show_book_by_list(choice, list_of_books)
    interface.display_input("EXCLUDE")

    if not interface.checks_delete():
        interface.default_screen(Type_screen.N_DELETE.value)
        interface.display_input("ENTER")

        return 
    

    book = database.remove_book(choice)
    
    interface.default_screen(Type_screen.DELETE_BOOK.value)
    interface.show_book(book)
    interface.display_input("ENTER")



def edit_book():
    list_of_books = database.show_list_of_books()

    interface.display_screen("EDIT")
    interface.display_input("EDIT")

    choice = interface.get_id()
    if choice == None:
        return 

    interface.default_screen(Type_screen.EDIT_BOOK.value)
    interface.show_book_by_list(choice, list_of_books)
    interface.display_input("EDIT_BOOK")

    book = interface.get_field_book()
    if not checks_book(book):
        interface.default_screen(Type_screen.N_EDIT.value)
        interface.display_input("ENTER")
        return 

    database.edit_book(book, choice)

    interface.default_screen(Type_screen.EDIT_OK.value)
    interface.display_input("ENTER")


def checks_book(book):
    count_empty = 0
    for value in book.values():
       if not value:
            count_empty += 1
    
    if count_empty == AMOUNT_ATTRIBUTES_BOOK:
        return False
    return True


def checks_empty_title(book):
    try:
        book.get("title")
    except AttributeError:
        return False    
    return True
