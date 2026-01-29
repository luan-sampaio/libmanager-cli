id_book = -1


def increase_id():
    global id_book
    id_book += 1
    return id_book


def get_actual_id():
    return id_book
