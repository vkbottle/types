from typing import Optional, List

from .base_model import BaseObject


class Amount(BaseObject):
    """VK Object orders/Amount

    currency - Currency name
    """

    amounts: Optional[List["AmountItem"]] = None
    currency: Optional[str] = None


class AmountItem(BaseObject):
    """VK Object orders/AmountItem

    amount - Votes amount in user's currency
    description - Amount description
    votes - Votes number
    """

    amount: Optional[int] = None
    description: Optional[str] = None
    votes: Optional[str] = None


class Order(BaseObject):
    """VK Object orders/Order

    amount - Amount
    app_order_id - App order ID
    cancel_transaction_id - Cancel transaction ID
    date - Date of creation in Unixtime
    id - Order ID
    item - Order item
    receiver_id - Receiver ID
    status - Order status
    transaction_id - Transaction ID
    user_id - User ID
    """

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
    """VK Object orders/Subscription

    cancel_reason - Cancel reason
    create_time - Date of creation in Unixtime
    id - Subscription ID
    item_id - Subscription order item
    next_bill_time - Date of next bill in Unixtime
    pending_cancel - Pending cancel state
    period - Subscription period
    period_start_time - Date of last period start in Unixtime
    price - Subscription price
    status - Subscription status
    test_mode - Is test subscription
    trial_expire_time - Date of trial expire in Unixtime
    update_time - Date of last change in Unixtime
    """

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
