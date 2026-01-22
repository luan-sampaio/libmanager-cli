import os
import interface
import database
from interface import Type_screen, Type_input

AMOUNT_ATTRIBUTES_BOOK = 3


def add_book(book): 
    database.save_book(book)
    interface.default_screen(Type_screen.REGISTER.value)
    interface.default_screen_input( Type_input.ENTER.value)
    input()


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
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id()
    if choice == None:
        return 

    interface.default_screen(Type_screen.CONFIRM_DELETE.value)
    interface.show_book_by_list(choice, list_of_books)
    interface.default_screen_input(Type_input.EXCLUDE.value)

    if not interface.checks_delete():
        interface.default_screen(Type_screen.N_DELETE.value)
        interface.default_screen_input(Type_input.ENTER.value)
        input()
        return 
    

    book = database.remove_book(choice)
    
    interface.default_screen(Type_screen.DELETE_BOOK.value)
    interface.show_book(book)
    interface.default_screen_input(Type_input.ENTER.value)
    input()


def edit_book():
    list_of_books = database.show_list_of_books()

    interface.default_screen(Type_screen.EDIT.value)
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id()
    if choice == None:
        return 

    interface.default_screen(Type_screen.EDIT_BOOK.value)
    interface.show_book_by_list(choice, list_of_books)
    interface.default_screen_input(Type_input.EDIT_BOOK.value)

    book = interface.get_field_book()
    if not checks_book(book):
        interface.default_screen(Type_screen.N_EDIT.value)
        interface.default_screen_input(Type_input.ENTER.value)  
        input()      
        return 

    database.edit_book(book, choice)

    interface.default_screen(Type_screen.EDIT_OK.value)
    interface.default_screen_input(Type_input.ENTER.value)
    input()


def checks_book(book):
    count_empty = 0
    for value in book.values():
        if not value:
            count_empty += 1
    
    if count_empty == AMOUNT_ATTRIBUTES_BOOK:
        return False
    return True
