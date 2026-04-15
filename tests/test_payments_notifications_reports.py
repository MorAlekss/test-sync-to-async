import pytest
from src.payments.payments import process_payment, refund_payment, get_payment_status
from src.notifications.notifications import send_email, send_sms, send_push
from src.reports.reports import generate_report, export_report, get_report_status


@pytest.mark.asyncio
async def test_process_payment():
    result = await process_payment(1, 100.0, "card")
    assert result["order_id"] == 1
    assert result["amount"] == 100.0
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_refund_payment():
    result = await refund_payment(1, 50.0)
    assert result["refunded"] == 50.0
    assert result["status"] == "refunded"


@pytest.mark.asyncio
async def test_get_payment_status():
    result = await get_payment_status(1)
    assert result["id"] == 1
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_send_email():
    result = await send_email("test@example.com", "Hello", "Body")
    assert result["sent"] == True
    assert result["to"] == "test@example.com"


@pytest.mark.asyncio
async def test_send_sms():
    result = await send_sms("+123****7890", "Hello")
    assert result["sent"] == True
    assert result["phone"] == "+123****7890"


@pytest.mark.asyncio
async def test_send_push():
    result = await send_push("device123", "Title", "Body")
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
