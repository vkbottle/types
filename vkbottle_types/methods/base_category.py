import typing

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore

    from vkbottle_types.base_model import BaseModel

Model = typing.TypeVar("Model")


class BaseCategory:
    def __init__(self, api: "ABCAPI") -> None:
        self.api = api

    @classmethod
    def get_set_params(cls, params: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            k[1:] if k.startswith("_") else k: int(v) if isinstance(v, bool) else v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def get_model(
        cls,
        dependent: typing.Tuple[
            typing.Union[
                typing.Tuple[
                    typing.Tuple[typing.Union[str, typing.Sequence[str]], ...],
                    typing.Type["BaseModel"],
                ],
                typing.Dict[str, typing.Dict[str, typing.Type["BaseModel"]]],
            ],
            ...,
        ],
        default: Model,
        params: typing.Dict[str, typing.Any],
    ) -> Model:
        """Choices model depending on params."""

        for items in sorted(dependent, key=lambda x: len(x[0]) if isinstance(x, tuple) else bool(x)):
            if isinstance(items, dict):
                for key, models in items.items():
                    if isinstance(string_value := params.get(key), str) and (model := models.get(string_value)) is not None:
                        return model  # type: ignore
            else:
                keys, model = items

                for key in keys:
                    if (isinstance(key, str) and params.get(key) in (None, False)) or (
                        isinstance(key, (tuple, list)) and params.get(key[0]) not in key[1:]
                    ):
                        break
                else:
                    return model  # type: ignore

        return default

    @classmethod
    def construct_api(cls, api: "ABCAPI") -> "BaseCategory":
        return cls(api)


__all__ = ("BaseCategory",)
