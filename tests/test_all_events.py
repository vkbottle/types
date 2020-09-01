from vkbottle_types.events import DEFAULT_EVENTS_BASE_GROUP, GroupEventType


def test_all_events():
    DEFAULT_EVENTS_BASE_GROUP.on_undefined = lambda et: exec(
        f"raise AssertionError({et})"
    )
    for event_type in GroupEventType:
        DEFAULT_EVENTS_BASE_GROUP.get(event_type)


if __name__ == "__main__":
    test_all_events()
