import inspect

from vkbottle_types.codegen.responses.docs import *  # noqa: F403,F401

from .base_response import BaseResponse

_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if not (inspect.isclass(item) and issubclass(item, BaseResponse)):
        continue
    item.update_forward_refs(**_locals)
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.update_forward_refs(**_locals)  # type: ignore
