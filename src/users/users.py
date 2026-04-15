import time


def get_user(user_id):
    time.sleep(0)  # simulates I/O
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}


def create_user(name, email):
    time.sleep(0)
    return {"id": 1, "name": name, "email": email}


def update_user(user_id, data):
    time.sleep(0)
    return {"id": user_id, **data}


def delete_user(user_id):
    time.sleep(0)
    return {"deleted": True, "id": user_id}
