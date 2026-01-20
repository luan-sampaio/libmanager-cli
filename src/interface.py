import os
from database import show_list_of_books
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
    EMPTY = 7
    DELETE_SUCESS = 8
    REGISTER = 9
    CONFIRM_DELETE = 10


class Type_input(Enum):
    ENTER = 0
    FILL = 1
    EXIT = 2
    EDIT = 3
    START = 4
    EXCLUDE = 5


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
     "para consultar o id do livro desejado.\n\n"],
    [" LISTA VAZIA ", "Não existe livros cadastrados no momento!"],
    ["", "Livro deletado com sucesso!"],
    [" CADASTRO ", "Livro Cadastrado com sucesso!"],
    [" EXCLUIR ", "ATENÇÃO: Esta ação não pode ser defesfeita!"]
]


list_input_screen = [
    ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN],
    [f"{'Preencha os dados abaixo.':^48}\n", SPACING_MINUS_SIGN],
    [f"{'Obrigado por usar o sistema!':^48}\n\n", SPACING_EQUAL_SIGN],
    [SPACING + "(Pressione [ENTER] para retornar)\n", SPACING_EQUAL_SIGN, 
      SPACING + "> _"], 
    [SPACING_EQUAL_SIGN, SPACING + "Digite sua opção abaixo: \n", 
     SPACING + "> _"],
    [SPACING_EQUAL_SIGN, SPACING + "> Para confirmar, digite 'DELETAR' ou ", SPACING +
     "pressione [ENTER] para retornar ao ", SPACING + "MENU: _"]
]

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

def show_book_to_delete(id):
    list_books = show_list_of_books()
    print(" " * 4 + "Título: " + list_books[id].get('title'))
    print(" " * 4 + "Autor: " + list_books[id].get('author') + '\n')


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
        if value_input == Type_input.EXCLUDE.value:
            if option == SPACING + "MENU: _":
                print(option, end="")
            else:
                print(option)
        else:
            print(option, end="")
        

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
