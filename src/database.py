import csv
import sys

from tabulate import tabulate

id_book = -1

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
        print(tabulate(reader, headers="keys", tablefmt="github"), "\n\n")            


def show_list_of_books():
    list_of_books = []
    with open("data/books.csv", encoding="utf-8") as read:
        reader = csv.DictReader(read)
        for row in reader:
            list_of_books.append(row)
            
    return list_of_books
    

def get_field_names():
    fieldnames = []
    with open("data/books.csv", encoding="utf-8") as read:
        reader = csv.DictReader(read)
        fieldnames = reader.fieldnames

    return fieldnames


def remove_book(id_book):
    count_id = 0
    list_of_books = show_list_of_books()
    removed_book_list = []
    excluded_book = {}
    
    for row in list_of_books:
        if int(row.get("id")) == id_book:
            excluded_book = row
        else:
            row["id"] = count_id
            removed_book_list.append(row)
            count_id += 1
            
    
    fieldnames = get_field_names()
    with open("data/books.csv", "w") as write:
        writer = csv.DictWriter(write, fieldnames)
        writer.writeheader()
        
        for row in removed_book_list:
            writer.writerow(row)
        
    return excluded_book


def edit_book(book, id_book):
    list_of_books = show_list_of_books()
    
    with open("data/books.csv", "r") as read:
        reader = csv.DictReader(read)
        for row in reader:
            if int(row.get("id")) == id_book:
                if book.get("title"):
                    list_of_books[id_book]["title"] = book.get("title")

                if book.get("author"):
                    list_of_books[id_book]["author"] = book.get("author")

                if book.get("date"):
                    list_of_books[id_book]["date"] = book.get("date")
        
    fieldnames = get_field_names()
    with open("data/books.csv", "w") as write:
        writer = csv.DictWriter(write, fieldnames)
        writer.writeheader()
        
        for book in list_of_books:
            writer.writerow(book)


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


def get_id():
    return id_book
