import interface
import functions_book
from interface import Type_screen


def main():
    while True:
        interface.display_screen("START")
        interface.display_input("START")

        options = input()
        match options:
            case "1":
                interface.display_screen("INSERT")
                interface.display_input("FILL")
                book = interface.get_book()
                functions_book.add_book(book)

            case "2":
                if functions_book.verify_list_books():
                    functions_book.edit_book()
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.display_input("ENTER")

            case "3":
                if functions_book.verify_list_books():
                    functions_book.delete_book()
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.display_input("ENTER")

            case "4":
                if functions_book.verify_list_books():
                    functions_book.view_books()
                    interface.display_input("ENTER")
                else:
                    interface.default_screen(Type_screen.EMPTY.value)
                    interface.display_input("ENTER")


            case "5":
                interface.display_screen("EXIT")
                interface.display_input("EXIT")
                break

            case _:
                interface.display_screen("INVALID")
                interface.display_input("ENTER")


main()
