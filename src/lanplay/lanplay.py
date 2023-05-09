import re as _re
from gql import gql as _gql
from typing import Optional as _Optional, List as _List, Dict as _Dict, Generator as _Generator, Union as _Union, Literal as _Literal
import lanplay.functions as _functions

class _Game():
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
        self._id = id
        self._name = _re.search(
            r'<a href="/Title/\w+">(.+?)</a>', name).group(1)
        self._icon_url = _re.search(
            r"url\s*\(\s*(['\"]?)(.*?)\1\s*\)", icon).group(2)
        self._release_date = release_date
        self._publisher = publisher
        self._size = size
        self._playtime = playtime
        self._user_rating = user_rating
        self._base_name = baseName
        self._status = status
        self._regular_price = regular_price
        self._sale_price = sale_price

    def __repr__(self) -> str:
        return self._name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self):
        raise AttributeError("The variable is read-only.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self):
        raise AttributeError("The variable is read-only.")

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self):
        raise AttributeError("The variable is read-only.")

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self):
        raise AttributeError("The variable is read-only.")

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self):
        raise AttributeError("The variable is read-only.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self):
        raise AttributeError("The variable is read-only.")

    @property
    def playtime(self):
        return self._playtime

    @playtime.setter
    def playtime(self):
        raise AttributeError("The variable is read-only.")

    @property
    def user_rating(self):
        return self._user_rating

    @user_rating.setter
    def user_rating(self):
        raise AttributeError("The variable is read-only.")

    @property
    def base_name(self):
        return self._base_name

    @base_name.setter
    def base_name(self):
        raise AttributeError("The variable is read-only.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self):
        raise AttributeError("The variable is read-only.")

    @property
    def regular_price(self):
        return self._regular_price

    @regular_price.setter
    def regular_price(self):
        raise AttributeError("The variable is read-only.")

    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self):
        raise AttributeError("The variable is read-only.")

class _Player():
    """
        Represents a Lan-Play player.

        Attributes
        ----------
        player_name: Name of the player in game.
    """

    def __init__(self, name: str) -> None:
        self._player_name = name

    def __repr__(self) -> str:
        return self._player_name
    
    @property
    def player_name(self):
        return self._player_name
    
    @player_name.setter
    def player_name(self):
        raise AttributeError("The variable is read-only.")


class _Room():
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

    def __init__(self, contentId: _Optional[str] = None, hostPlayerName: _Optional[str] = None, nodeCountMax: _Optional[int] = None, nodeCount: _Optional[int] = None, advertiseData: _Optional[str] = None, nodes: _Optional[_List[_Dict]] = None, games_list: _Optional[_Generator] = None, encoding: _Union[_Literal['utf-8'], _Literal['utf-16']] = 'utf-8') -> None:
        self._content_id = '0100B04011742000' if contentId == 'ffffffffffffffff' else contentId
        self._host_player = _Player(hostPlayerName)
        self._node_count_max = nodeCountMax
        self._node_count = nodeCount
        self._advertise_data = advertiseData
        self._host_player_nintendo_name = bytearray.fromhex(
            self._advertise_data[56:94].replace('00', '')).decode(encoding)
        self._players = [_Player(player.get('playerName'))
                        for player in nodes] if nodes else None
        self._games_list = games_list
        self._game = self.__setGame()

    def __repr__(self) -> str:
        return self.__doc__
    
    @property
    def content_id(self):
        return self._content_id
    
    @content_id.setter
    def content_id(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def host_player(self):
        return self._host_player
    
    @host_player.setter
    def host_player(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def node_count_max(self):
        return self._node_count_max
    
    @node_count_max.setter
    def node_count_max(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def node_count(self):
        return self._node_count
    
    @node_count.setter
    def node_count(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def advertise_data(self):
        return self._advertise_data
    
    @advertise_data.setter
    def advertise_data(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def host_player_nintendo_name(self):
        return self._host_player_nintendo_name
    
    @host_player_nintendo_name.setter
    def host_player_nintendo_name(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self):
        raise AttributeError("The variable is read-only.")

    def __setGame(self):
        if self._content_id:
            for game in self._games_list:
                if game['id'] == self._content_id:
                    return _Game(**game)


class _ServerInfo():
    """
        Represents a Server Info.

        Attributes
        ----------
        online: Number of online players.

        idle: Number of idle players.

        url: URL of the LanPlay server.
    """

    def __init__(self, online: int, idle: int, url: str) -> None:
        self._online = online - idle
        self._idle = idle
        self._url = url

    def __repr__(self) -> str:
        return self.__doc__
    
    @property
    def online(self):
        print(self._online)
        return self._online
    
    @online.setter
    def online(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def idle(self):
        return self._idle
    
    @idle.setter
    def idle(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self):
        raise AttributeError("The variable is read-only.")


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
        self._rooms: _List[_Room] = []
        self._server_info: _ServerInfo = None
        self._servers = _functions._getLanServers(LAN_PLAY_API_KEY)
        self._all_games_url_list = _functions._getAllGamesUrlList()

    def __repr__(self) -> str:
        return self.__doc__

    @property
    def rooms(self):
        return self._rooms
    
    @rooms.setter
    def rooms(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def server_info(self):
        return self._server_info
    
    @server_info.setter
    def server_info(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def servers(self):
        return self._servers
    
    @servers.setter
    def servers(self):
        raise AttributeError("The variable is read-only.")
    
    @property
    def all_games_url_list(self):
        return self._all_games_url_list
    
    @all_games_url_list.setter
    def all_games_url_list(self):
        raise AttributeError("The variable is read-only.")

    def __setServerInfos(func):
        async def inner(self, *args, **kwargs):
            lan_server_url = kwargs.get('lan_server_url') or (args[0] if len(args) > 0 else self._server_info.url if isinstance(self._server_info, _ServerInfo) else None)
            result = await func(self, *args, **kwargs)
            if 'room' in result:
                self._rooms = []
                for room in result['room']:
                    self._rooms.append(
                        _Room(**room, games_list=(game for game in self._all_games_url_list['data'])))
            if 'serverInfo' in result:
                self._server_info = _ServerInfo(**result['serverInfo'], url=lan_server_url)
            return result
        return inner

    @__setServerInfos
    @_functions._sendQuery
    async def setServer(self, lan_server_url: str) -> None:
        """
            Set current working Lan-Play URL.

            Parameters
            ----------
            lan_server_url: URL of the Lan-Play server.
        """
        query = _gql("""   
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

    @__setServerInfos
    @_functions._sendQuery
    async def refreshServer(self) -> None:
        lan_server_url = self._server_info.url if isinstance(self._server_info, _ServerInfo) else None

        if lan_server_url:
            query = _gql("""   
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
        else:
            raise AttributeError("No server set yet.")
