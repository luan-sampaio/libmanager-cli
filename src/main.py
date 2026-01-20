import interface
import functions_book
from interface import Type_screen, Type_input


def main():
    book_id = 0

    while True:
        interface.start_screen()
        options = interface.get_input()
        match options:
            case "1":
                interface.default_screen(Type_screen.INSERT.value, Type_input.FILL.value)
                if functions_book.add_book():
                    interface.display_sucess_message(book_id)
                    book_id += 1
            case "2":
                functions_book.edit_book(book_id)
            case "3":
                functions_book.delete_book(book_id)
                if book_id > 0:
                    book_id -= 1
            case "4":
                functions_book.view_books()
            case "5":
                interface.exit_message()
                break


main()
