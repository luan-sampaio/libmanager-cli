import os
import interface
import database
from interface import Type_screen, Type_input

def add_book(book): 
    database.save_book(book)
    return True


def view_books():
    list_of_books = database.show_list_of_books()
    if not list_of_books:
        return False

    interface.default_screen(Type_screen.VIEW.value)
    interface.show_list_books(list_of_books)
    return True


def verify_list_books():
    list_of_books = database.show_list_of_books()
    if not len(list_of_books):
        return False
    return True


def delete_book(book_id):
    interface.default_screen(Type_screen.DELETE.value)
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id(book_id)

    interface.default_screen(Type_screen.CONFIRM_DELETE.value)
    interface.default_screen_input(Type_input.EXCLUDE.value)

    if not interface.checks_delete():
        return 
    
    database.remove_book(choice)


def edit_book(max_id):
    list_of_books = database.show_list_of_books()
    if not len(list_of_books):
        interface.default_screen(Type_screen.EMPTY.value)
        interface.default_screen_input(Type_input.ENTER.value)
        input()
        return 

    interface.default_screen(Type_screen.EDIT.value)
    interface.default_screen_input(Type_input.EDIT.value)

    choice = interface.get_id(max_id)
    if not choice:
        return 

    choice = int(choice)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EDIÇÃO ':=^40}\n\n")
    print(" " * 4 + "Título: " + f"{list_of_books[choice].get('title')}")
    print(" " * 4 + "Autor: " + f"{list_of_books[choice].get('author')}")
    print(" " * 4 + "Data: " + f"{list_of_books[choice].get('date')}\n\n")
    print(f"{'Se não for alterar, pressione [ENTER]':^48}")
    print(" " * 4 + "-" * 40)

    
    title = input(" " * 4 + "Digite o título: ")
    if title:
        list_of_books[choice]["title"] = title

    author = input(" " * 4 + "Digite o autor: ")
    if author:
        list_of_books[choice]["author"] = author
        
    date = input(" " * 4 + "Digite o ano: ")
    if date:
        list_of_books[choice]["date"] = date

    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40 + "\n\n")
    print(f"{'Livro editado com sucesso!':^48}\n\n")    
    print(" " * 4 + 'Pressione [ENTER] para retornar ao menu')
    print(" " * 4 + "=" * 40)
    input()
