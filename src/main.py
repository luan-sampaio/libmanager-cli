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
                print("Em manutenção!")
            case "3":
                print("Em manutenção!")
            case "4":
                print("Q")
                #view_books(book_id, list_of_books)
            case "5":
                break


def start_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("               LIBMANAGER v1.0")
    print("    =====================================")
    print()    
    print("         Escolha uma opção:")
    print()
    print("         [1] Cadastrar livro")
    print("         [2] Editar livro")
    print("         [3] Excluir livro")
    print("         [4] Visualizar livros")
    print("         [5] Sair do programa")
    print()
    print("    =====================================")
    print("    Digite sua opção abaixo: ")
    print("    > _", end="")


def get_input():
    while True:
        choice = input()
        match choice:
            case "1" | "2" | "3" | "4" | "5":
                return choice
            case _:
                handle_invalid_option_in_menu()
                input("     >_")
                start_screen()
                continue


def handle_invalid_option_in_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    =============== ERRO ================")
    print()
    print("               Opção inválida!")
    print()
    print("         Pressione [ENTER] para retornar")
    print("    =====================================")


def insert_book_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    ============= CADASTRO =============")
    print()
    print("            Preencha os dados abaixo.")
    print()
    print("     -------------------------------------")


def add_book(books): 
    print("     (Pressione [ENTER] para retornar)")

    title = input("     Insira o título do livro: ",)
    if title == "":
        return False

    author = input("     Insira o nome do autor: ")    
    date = input("     Insira o ano de lançamento do livro: ")


    book = {"title": title, "author": author, "date": date}
    books.append(book)

    return True


def display_sucess_message(id, list_of_books):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    ============= CADASTRO =============")
    print()
    print()
    print("                ID - TÍTULO")
    print("    ------------------------------------")
    print(f"                {id}  - {list_of_books[id]["title"]}   ")
    print()
    print()
    print("         Livro Cadastrado com sucesso!")
    print()
    print()
    print("    Pressione [ENTER] para retornar ao menu.")
    print("    =====================================")
    input()


#def view_books(id, list_of_books):
    

main()
