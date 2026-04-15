import asyncio


async def process_payment(order_id, amount, method):
    await asyncio.sleep(0)
    return {"id": 1, "order_id": order_id, "amount": amount, "method": method, "status": "success"}


async def refund_payment(payment_id, amount):
    await asyncio.sleep(0)
    return {"id": payment_id, "refunded": amount, "status": "refunded"}


async def get_payment_status(payment_id):
    await asyncio.sleep(0)
    return {"id": payment_id, "status": "success"}
