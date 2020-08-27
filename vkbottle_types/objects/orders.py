from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Amount(BaseObject):
    """VK Object orders/Amount"""

    amounts: Optional[List["AmountItem"]]
    currency: Optional[str] = None


class AmountItem(BaseObject):
    """VK Object orders/AmountItem"""

    amount: Optional[int] = None
    description: Optional[str] = None
    votes: Optional[str] = None


class Order(BaseObject):
    """VK Object orders/Order"""

    amount: Optional[int] = None
    app_order_id: Optional[int] = None
    cancel_transaction_id: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    item: Optional[str] = None
    receiver_id: Optional[int] = None
    status: Optional[str] = None
    transaction_id: Optional[int] = None
    user_id: Optional[int] = None


class Subscription(BaseObject):
    """VK Object orders/Subscription"""

    cancel_reason: Optional[str] = None
    create_time: Optional[int] = None
    id: Optional[int] = None
    item_id: Optional[str] = None
    next_bill_time: Optional[int] = None
    pending_cancel: Optional[bool] = None
    period: Optional[int] = None
    period_start_time: Optional[int] = None
    price: Optional[int] = None
    status: Optional[str] = None
    test_mode: Optional[bool] = None
    trial_expire_time: Optional[int] = None
    update_time: Optional[int] = None
