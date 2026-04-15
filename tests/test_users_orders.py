import pytest
from src.users.users import get_user, create_user, update_user, delete_user
from src.orders.orders import get_order, create_order, cancel_order, list_orders


def test_get_user():
    result = get_user(1)
    assert result["id"] == 1
    assert "name" in result
    assert "email" in result


def test_create_user():
    result = create_user("Jane Doe", "jane@example.com")
    assert result["name"] == "Jane Doe"
    assert result["email"] == "jane@example.com"


def test_update_user():
    result = update_user(1, {"name": "Updated Name"})
    assert result["id"] == 1
    assert result["name"] == "Updated Name"


def test_delete_user():
    result = delete_user(1)
    assert result["deleted"] == True
    assert result["id"] == 1


def test_get_order():
    result = get_order(1)
    assert result["id"] == 1
    assert result["status"] == "pending"


def test_create_order():
    result = create_order(1, ["item1", "item2"])
    assert result["user_id"] == 1
    assert result["items"] == ["item1", "item2"]
    assert result["status"] == "created"


def test_cancel_order():
    result = cancel_order(1)
    assert result["id"] == 1
    assert result["status"] == "cancelled"


def test_list_orders():
    result = list_orders(1)
    assert isinstance(result, list)
    assert len(result) > 0
