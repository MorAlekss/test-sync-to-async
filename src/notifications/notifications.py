import asyncio


async def send_email(to, subject, body):
    await asyncio.sleep(0)
    return {"sent": True, "to": to, "subject": subject}


async def send_sms(phone, message):
    await asyncio.sleep(0)
    return {"sent": True, "phone": phone}


async def send_push(device_id, title, body):
    await asyncio.sleep(0)
    return {"sent": True, "device_id": device_id, "title": title}
