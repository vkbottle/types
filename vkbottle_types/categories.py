import typing
from abc import ABC, abstractmethod

from .methods import (
    account,
    ads,
    adsweb,
    app_widgets,
    apps,
    auth,
    board,
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
    users,
    utils,
    video,
    wall,
    widgets,
)

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI


class APICategories(ABC):
    @property
    def account(self) -> account.AccountCategory:
        return account.AccountCategory(self.api_instance)

    @property
    def ads(self) -> ads.AdsCategory:
        return ads.AdsCategory(self.api_instance)

    @property
    def adsweb(self) -> adsweb.AdswebCategory:
        return adsweb.AdswebCategory(self.api_instance)

    @property
    def apps(self) -> apps.AppsCategory:
        return apps.AppsCategory(self.api_instance)

    @property
    def app_widgets(self) -> app_widgets.AppWidgetsCategory:
        return app_widgets.AppWidgetsCategory(self.api_instance)

    @property
    def auth(self) -> auth.AuthCategory:
        return auth.AuthCategory(self.api_instance)

    @property
    def board(self) -> board.BoardCategory:
        return board.BoardCategory(self.api_instance)

    @property
    def database(self) -> database.DatabaseCategory:
        return database.DatabaseCategory(self.api_instance)

    @property
    def docs(self) -> docs.DocsCategory:
        return docs.DocsCategory(self.api_instance)

    @property
    def donut(self) -> donut.DonutCategory:
        return donut.DonutCategory(self.api_instance)

    @property
    def downloaded_games(self) -> downloaded_games.DownloadedGamesCategory:
        return downloaded_games.DownloadedGamesCategory(self.api_instance)

    @property
    def fave(self) -> fave.FaveCategory:
        return fave.FaveCategory(self.api_instance)

    @property
    def friends(self) -> friends.FriendsCategory:
        return friends.FriendsCategory(self.api_instance)

    @property
    def gifts(self) -> gifts.GiftsCategory:
        return gifts.GiftsCategory(self.api_instance)

    @property
    def groups(self) -> groups.GroupsCategory:
        return groups.GroupsCategory(self.api_instance)

    @property
    def lead_forms(self) -> lead_forms.LeadFormsCategory:
        return lead_forms.LeadFormsCategory(self.api_instance)

    @property
    def likes(self) -> likes.LikesCategory:
        return likes.LikesCategory(self.api_instance)

    @property
    def market(self) -> market.MarketCategory:
        return market.MarketCategory(self.api_instance)

    @property
    def messages(self) -> messages.MessagesCategory:
        return messages.MessagesCategory(self.api_instance)

    @property
    def newsfeed(self) -> newsfeed.NewsfeedCategory:
        return newsfeed.NewsfeedCategory(self.api_instance)

    @property
    def notes(self) -> notes.NotesCategory:
        return notes.NotesCategory(self.api_instance)

    @property
    def notifications(self) -> notifications.NotificationsCategory:
        return notifications.NotificationsCategory(self.api_instance)

    @property
    def orders(self) -> orders.OrdersCategory:
        return orders.OrdersCategory(self.api_instance)

    @property
    def pages(self) -> pages.PagesCategory:
        return pages.PagesCategory(self.api_instance)

    @property
    def photos(self) -> photos.PhotosCategory:
        return photos.PhotosCategory(self.api_instance)

    @property
    def podcasts(self) -> podcasts.PodcastsCategory:
        return podcasts.PodcastsCategory(self.api_instance)

    @property
    def polls(self) -> polls.PollsCategory:
        return polls.PollsCategory(self.api_instance)

    @property
    def prettyCards(self) -> pretty_cards.PrettyCardsCategory:
        return pretty_cards.PrettyCardsCategory(self.api_instance)

    @property
    def search(self) -> search.SearchCategory:
        return search.SearchCategory(self.api_instance)

    @property
    def secure(self) -> secure.SecureCategory:
        return secure.SecureCategory(self.api_instance)

    @property
    def stats(self) -> stats.StatsCategory:
        return stats.StatsCategory(self.api_instance)

    @property
    def status(self) -> status.StatusCategory:
        return status.StatusCategory(self.api_instance)

    @property
    def storage(self) -> storage.StorageCategory:
        return storage.StorageCategory(self.api_instance)

    @property
    def store(self) -> store.StoreCategory:
        return store.StoreCategory(self.api_instance)

    @property
    def stories(self) -> stories.StoriesCategory:
        return stories.StoriesCategory(self.api_instance)

    @property
    def streaming(self) -> streaming.StreamingCategory:
        return streaming.StreamingCategory(self.api_instance)

    @property
    def users(self) -> users.UsersCategory:
        return users.UsersCategory(self.api_instance)

    @property
    def utils(self) -> utils.UtilsCategory:
        return utils.UtilsCategory(self.api_instance)

    @property
    def video(self) -> video.VideoCategory:
        return video.VideoCategory(self.api_instance)

    @property
    def wall(self) -> wall.WallCategory:
        return wall.WallCategory(self.api_instance)

    @property
    def widgets(self) -> widgets.WidgetsCategory:
        return widgets.WidgetsCategory(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "ABCAPI":
        pass

    async def execute(self, code: str) -> typing.Any:
        return await self.api_instance.request("execute", {"code": code})
