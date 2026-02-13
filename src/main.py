import interface
import functions_book
import sys


def main():
    if sys.argv[0] != "src/main.py":
        sys.exit("Use python src/main.py")
    
    while True:
        interface.display_screen("START")
        interface.display_input("START")

        options = input()
        match options:
            case "1":
                interface.display_screen("INSERT")
                functions_book.add_book()

            case "2":
                if functions_book.verify_list_books():
                    functions_book.edit_book()
                else:
                    interface.display_screen("EMPTY")

                    interface.display_input("ENTER")

            case "3":
                if functions_book.verify_list_books():
                    functions_book.delete_book()
                else:
                    interface.display_screen("EMPTY")

                    interface.display_input("ENTER")

            case "4":
                if functions_book.verify_list_books():
                    functions_book.view_books()
                    interface.display_input("ENTER")
                else:
                    interface.display_screen("EMPTY")
                    interface.display_input("ENTER")

            case "5":
                interface.display_screen("EXIT")
                interface.display_input("EXIT")
                break

            case _:
                interface.display_screen("INVALID")
                interface.display_input("ENTER")


main()
