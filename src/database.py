import csv
import sys

from tabulate import tabulate


def save_book_csv(book):
    with open("data/books.csv", "a", encoding="utf-8") as analysis, open(
        "data/books.csv", encoding="utf-8"
    ) as read:
        reader = csv.DictReader(read)
        writer = csv.DictWriter(analysis, reader.fieldnames)
        writer.writerow(book)


def show_table_of_books():
    with open("data/books.csv", encoding="utf-8") as read:
        reader = csv.DictReader(read)
        print(tabulate(reader, headers="keys", tablefmt="grid"))            


def show_list_of_books():
    list_of_books = []
    with open("data/books.csv", encoding="utf-8") as read:
        reader = csv.DictReader(read)
        for row in reader:
            list_of_books.append(row)
            
        return list_of_books
    

def remove_book(id_book):
    return list_of_books.pop(int(id_book))


def edit_book(book, id_book):
    if book.get("title"):
        list_of_books[id_book]["title"] = book.get("title")

    if book.get("author"):
        list_of_books[id_book]["author"] = book.get("author")

    if book.get("date"):
        list_of_books[id_book]["date"] = book.get("date")


def get_actual_id():
    id_book_local = -1
    books = []
    
    try:
        with open("data/books.csv", encoding="utf-8") as read:
            reader = csv.DictReader(read)
            for line in reader:
                books.append(line)
    except FileNotFoundError:
        sys.exit("Use python src/main.py")

    if books:
        return int(books[len(books) - 1]["id"])
    return id_book_local


def increase_id():
    global id_book
    id_book += 1
    return id_book


id_book = get_actual_id()
