import os

def main():
    start_screen()
    get_input = input()
    insert_book_screen()


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


def insert_book_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    ============= CADASTRO =============")
    print()
    print("             Preencha os dados abaixo.")
    print()
    print("    =====================================")


main()
