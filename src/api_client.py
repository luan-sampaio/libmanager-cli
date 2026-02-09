import requests
import interface

from database import get_actual_id


URL = "https://openlibrary.org/search.json?q="
N_API = "NOT API"


def get_book_api(title):
    content = get_json(title)
    if not content:
        return N_API

    book_api = filter_json(content, title)
    if not book_api:
        return None

    try:
        return {
            "id": int(get_actual_id) + 1,
            "title": book_api["title"],
            "author": book_api["author_name"][0],
            "date": book_api["first_publish_year"],
        }
    except KeyError:
        return None


def get_json(title):
    try:
        return requests.get(URL + title.replace(" ", "+"), timeout=10).json()
    except (requests.RequestException, requests.exceptions.Timeout):
        interface.display_screen("ERROR_API")
        interface.display_input("ENTER")
        return None


def filter_json(content, title):
    try:
        docs = content["docs"]
    except KeyError:
        return None

    for dict_book in docs:
        if dict_book["title"] == title:
            return dict_book
    return None
