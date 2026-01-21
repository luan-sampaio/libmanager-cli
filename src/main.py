import interface
import functions_book
from interface import Type_screen, Type_input


def main():
    book_id = 0

    while True:
        interface.default_screen(Type_screen.START.value)
        interface.default_screen_input(Type_input.START.value)

        options = input()
        match options:
            case "1":
                interface.default_screen(Type_screen.INSERT.value)
                interface.default_screen_input(Type_input.FILL.value)
                book = interface.get_book()
                if functions_book.add_book(book):
                    interface.default_screen(Type_screen.REGISTER.value)
                    interface.default_screen_input( Type_input.ENTER.value)
                    input()
                    book_id += 1

            case "2":
                functions_book.edit_book(book_id)

            case "3":
                if functions_book.verify_list_books():
                    interface.default_screen(Type_screen.DELETE.value)
                    interface.default_screen_input(Type_input.EDIT.value)
                    choice = interface.get_id(book_id)
                    interface.default_screen(Type_screen.CONFIRM_DELETE.value)
                    interface.default_screen_input(Type_input.EXCLUDE.value)
                    
                    functions_book.delete_book(choice)
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.default_screen_input(Type_input.ENTER.value)
                    input()

                if book_id > 0:
                    book_id -= 1

            case "4":
                if functions_book.view_books():
                    interface.default_screen_input(Type_input.ENTER.value)
                    input()
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.default_screen_input(Type_input.ENTER.value)
                    input()

            case "5":
                interface.default_screen(Type_screen.EXIT.value)
                interface.default_screen_input(Type_input.EXIT.value)
                break

            case _:
                interface.default_screen(Type_screen.INVALID.value)
                interface.default_screen_input(Type_input.ENTER.value)
                input()


main()
