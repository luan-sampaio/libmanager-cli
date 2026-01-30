import requests
import utils

URL = "https://openlibrary.org/search.json?q="

def get_book_api(title):
    response = requests.get(URL + title.replace(' ', '+'))
    content = response.json()
    
    book_api = {}
    docs = content["docs"]
    
    for dict_book in docs:
        if dict_book["title"] == title:
            book_api = dict_book
            break
    
    book_id = utils.increase_id()
    
    book = {
        "title": book_api["title"],
        "author": book_api["author_name"][0],
        "date": book_api["first_publish_year"],
        "id": book_id
    }
        
    return book
    
