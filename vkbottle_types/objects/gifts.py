import enum
from typing import Optional

from .base_model import BaseObject


class Gift(BaseObject):
    """VK Object gifts/Gift"""

    date: Optional[int] = None
    from_id: Optional[int] = None
    gift: Optional["Layout"] = None
    gift_hash: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    privacy: Optional["GiftPrivacy"] = None


class GiftPrivacy(enum.IntEnum):
    """ Gift privacy """

    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2


class Layout(BaseObject):
    """VK Object gifts/Layout

    id - Gift ID
    thumb_512 - URL of the preview image with 512 px in width
    thumb_256 - URL of the preview image with 256 px in width
    thumb_48 - URL of the preview image with 48 px in width
    thumb_96 - URL of the preview image with 96 px in width
    stickers_product_id - ID of the sticker pack, if the gift is representing one
    build_id - ID of the build of constructor gift
    keywords - Keywords used for search
    """

    id: Optional[int] = None
    thumb_512: Optional[str] = None
    thumb_256: Optional[str] = None
    thumb_48: Optional[str] = None
    thumb_96: Optional[str] = None
    stickers_product_id: Optional[int] = None
    build_id: Optional[str] = None
    keywords: Optional[str] = None
