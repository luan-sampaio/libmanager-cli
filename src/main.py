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
                functions_book.add_book(book)

            case "2":
                if functions_book.verify_list_books():
                    functions_book.edit_book()
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.default_screen_input(Type_input.ENTER.value)
                    input()

            case "3":
                if functions_book.verify_list_books():
                    functions_book.delete_book()
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.default_screen_input(Type_input.ENTER.value)
                    input()

            case "4":
                if functions_book.verify_list_books():
                    functions_book.view_books()
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
                #interface.default_screen(Type_screen.INVALID.value)
                #interface.default_screen_input(Type_input.ENTER.value)
                interface.display_screen("INVALID")
                interface.display_input("ENTER")
                #input()


main()
