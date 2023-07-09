try:
    from pydantic.v1 import BaseModel
except ImportError:
    from pydantic import BaseModel  # type: ignore[assignment]


class BaseEventObject(BaseModel):
    pass
