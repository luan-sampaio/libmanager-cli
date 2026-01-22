import os
import interface
import database
from interface import Type_screen, Type_input


def add_book(book): 
    database.save_book(book)
    interface.default_screen(Type_screen.REGISTER.value)
    interface.default_screen_input( Type_input.ENTER.value)
    input()
    return True


def view_books():
    list_of_books = database.show_list_of_books()
    interface.default_screen(Type_screen.VIEW.value)
    interface.show_list_books(list_of_books)


def verify_list_books():
    list_of_books = database.show_list_of_books()
    if not len(list_of_books):
        return False
    return True


def delete_book(book_id):
    list_of_books = database.show_list_of_books()

    interface.default_screen(Type_screen.DELETE.value)
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id(book_id)
    if choice == None:
        return 

    interface.default_screen(Type_screen.CONFIRM_DELETE.value)
    interface.show_book(choice, list_of_books)
    interface.default_screen_input(Type_input.EXCLUDE.value)

    if not interface.checks_delete():
        return 
    
    database.remove_book(choice)


def edit_book(max_id):
    list_of_books = database.show_list_of_books()

    interface.default_screen(Type_screen.EDIT.value)
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id(max_id)
    if choice == None:
        return 

    interface.default_screen(Type_screen.EDIT_BOOK.value)
    interface.show_book(choice, list_of_books)
    interface.default_screen_input(Type_input.EDIT_BOOK.value)

    book = interface.get_field_book()
    database.edit_book(book, choice)

    interface.default_screen(Type_screen.EDIT_OK.value)
    interface.default_screen_input(Type_input.ENTER.value)
    input()
