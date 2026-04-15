import pytest
from src.payments.payments import process_payment, refund_payment, get_payment_status
from src.notifications.notifications import send_email, send_sms, send_push
from src.reports.reports import generate_report, export_report, get_report_status


def test_process_payment():
    result = process_payment(1, 100.0, "card")
    assert result["order_id"] == 1
    assert result["amount"] == 100.0
    assert result["status"] == "success"


def test_refund_payment():
    result = refund_payment(1, 50.0)
    assert result["refunded"] == 50.0
    assert result["status"] == "refunded"


def test_get_payment_status():
    result = get_payment_status(1)
    assert result["id"] == 1
    assert result["status"] == "success"


def test_send_email():
    result = send_email("test@example.com", "Hello", "Body")
    assert result["sent"] == True
    assert result["to"] == "test@example.com"


def test_send_sms():
    result = send_sms("+1234567890", "Hello")
    assert result["sent"] == True
    assert result["phone"] == "+1234567890"


def test_send_push():
    result = send_push("device123", "Title", "Body")
    assert result["sent"] == True
    assert result["device_id"] == "device123"


@pytest.mark.asyncio
async def test_generate_report():
    result = await generate_report("sales", {"period": "monthly"})
    assert result["type"] == "sales"
    assert "data" in result


@pytest.mark.asyncio
async def test_export_report():
    result = await export_report(1, "pdf")
    assert result["report_id"] == 1
    assert result["format"] == "pdf"
    assert "url" in result


@pytest.mark.asyncio
async def test_get_report_status():
    result = await get_report_status(1)
    assert result["report_id"] == 1
    assert result["status"] == "completed"
