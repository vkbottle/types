import warnings


class BaseStateGroup:
    warnings.warn(
        "BaseStateGroup from vkbottle_types is deprecated "
        "and will be removed in future releases, "
        "use vkbottle.BaseStateGroup instead",
        DeprecationWarning,
    )

    def __init__(self, *args, **kwargs):
        pass


class StatePeer:
    warnings.warn(
        "StatePeer from vkbottle_types is deprecated "
        "and will be removed in future releases, "
        "use vkbottle.StatePeer instead",
        DeprecationWarning,
    )

    def __init__(self, *args, **kwargs):
        pass
