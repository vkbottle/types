import typing

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore

Model = typing.TypeVar("Model")


class BaseCategory:
    def __init__(self, api: "ABCAPI"):
        self.api = api

    @classmethod
    def get_set_params(cls, params: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            k[1:] if k.startswith("_") else k:
            int(v) if isinstance(v, bool) else v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def get_model(
        cls,
        dependent: typing.Tuple[typing.Tuple[typing.Tuple[typing.Union[str, typing.List[str]], ...], Model], ...],
        default: Model,
        params: typing.Dict[str, typing.Any],
    ) -> Model:
        """Choices model depending on params."""

        for items in sorted(dependent, key=lambda x: len(x[0])):
            keys, model = items
            
            for key in keys:
                if (
                    isinstance(key, str) and params.get(key) is None
                ) or (
                    isinstance(key, list) and params.get(key[0]) not in key[1:]
                ):
                    break
            else:
                return model

        return default

    @classmethod
    def construct_api(cls, api: "ABCAPI") -> typing.Type["BaseCategory"]:
        cls.api = api
        return cls


__all__ = ("BaseCategory",)
