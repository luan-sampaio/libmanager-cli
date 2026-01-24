import os
import utils
from enum import Enum


SPACING = " " * 4
SPACING_EQUAL_SIGN = " " * 4 + "=" * 40 + "\n"
SPACING_MINUS_SIGN = " " * 4 + "-" * 40 + "\n"
DISPLAY_HEADER = 0

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

def display_screen(type):
    list_screen = screen[type]
    
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(len(list_screen)):
        if i == DISPLAY_HEADER:
            print(SPACING + f"{list_screen[i]:=^40}\n\n")
        elif type == "START":
            print(list_screen[i])
        else:
            print(f"{list_screen[i]:^48}\n\n")


screen = {
    "INVALID": [" ERRO ", "Opção inválida!"],
    "INSERT": [" CADASTRO "],
    "EXIT": [""], 
    "EDIT": [" EDIÇÃO ", "Digite o ID do livro que deseja editar!"],
    "START": [" LIBMANAGER v1.0 ", "\tEscolha uma opção:\n", "\t[1] Cadastrar livro", 
     "\t[2] Editar livro", "\t[3] Excluir livro", "\t[4] Visualizar livros",
     "\t[5] Sair do programa\n"],

}


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
    DELETE_BOOK = 16


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
    ["", f"{'O Livro NÃO foi excluído!'}"], 
    [" EXCLUIR ", f"{'O Livro abaixo foi excluído com sucesso!':^48}"]
]

screen_input = {
    "ENTER": ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN],
    "FILL": [f"{'Preencha os dados abaixo.':^48}\n\n\n",
    f"{'Pressione [ENTER] para retornar':^48}\n", SPACING_MINUS_SIGN],
    "EXIT": [f"{'Obrigado por usar o sistema!':^48}\n\n\n", SPACING_EQUAL_SIGN],
    "EDIT": ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN, 
    SPACING + "> _"], 
    "START": [SPACING_EQUAL_SIGN, SPACING + "Digite sua opção abaixo: \n", 
    SPACING + "> _"],
    "EXCLUDE": [SPACING_EQUAL_SIGN, SPACING + "> Para confirmar, digite 'DELETAR' ou ",
    SPACING + "pressione [ENTER] para retornar ao ", SPACING + "MENU: _"],
    "EDIT_BOOK": [f"{'Se não for alterar, pressione [ENTER]':^48}", "\n", SPACING_MINUS_SIGN]
}


def display_input(type):
    list_screen_input = screen_input[type]
    for element in list_screen_input:
        if type == "EXCLUDE":
            if element == SPACING + "MENU: _":
                print(element, end="")
            else:
                print(element)
        else:
            print(element, end="")

    if type == "ENTER":
        input()
    else:
        return


def get_id():
    choice = input()
    
    if not choice.isdigit():
        default_screen(Type_screen.INVALID.value)
        display_input("ENTER")
        return None
    
    choice = int(choice)

    if not 0 <= choice <= utils.get_actual_id():
        default_screen(Type_screen.INVALID.value)
        display_input("ENTER")        
        return None

    return choice


def get_book():
    title = input(SPACING + "Insira o título do livro: ",)
    if not title:
        return

    while True:
        author = input(SPACING + "Insira o nome do autor: ") 
        if not author:
            display_fill_info()
        else:
            break
    
    while True:
        date = input(SPACING + "Insira o ano de lançamento do livro: ")
        if not date:
            display_fill_info()
        else:
            break

    id = utils.increase_id()
    return {"title": title, "author": author, "date": date, "id": id}


def show_list_books(list_books):
    for book in list_books:
        print(SPACING +  f"{book.get('id'):<4}{book.get('title'):<19}{book.get('author'):<15}{book.get('date')}")
    print("\n")


def checks_delete():
    checks = input()
    if checks == "DELETAR":
        return True
    else:
        return False


def show_book_by_list(id, books):
    print(SPACING + "Título: " + f"{books[id].get('title')}")
    print(SPACING + "Autor: " + f"{books[id].get('author')}")
    print(SPACING + "Ano: " + f"{books[id].get('date')}\n\n")


def get_field_book():
    title = input(SPACING + "Digite o título: ")
    author = input(SPACING + "Digite o autor: ")
    date = input(SPACING + "Digite o ano: ")
    return {"title": title, "author": author, "date": date}


def show_book(book):
    print(SPACING + "Título: " + f"{book.get('title')}")
    print(SPACING + "Autor: " + f"{book.get('author')}")
    print(SPACING + "Ano: " + f"{book.get('date')}\n\n")


def display_fill_info():
    print("\n" + SPACING + "Preencha as informações por favor!")
