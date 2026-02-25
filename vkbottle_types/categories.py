import importlib
import dataclasses
import typing
from abc import ABC, abstractmethod

from .responses.execute import ExecuteResponse, Response

if typing.TYPE_CHECKING:
    from .methods.base_category import BaseCategory
    from .methods import (
        account,
        ads,
        app_widgets,
        apps,
        auth,
        board,
        bugtracker,
        database,
        docs,
        donut,
        downloaded_games,
        fave,
        friends,
        gifts,
        groups,
        lead_forms,
        likes,
        market,
        messages,
        newsfeed,
        notes,
        notifications,
        orders,
        pages,
        photos,
        podcasts,
        polls,
        pretty_cards,
        search,
        secure,
        stats,
        status,
        storage,
        store,
        stories,
        streaming,
        translations,
        users,
        utils,
        video,
        wall,
        widgets,
    )

    from vkbottle import ABCAPI  # type: ignore


@dataclasses.dataclass(frozen=True)
class ExecutableCode(typing.Generic[Response]):
    code: str


CATEGORIES = {
    "account": "AccountCategory",
    "ads": "AdsCategory",
    "app_widgets": "AppWidgetsCategory",
    "apps": "AppsCategory",
    "auth": "AuthCategory",
    "board": "BoardCategory",
    "bugtracker": "BugtrackerCategory",
    "database": "DatabaseCategory",
    "docs": "DocsCategory",
    "donut": "DonutCategory",
    "downloaded_games": "DownloadedGamesCategory",
    "fave": "FaveCategory",
    "friends": "FriendsCategory",
    "gifts": "GiftsCategory",
    "groups": "GroupsCategory",
    "lead_forms": "LeadFormsCategory",
    "likes": "LikesCategory",
    "market": "MarketCategory",
    "messages": "MessagesCategory",
    "newsfeed": "NewsfeedCategory",
    "notes": "NotesCategory",
    "notifications": "NotificationsCategory",
    "orders": "OrdersCategory",
    "pages": "PagesCategory",
    "photos": "PhotosCategory",
    "podcasts": "PodcastsCategory",
    "polls": "PollsCategory",
    "pretty_cards": "PrettyCardsCategory",
    "search": "SearchCategory",
    "secure": "SecureCategory",
    "stats": "StatsCategory",
    "status": "StatusCategory",
    "storage": "StorageCategory",
    "store": "StoreCategory",
    "stories": "StoriesCategory",
    "streaming": "StreamingCategory",
    "translations": "TranslationsCategory",
    "users": "UsersCategory",
    "utils": "UtilsCategory",
    "video": "VideoCategory",
    "wall": "WallCategory",
    "widgets": "WidgetsCategory",
}


class APICategories(ABC):

    if typing.TYPE_CHECKING:
        @typing.overload
        @property
        def account(self) -> "account.AccountCategory": ...

        @typing.overload
        @property
        def ads(self) -> "ads.AdsCategory": ...

        @typing.overload
        @property
        def app_widgets(self) -> "app_widgets.AppWidgetsCategory": ...

        @typing.overload
        @property
        def apps(self) -> "apps.AppsCategory": ...

        @typing.overload
        @property
        def auth(self) -> "auth.AuthCategory": ...

        @typing.overload
        @property
        def board(self) -> "board.BoardCategory": ...

        @typing.overload
        @property
        def bugtracker(self) -> "bugtracker.BugtrackerCategory": ...

        @typing.overload
        @property
        def database(self) -> "database.DatabaseCategory": ...

        @typing.overload
        @property
        def docs(self) -> "docs.DocsCategory": ...

        @typing.overload
        @property
        def donut(self) -> "donut.DonutCategory": ...

        @typing.overload
        @property
        def downloaded_games(self) -> "downloaded_games.DownloadedGamesCategory": ...

        @typing.overload
        @property
        def fave(self) -> "fave.FaveCategory": ...

        @typing.overload
        @property
        def friends(self) -> "friends.FriendsCategory": ...

        @typing.overload
        @property
        def gifts(self) -> "gifts.GiftsCategory": ...

        @typing.overload
        @property
        def groups(self) -> "groups.GroupsCategory": ...

        @typing.overload
        @property
        def lead_forms(self) -> "lead_forms.LeadFormsCategory": ...

        @typing.overload
        @property
        def likes(self) -> "likes.LikesCategory": ...

        @typing.overload
        @property
        def market(self) -> "market.MarketCategory": ...

        @typing.overload
        @property
        def messages(self) -> "messages.MessagesCategory": ...

        @typing.overload
        @property
        def newsfeed(self) -> "newsfeed.NewsfeedCategory": ...

        @typing.overload
        @property
        def notes(self) -> "notes.NotesCategory": ...

        @typing.overload
        @property
        def notifications(self) -> "notifications.NotificationsCategory": ...

        @typing.overload
        @property
        def orders(self) -> "orders.OrdersCategory": ...

        @typing.overload
        @property
        def pages(self) -> "pages.PagesCategory": ...

        @typing.overload
        @property
        def photos(self) -> "photos.PhotosCategory": ...

        @typing.overload
        @property
        def podcasts(self) -> "podcasts.PodcastsCategory": ...

        @typing.overload
        @property
        def polls(self) -> "polls.PollsCategory": ...

        @typing.overload
        @property
        def pretty_cards(self) -> "pretty_cards.PrettyCardsCategory": ...

        @typing.overload
        @property
        def search(self) -> "search.SearchCategory": ...

        @typing.overload
        @property
        def secure(self) -> "secure.SecureCategory": ...

        @typing.overload
        @property
        def stats(self) -> "stats.StatsCategory": ...

        @typing.overload
        @property
        def status(self) -> "status.StatusCategory": ...

        @typing.overload
        @property
        def storage(self) -> "storage.StorageCategory": ...

        @typing.overload
        @property
        def store(self) -> "store.StoreCategory": ...

        @typing.overload
        @property
        def stories(self) -> "stories.StoriesCategory": ...

        @typing.overload
        @property
        def streaming(self) -> "streaming.StreamingCategory": ...

        @typing.overload
        @property
        def translations(self) -> "translations.TranslationsCategory": ...

        @typing.overload
        @property
        def users(self) -> "users.UsersCategory": ...

        @typing.overload
        @property
        def utils(self) -> "utils.UtilsCategory": ...

        @typing.overload
        @property
        def video(self) -> "video.VideoCategory": ...

        @typing.overload
        @property
        def wall(self) -> "wall.WallCategory": ...

        @typing.overload
        @property
        def widgets(self) -> "widgets.WidgetsCategory": ...

    def __getattr__(self, name) -> "BaseCategory":
        if name not in CATEGORIES:
            raise AttributeError(name=name, obj=self)

        module: "BaseCategory" = importlib.import_module(f".methods.{name}", package=__package__)
        category = getattr(module, CATEGORIES[name])
        
        return category(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "ABCAPI":
        pass

    @typing.overload
    async def execute(self, code: ExecutableCode[Response]) -> ExecuteResponse[Response]:
        pass

    @typing.overload
    async def execute(self, code: str) -> ExecuteResponse[typing.Any]:
        pass

    async def execute(self, code: typing.Union[str, ExecutableCode[Response]]) -> ExecuteResponse[typing.Any]:
        data = code.__dict__ if isinstance(code, ExecutableCode) else {"code": code}
        response = await self.api_instance.request("execute", data)
        return ExecuteResponse(response=response)


__all__ = ("APICategories",)
