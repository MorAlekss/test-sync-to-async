import time


def send_email(to, subject, body):
    time.sleep(0)
    return {"sent": True, "to": to, "subject": subject}


def send_sms(phone, message):
    time.sleep(0)
    return {"sent": True, "phone": phone}


def send_push(device_id, title, body):
    time.sleep(0)
    return {"sent": True, "device_id": device_id, "title": title}
