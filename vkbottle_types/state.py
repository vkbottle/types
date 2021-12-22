class BaseStateGroup:
    def __init__(self, *args, **kwargs):
        raise DeprecationWarning(
            "BaseStateGroup from vkbottle_types is deprecated "
            "and will be removed in future releases, "
            "use vkbottle.BaseStateGroup instead",
        )


class StatePeer:
    def __init__(self, *args, **kwargs):
        raise DeprecationWarning(
            "StatePeer from vkbottle_types is deprecated "
            "and will be removed in future releases, "
            "use vkbottle.StatePeer instead"
        )
