import os

def main():
    start_screen()
    options = get_input()
#    insert_book_screen()


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
    print("             Preencha os dados abaixo.")
    print()
    print("    =====================================")


main()
