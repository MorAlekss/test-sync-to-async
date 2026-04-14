import asyncio


async def get_user(user_id):
    await asyncio.sleep(0)  # simulates I/O
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}


async def create_user(name, email):
    await asyncio.sleep(0)
    return {"id": 1, "name": name, "email": email}


async def update_user(user_id, data):
    await asyncio.sleep(0)
    return {"id": user_id, **data}


async def delete_user(user_id):
    await asyncio.sleep(0)
    return {"deleted": True, "id": user_id}
