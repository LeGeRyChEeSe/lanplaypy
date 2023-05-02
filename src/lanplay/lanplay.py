import re
import requests
import typing
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from typing import Optional, List, Dict, Generator

list_all_games_url = "https://tinfoil.media/Title/ApiJson/"
monitors_url = "https://api.uptimerobot.com/v2/getMonitors"


def formatUrl(url: str) -> str:
    """
        Format an URL with correct syntax.
    """
    if not url.startswith("http"):
        url = "http://" + url
    if not url.endswith("/"):
        url = url + "/"
    return url


def _send_query(func):
    """
    A decorator that builds and execute a query with all informations needed to send a compliant request to the LAN-PLAY website.
    """
    async def inner(self, *args, **kwargs):
        url: str = kwargs.get('lan_server_url') or args[0]
        url = formatUrl(url)
        transport = AIOHTTPTransport(url=url)
        async with Client(
            transport=transport
        ) as session:
            result = await session.execute(*await func(self, *args, **kwargs))
            return result
    return inner


class Game():
    """
        Represents a Nintendo Game.

        Attributes
        ----------
        id: ID of the game.

        name: Name of the game.

        icon_url: Icon URL of the game.

        release_date: Release date of the game.

        publisher: Name of the publisher of the game.

        size: Size of the game.

        playtime: Playtime of the game.

        user_rating: User rating of the game.

        base_name: Base name of the game.

        status: Status of the game.

        regular_price: Regular price of the game.

        sale_price: Sale price of the game.
    """

    def __init__(self, id: str, name: str, icon: str, release_date: str, publisher: str, size: str, playtime: int, user_rating: float, baseName=None, status=None, regular_price=None, sale_price=None) -> None:
        self.id = id
        self.name = re.search(r'<a href="/Title/\w+">(.+?)</a>', name).group(1)
        self.icon_url = re.search(
            r"url\s*\(\s*(['\"]?)(.*?)\1\s*\)", icon).group(2)
        self.release_date = release_date
        self.publisher = publisher
        self.size = size
        self.playtime = playtime
        self.user_rating = user_rating
        self.base_name = baseName
        self.status = status
        self.regular_price = regular_price
        self.sale_price = sale_price

    def __repr__(self) -> str:
        return self.name


class Player():
    """
        Represents a Lan-Play player.

        Attributes
        ----------
        player_name: Name of the player in game.
    """

    def __init__(self, name: str) -> None:
        self.player_name = name

    def __repr__(self) -> str:
        return self.player_name


class Room():
    """
        Represents a Room with players, games and some other data.

        Attributes
        ----------
        content_id: ID of the current played game in the room.

        host_player: Player with specifics attributes.

        node_count_max: Maximum number of players in the room.

        node_count: Actual number of players in the room.

        advertise_data: Sensitive Nintendo data.

        host_player_nintendo_name: Nintendo name of the host player. (It can be different than the real name of the player in game)

        players: List of Player's in the room.

        game: Actual Game played in the room.
    """

    def __init__(self, contentId: Optional[str] = None, hostPlayerName: Optional[str] = None, nodeCountMax: Optional[int] = None, nodeCount: Optional[int] = None, advertiseData: Optional[str] = None, nodes: Optional[List[Dict]] = None, games_list: Optional[Generator] = None) -> None:
        self.content_id = '0100B04011742000' if contentId == 'ffffffffffffffff' else contentId
        self.host_player = Player(hostPlayerName)
        self.node_count_max = nodeCountMax
        self.node_count = nodeCount
        self.advertise_data = advertiseData
        self.host_player_nintendo_name = bytearray.fromhex(
            self.advertise_data[56:94].replace('00', '')).decode()
        self.players = [Player(player.get('playerName'))
                        for player in nodes] if nodes else None
        self._games_list = games_list
        self.game: Game = None
        self._setGame()

    def __repr__(self) -> str:
        return self.__doc__

    def _setGame(self):
        for game in self._games_list:
            if game['id'] == self.content_id:
                self.game = Game(**game)
                return


class ServerInfo():
    """
        Represents a Server Info.

        Attributes
        ----------
        online: Number of online players.

        idle: Number of idle players.
    """

    def __init__(self, online: int, idle: int) -> None:
        self.online = online
        self.idle = idle

    def __repr__(self) -> str:
        return self.__doc__


class LanPlay():
    """
        Main class for Lan-Play API use.

        Please execute :meth:`setServer` method first to setting the current Lan-Play URL.

        Executing :meth:`setServer` method will automatically modify :class:`LanPlay` settings with correct ones.

        Attributes
        ----------
        rooms: List of Room's available in the current server with specifics attributes.

        server_info: ServerInfo of the server with specifics attributes.

        all_games_url_list: List of all games retrieved from Tinfoil server.
    """

    def __init__(self, LAN_PLAY_API_KEY: str) -> None:
        self.rooms: List[Room] = []
        self.server_info: ServerInfo = None
        self.servers = self._getLanServers(LAN_PLAY_API_KEY)
        self.all_games_url_list = requests.get(list_all_games_url)
        self.all_games_url_list: Dict = self.all_games_url_list.json(
        ) if self.all_games_url_list.ok else self.all_games_url_list

    def __repr__(self) -> str:
        return self.__doc__

    def _getLanServers(self, API_KEY: str) -> typing.Dict:
        response = requests.post(monitors_url, json={
                                 "api_key": API_KEY, "format": "json", "all_time_uptime_ratio": 1})
        return response.json()

    def _setServerInfos(func):
        async def inner(self, *args, **kwargs):
            result = await func(self, *args, **kwargs)
            if 'room' in result:
                for room in result['room']:
                    self.rooms.append(
                        Room(**room, games_list=(game for game in self.all_games_url_list['data'])))
            if 'serverInfo' in result:
                self.server_info = ServerInfo(*result['serverInfo'])
            return result
        return inner

    @_setServerInfos
    @_send_query
    async def setServer(self, lan_server_url: str) -> None:
        """
            Set current working Lan-Play URL.

            Parameters
            ----------
            lan_server_url: URL of the Lan-Play server.
        """
        query = gql("""   
        query getUsers {
            room {
                contentId
                hostPlayerName
                nodeCountMax
                nodeCount
                advertiseData
                nodes {
                    playerName
                }
            }
            serverInfo {
                online
                idle
            }
        }
        """)

        return query,
