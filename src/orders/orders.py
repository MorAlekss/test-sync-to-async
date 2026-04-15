import time


def get_order(order_id):
    time.sleep(0)
    return {"id": order_id, "status": "pending", "items": []}


def create_order(user_id, items):
    time.sleep(0)
    return {"id": 1, "user_id": user_id, "items": items, "status": "created"}


def cancel_order(order_id):
    time.sleep(0)
    return {"id": order_id, "status": "cancelled"}


def list_orders(user_id):
    time.sleep(0)
    return [{"id": 1, "user_id": user_id, "status": "pending"}]
