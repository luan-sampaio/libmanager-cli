import os
import interface


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


def view_books(list_of_books):
    if not list_of_books:
        interface.screen_of_empty_list()
        return 

    os.system('cls' if os.name == 'nt' else 'clear')

    count = 0
    print(" " * 4 + f"{' CONSULTA ':=^40}")
    print("\n\n")
    print(" " * 4 + f"{'ID':<4}{'TÍTULO':<19}{'AUTOR':<15}{'ANO'}")
    print(" " * 4 + "-" * 40)
    
    for book in list_of_books:
        print(" " * 4 +  f"{count:<4}{book.get('title'):<19}{book.get('author'):<15}{book.get('date')}")
        count += 1
    
    print("\n\n")
    print(" " * 4 + "Pressione [ENTER] para retornar ao menu.")
    print(" " * 4 + "=" * 40)
    input()
    

def delete_book(max_id, list_of_books):
    if not len(list_of_books):
        interface.screen_of_empty_list()
        return 
    
    interface.delete_book_screen()    
    choice = interface.get_id(max_id)
    if not choice:
        return 
    
    if interface.confirm_deletion(int(choice), list_of_books):
        list_of_books.pop(int(choice))
        interface.display_sucess_delete()
        input()
    return 


def edit_book(list_of_books, max_id):
    if not len(list_of_books):
        interface.screen_of_empty_list()
        return 

    interface.screen_edit_book()
    choice = interface.get_id(max_id)
    if not choice:
        return 

    choice = int(choice)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + f"{' EDIÇÃO ':=^40}\n\n")
    print(" " * 4 + "Título: " + f"{list_of_books[choice].get('title')}")
    print(" " * 4 + "Autor: " + f"{list_of_books[choice].get('author')}")
    print(" " * 4 + "Data: " + f"{list_of_books[choice].get('date')}\n\n")
    print(f"{'Se não for alterar, pressione [ENTER]':^48}")
    print(" " * 4 + "-" * 40)

    
    title = input(" " * 4 + "Digite o título: ")
    if title:
        list_of_books[choice]["title"] = title

    author = input(" " * 4 + "Digite o autor: ")
    if author:
        list_of_books[choice]["author"] = author
        
    date = input(" " * 4 + "Digite o ano: ")
    if date:
        list_of_books[choice]["date"] = date

    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " * 4 + "=" * 40 + "\n\n")
    print(f"{'Livro editado com sucesso!':^48}\n\n")    
    print(" " * 4 + 'Pressione [ENTER] para retornar ao menu')
    print(" " * 4 + "=" * 40)
    input()
