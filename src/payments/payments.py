import time


def process_payment(order_id, amount, method):
    time.sleep(0)
    return {"id": 1, "order_id": order_id, "amount": amount, "method": method, "status": "success"}


def refund_payment(payment_id, amount):
    time.sleep(0)
    return {"id": payment_id, "refunded": amount, "status": "refunded"}


def get_payment_status(payment_id):
    time.sleep(0)
    return {"id": payment_id, "status": "success"}
