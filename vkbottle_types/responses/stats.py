from vkbottle_types.codegen.responses.stats import *  # noqa: F403,F401

from .base_response import BaseResponse

localns = locals().copy()
for item in localns.values():
    if not (isinstance(item, type) and issubclass(item, BaseResponse)):
        continue
    
    for base in item.__bases__:
        if base is not BaseResponse and issubclass(base, BaseResponse):
            item.model_rebuild(force=True)

    item.model_rebuild(force=True, _types_namespace=localns)

