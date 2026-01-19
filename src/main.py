import os
import interface
import functions_book


def main():
    book_id = 0

    while True:
        interface.start_screen()
        options = interface.get_input()
        match options:
            case "1":
                interface.insert_book_screen()
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
