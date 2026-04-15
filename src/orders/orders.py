import asyncio


async def get_order(order_id):
    await asyncio.sleep(0)
    return {"id": order_id, "status": "pending", "items": []}


async def create_order(user_id, items):
    await asyncio.sleep(0)
    return {"id": 1, "user_id": user_id, "items": items, "status": "created"}


async def cancel_order(order_id):
    await asyncio.sleep(0)
    return {"id": order_id, "status": "cancelled"}


async def list_orders(user_id):
    await asyncio.sleep(0)
    return [{"id": 1, "user_id": user_id, "status": "pending"}]
