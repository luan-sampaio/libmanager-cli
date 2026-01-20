import os
import database

from enum import Enum

SPACING = " " * 4
SPACING_EQUAL_SIGN = " " * 4 + "=" * 40 + "\n"
SPACING_MINUS_SIGN = " " * 4 + "-" * 40 + "\n"


class Type_screen(Enum):
    INVALID = 0
    INSERT = 1
    EXIT = 2
    EDIT = 3
    START = 4
    DELETE = 5
    INVALID_INPUT = 6


class Type_input(Enum):
    ENTER = 0
    FILL = 1
    EXIT = 2
    EDIT = 3
    START = 4


list_screen = [
    [" ERRO ", "Opção inválida!"],
    [" CADASTRO "],
    [""],
    [" EDIÇÃO ", "Digite o ID do livro que deseja editar!"],
    [" LIBMANAGER v1.0 ", "\tEscolha uma opção:\n", "\t[1] Cadastrar livro", 
     "\t[2] Editar livro", "\t[3] Excluir livro", "\t[4] Visualizar livros",
     "\t[5] Sair do programa\n"],
    [" EXCLUIR ", "Digite o ID do livro que deseja excluir!"],
    [" ERRO ", "ID inexistente!\n", "Acesse a lista de livros", 
     "para consultar o id do livro desejado.\n\n"]
]


list_input_screen = [
    ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN],
    [f"{'Preencha os dados abaixo.':^48}\n", SPACING_MINUS_SIGN],
    [f"{'Obrigado por usar o sistema!':^48}\n\n", SPACING_EQUAL_SIGN],
    [SPACING + "(Pressione [ENTER] para retornar)\n", SPACING_EQUAL_SIGN, 
     " " * 4 + "> _"],
    [SPACING_EQUAL_SIGN, SPACING + "Digite sua opção abaixo: \n", 
     SPACING + "> _"],
]


def default_screen(value_screen, value_input):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(list_screen[value_screen])):
        if i == 0:
            print(SPACING + f"{list_screen[value_screen][i]:=^40}\n\n")
        elif value_screen == 4:
            print(list_screen[value_screen][i])
        elif value_screen == 6:
            print(f"{list_screen[value_screen][i]:^48}")
        else:
            print(f"{list_screen[value_screen][i]:^48}\n\n")
    
    for option in list_input_screen[value_input]:
        print(option, end="")
        

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
        default_screen(Type_screen.INVALID_INPUT.value, Type_input.ENTER.value)
        input()
        return 
    
    if not 0 <= int(choice) < int(max_id):
        default_screen(Type_screen.INVALID_INPUT.value, Type_input.ENTER.value)
        input()
        return

    return choice


def screen_of_empty_list():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40)
    print(f"{'LISTA VAZIA!':^48}\n\n")    
    print(" " * 4 + "Não existe livros cadastrados no momento!\n\n")
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu")
    print(" " * 4 + "=" * 40)
    input()

