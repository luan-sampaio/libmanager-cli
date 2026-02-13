import os

from database import show_list_of_books
import database

SPACING = " " * 4
SPACING_EQUAL_SIGN = "=" * 50 + "\n"
SPACING_MINUS_SIGN = "-" * 50 + "\n"
DISPLAY_HEADER = 0


screen = {
    "INVALID": [" ERRO ", "Opção inválida!"],
    "INSERT": [" CADASTRO "],
    "EXIT": [""],
    "EDIT": [" EDIÇÃO ", "Digite o ID do livro que deseja editar!"],
    "START": [
        " LIBMANAGER v1.0 ",
        "Escolha uma opção:\n",
        "[1] Cadastrar livro  ",
        "[2] Editar livro     ",
        "[3] Excluir livro    ",
        "[4] Visualizar livros",
        "[5] Sair do programa\n",
    ],
    "DELETE": [" EXCLUIR ", "Digite o ID do livro que deseja excluir!"],
    "EMPTY": [" LISTA VAZIA ", "Não existe livros cadastrados no momento!"],
    "REGISTER": [" CADASTRO ", "Livro Cadastrado com sucesso!\n\n"],
    "CONFIRM_DELETE": [" EXCLUIR ", "ATENÇÃO: Esta ação não pode ser defesfeita!"],
    "VIEW": [" CONSULTA "],
    "EDIT_BOOK": [" EDIÇÃO "],
    "EDIT_OK": ["", "Livro editado com sucesso!"],
    "N_EDIT": ["", "Não houve Edição no livro!'"],
    "N_DELETE": ["", "O Livro NÃO foi excluído!"],
    "DELETE_BOOK": [" EXCLUIR ", "O Livro abaixo foi excluído com sucesso!"],
    "ERROR_API": [" ERROR ", "Houve algum problema na API, tente novamente!"],
    "ERROR_BOOK": [" ERROR ", "Título Inválido! Digite um título válido."],
}


def display_screen(type_screen):
    list_screen = screen[type_screen]
    os.system("cls" if os.name == "nt" else "clear")

    for i, type_list in enumerate(list_screen):
        if i == DISPLAY_HEADER:
            print(f"{type_list:=^50}\n\n")
        elif type_screen in ["START", "VIEW", "REGISTER"]:
            print(f"{type_list:^50}")
        else:
            print(f"{type_list:^50}\n\n")


screen_input = {
    "ENTER": ["\tPressione [ENTER] para retornar\n", SPACING_EQUAL_SIGN],
    "FILL": [
        f"{'Preencha os dados abaixo.':^50}\n\n\n",
        f"{'Pressione [ENTER] para retornar':^50}\n",
        SPACING_MINUS_SIGN,
    ],
    "EXIT": [f"{'Obrigado por usar o sistema!':^50}\n\n\n", SPACING_EQUAL_SIGN],
    "EDIT": [
        "\tPressione [ENTER] para retornar\n",
        SPACING_EQUAL_SIGN,
        SPACING + "> _",
    ],
    "START": [
        "Digite sua opção abaixo: \n",
    ],
    "EXCLUDE": [
        SPACING_EQUAL_SIGN,
        SPACING + "> Para confirmar, digite 'DELETAR' ou ",
        SPACING + "pressione [ENTER] para retornar ao ",
        SPACING + "MENU: _",
    ],
    "EDIT_BOOK": [
        f"{'Se não for alterar, pressione [ENTER]':^50}",
        "\n",
        SPACING_MINUS_SIGN,
    ],
}


def display_input(type_input):
    list_screen_input = screen_input[type_input]
    for element in list_screen_input:
        if type_input == "EXCLUDE":
            if element == SPACING + "MENU: _":
                print(element, end="")
            else:
                print(element)
        elif type_input == "ADD_BOOK":
            print(f"{element:^50}")
        elif type_input == "START":
            print(SPACING_EQUAL_SIGN)
            print(f"{element:^50}", end="")
            print("> _", end="")
        else:
            print(element, end="")

    if type_input == "ENTER":
        input()
    else:
        return


def get_id():
    choice = input()

    if not choice.isdigit():
        display_screen("INVALID")
        display_input("ENTER")
        return None

    choice = int(choice)
    if not 0 <= choice <= database.get_actual_id():
        display_screen("INVALID")
        display_input("ENTER")
        return None

    return choice


def get_title():
    print(f"{'          Insira o título do livro: ':^30}", end="")
    title = input()
    if not title:
        return None

    return title


def checks_delete():
    checks = input()
    return checks == "DELETAR"


def show_book_by_list(id_book):
    books = show_list_of_books()
    print(SPACING + "Título: " + f"{books[id_book].get('title')}")
    print(SPACING + "Autor: " + f"{books[id_book].get('author')}")
    print(SPACING + "Ano: " + f"{books[id_book].get('date')}\n\n")


def get_field_book():
    book = {"title": None, "author": None, "date": None}

    title = input("\n" + SPACING + "Digite o título: ")
    if title:
        book["title"] = title

    author = input(SPACING + "Digite o autor: ")
    if author:
        book["author"] = author

    date = input(SPACING + "Digite o ano: ")
    if date:
        book["date"] = date
    return book


def show_book(book):
    print(SPACING + "Título: " + f"{book.get('title')}")
    print(SPACING + "Autor: " + f"{book.get('author')}")
    print(SPACING + "Ano: " + f"{book.get('date')}\n\n")


def display_fill_info():
    print("\n" + SPACING + "Preencha as informações por favor!")
