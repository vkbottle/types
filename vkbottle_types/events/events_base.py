from typing import TYPE_CHECKING, Any, Callable, Dict, Type, Union

from .enums import GroupEventType, UserEventType

if TYPE_CHECKING:
    from . import GroupTypes, UserTypes
    from .bot_events import BaseGroupEvent
    from .user_events import BaseUserEvent


class EventsBase:
    events_registered: Dict[
        Union[GroupEventType, UserEventType],
        Type[Union["GroupTypes.UnifiedTypes", "UserTypes.UnifiedTypes"]],
    ] = {}

    def __init__(
        self,
        type_enum: Type[Union[GroupEventType, UserEventType]],
        on_undefined: Callable[[str], Any] = lambda et: EventsBase.__raise(
            NotImplementedError(et)
        ),
    ):
        self.type_enum = type_enum
        self.on_undefined = on_undefined

    def register(
        self,
        event_type: Union[GroupEventType, UserEventType],
        event_model: Union["BaseGroupEvent", "BaseUserEvent"],
    ):
        self.events_registered[event_type] = event_model

    def get(
        self, event_type: Union[int, str, GroupEventType, UserEventType]
    ) -> Callable[..., Union["GroupTypes.UnifiedTypes", "UserTypes.UnifiedTypes"]]:
        if not str(event_type).startswith(self.type_enum.__name__):
            event_type = self.type_enum(event_type)

        model = self.events_registered.get(event_type)
        if model is None:
            return self.on_undefined(event_type)
        return model

    @staticmethod
    def __raise(ex):
        raise ex
