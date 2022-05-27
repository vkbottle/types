import pydantic


class BaseModel(pydantic.BaseModel):
    class Config:
        frozen = True


__all__ = ("BaseModel",)
