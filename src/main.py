import os


def main():
    list_of_books = []
    book_id = 0

    while True:
        start_screen()
        options = get_input()
        match options:
            case "1":
                insert_book_screen()
                if add_book(list_of_books):
                    display_sucess_message(book_id, list_of_books)
                    book_id += 1
            case "2":
                continue
            case "3":
                continue
            case "4":
                view_books(list_of_books)
            case "5":
                exit_message()
                break


def start_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{"LIBMANAGER v1.0":^48}")
    print(" " * 4 + "=" * 40 + "\n")
    print("\tEscolha uma opção:\n")
    print("\t[1] Cadastrar livro")
    print("\t[2] Editar livro")
    print("\t[3] Excluir livro")
    print("\t[4] Visualizar livros")
    print("\t[5] Sair do programa\n")
    print(" " * 4 + "=" * 40)
    print(" " * 4 + "Digite sua opção abaixo: ")
    print(" " * 4 + "> _", end="")


def get_input():
    while True:
        choice = input()
        match choice:
            case "1" | "2" | "3" | "4" | "5":
                return choice
            case _:
                handle_invalid_option_in_menu()
                input()
                start_screen()
                continue


def handle_invalid_option_in_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{" ERRO ":=^40}\n")
    print(f"{"Opção inválida!":^48}\n\n\n")
    print("\tPressione [ENTER] para retornar")
    print(" " * 4 + "=" * 40)


def insert_book_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{" CADASTRO ":=^40}\n\n")
    print(f"{"Preencha os dados abaixo.":^48}\n\n")
    print(" " * 4 + "-" * 40)


def add_book(books): 
    print(" " * 4 + "(Pressione [ENTER] para retornar)")

    title = input(" " * 4 + "Insira o título do livro: ",)
    if not title:
        return False

    author = input(" " * 4 + "Insira o nome do autor: ")    

    while True:
        date = input(" " * 4 + "Insira o ano de lançamento do livro: ")
        if date.isdigit():
            break


    book = {"title": title, "author": author, "date": date}
    books.append(book)

    return True


def display_sucess_message(id, list_of_books):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{" CADASTRO ":=^40}")
    print("\n\n")
    print("\t\tID - TÍTULO")
    print(" " * 4 + "-" * 40)
    print(f"\t\t{id}  - {list_of_books[id]["title"]}   ")
    print("\n")
    print(f"{"Livro Cadastrado com sucesso!":^48}")
    print("\n")
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu.")
    print(" " * 4 + "=" * 40)
    input()


def view_books(list_of_books):
    os.system('cls' if os.name == 'nt' else 'clear')

    count = 0
    print(" " * 4 + f"{" CONSULTA ":=^40}")
    print("\n\n")
    print(" " * 4 + f"{'ID':<4}{'TÍTULO':<15}{'AUTOR':<10}{'ANO'}")
    print(" " * 4 + "-" * 40)
    
    for book in list_of_books:
        print(" " * 4 +  f"{count:<4}{book.get("title"):<15}{book.get("author"):<10}{book.get("date")}")
        count += 1
    
    print("\n\n")
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu.")
    print(" " * 4 + "=" * 40)
    input()
    

def exit_message():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40 + "\n\n")
    print(" " * 4 + "Obrigado por usar o sistema!\n\n")
    print(" " * 4 + "=" * 40)


main()
