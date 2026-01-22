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
    VIEW = 11
    EDIT_BOOK = 12
    EDIT_OK = 13
    N_EDIT = 14
    N_DELETE = 15


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
    [" EXCLUIR ", "ATENÇÃO: Esta ação não pode ser defesfeita!"],
    [" CONSULTA ", SPACING + f"{'ID':<4}{'TÍTULO':<19}{'AUTOR':<15}{'ANO'}",
     SPACING_MINUS_SIGN],
    [" EDIÇÃO "],
    ["", f"{'Livro editado com sucesso!':^48}"],
    ["", 
     f"{'Não houve Edição no livro!':^48}"],
    ["", f"{'O Livro NÃO foi excluído!'}"]
]


class Type_input(Enum):
    ENTER = 0
    FILL = 1
    EXIT = 2
    EDIT = 3
    START = 4
    EXCLUDE = 5
    EDIT_BOOK = 6


list_input_screen = [
    ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN],
    [f"{'Preencha os dados abaixo.':^48}\n\n\n", f"{'Pressione [ENTER] para retornar':^48}\n", SPACING_MINUS_SIGN],
    [f"{'Obrigado por usar o sistema!':^48}\n\n", SPACING_EQUAL_SIGN],
    [SPACING + "(Pressione [ENTER] para retornar)\n", SPACING_EQUAL_SIGN, 
      SPACING + "> _"], 
    [SPACING_EQUAL_SIGN, SPACING + "Digite sua opção abaixo: \n", 
     SPACING + "> _"],
    [SPACING_EQUAL_SIGN, SPACING + "> Para confirmar, digite 'DELETAR' ou ", SPACING +
     "pressione [ENTER] para retornar ao ", SPACING + "MENU: _"],
    [f"{'Se não for alterar, pressione [ENTER]':^48}", "\n", SPACING_MINUS_SIGN]
]


def default_screen(value_screen):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(list_screen[value_screen])):
        if i == 0:
            print(SPACING + f"{list_screen[value_screen][i]:=^40}\n\n")
        elif value_screen == 4 or value_screen == 11:
            print(list_screen[value_screen][i])
        elif value_screen == 6:
            print(f"{list_screen[value_screen][i]:^48}")
        else:
            print(f"{list_screen[value_screen][i]:^48}\n\n")


def default_screen_input(value_input):
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
        default_screen(Type_screen.INVALID.value)
        default_screen_input(Type_input.ENTER.value)
        input()
        return None
    
    if not 0 <= int(choice) < int(max_id):
        default_screen(Type_screen.INVALID.value)
        default_screen_input(Type_input.ENTER.value)
        input()
        return None

    return int(choice)


def get_book():
    title = input(" " * 4 + "Insira o título do livro: ",)
    if not title:
        return

    author = input(" " * 4 + "Insira o nome do autor: ")  
    date = input(" " * 4 + "Insira o ano de lançamento do livro: ")
    
    return {"title": title, "author": author, "date": date}


def show_list_books(list_books):
    count = 0
    for book in list_books:
        print(SPACING +  f"{count:<4}{book.get('title'):<19}{book.get('author'):<15}{book.get('date')}")
        count += 1
    print("\n")


def checks_delete():
    checks = input()
    if checks == "DELETAR":
        return True
    else:
        return False


def show_book(id, books):
    print(SPACING + "Título: " + f"{books[id].get('title')}")
    print(SPACING + "Autor: " + f"{books[id].get('author')}")
    print(SPACING + "Data: " + f"{books[id].get('date')}\n\n")


def get_field_book():
    title = input(SPACING + "Digite o título: ")
    author = input(SPACING + "Digite o autor: ")
    date = input(SPACING + "Digite o ano: ")
    return {"title": title, "author": author, "date": date}
