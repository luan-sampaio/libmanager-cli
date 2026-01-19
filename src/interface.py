import os
import database

def start_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'LIBMANAGER v1.0':^48}")
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
    print(" " * 4 + f"{' ERRO ':=^40}\n")
    print(f"{'Opção inválida!':^48}\n\n\n")
    print("\tPressione [ENTER] para retornar")
    print(" " * 4 + "=" * 40)


def insert_book_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' CADASTRO ':=^40}\n\n")
    print(f"{'Preencha os dados abaixo.':^48}\n\n")
    print(" " * 4 + "-" * 40)


def display_sucess_message(id):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' CADASTRO ':=^40}")
    print("\n\n")
    print("\t\tID - TÍTULO")
    print(" " * 4 + "-" * 40)
    list_of_books = database.show_list_of_books()

    print(f"\t\t{id}  - {list_of_books[id]['title']}   ")
    print("\n")
    print(f"{'Livro Cadastrado com sucesso!':^48}")
    print("\n")
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu.")
    print(" " * 4 + "=" * 40)
    input()


def exit_message():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40 + "\n\n")
    print(f"{'Obrigado por usar o sistema!':^48}\n\n")
    print(" " * 4 + "=" * 40)


def delete_book_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EXCLUIR ':=^40}\n\n")
    print(f"{'Digite o ID do livro que deseja excluir!':^48}\n")
    print(" " * 4 + "(Pressione [ENTER] para retornar)")
    print(" " * 4 + "=" * 40)
    print(" " * 4 + "> _", end="")


def message_of_invalid_input():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' ERRO ':=^40}\n")
    print(f"{'ID inexistente!':^48}\n")
    print(f"{'Acesse a lista de livros':^48}")
    print(f"{'para consultar o id do livro desejado.':^48}\n\n")
    print('\tPressione [ENTER] para retornar ao menu')
    print(" " * 4 + "=" * 40)
    input()


def screen_edit_book():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EDIÇÃO ':=^40}\n\n")
    print(f"{'Digite o ID do livro que deseja editar!':^48}\n")
    print(" " * 4 + "(Pressione [ENTER] para retornar)")
    print(" " * 4 + "=" * 40)
    print(" " * 4 + "> _", end="")


def confirm_deletion(id, books):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EXCLUIR ':=^40}\n\n")
    print(f"{'ATENÇÃO: Esta ação não pode ser defesfeita!':^48}\n")    
    print(" " * 4 + "=" * 40 + "\n")
    print(" " * 4 + "Livro: " + books[id].get('title'))
    print(" " * 4 + "Livro: " + books[id].get('author') + '\n')
    print(" " * 4 + "> Para confirmar, digite 'DELETAR' ou ")
    print(" " * 4 + "pressione [ENTER] para retornar ao ")
    print(" " * 4 + "MENU: _", end="")

    choice = input()
    if choice == "DELETAR":
        return True
    return False


def display_sucess_delete():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40 + "\n\n")
    print(f"{'Livro deletado com sucesso!':^48}\n\n")    
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu")
    print(" " * 4 + "=" * 40)


def get_id(max_id):
    choice = input()

    if not choice.isdigit():
        message_of_invalid_input()
        return 
    
    if not 0 <= int(choice) < int(max_id):
        message_of_invalid_input()
        return

    return choice


def screen_edit_book():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EDIÇÃO ':=^40}\n\n")
    print(f"{'Digite o ID do livro que deseja editar!':^48}\n")
    print(" " * 4 + "(Pressione [ENTER] para retornar)")
    print(" " * 4 + "=" * 40)
    print(" " * 4 + "> _", end="")
