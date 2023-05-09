import requests
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from typing import Dict

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


def _sendQuery(func):
    """
        A decorator that builds and execute a query with all informations needed to send a compliant request to the LAN-PLAY website.
    """
    async def inner(self, *args, **kwargs):
        url: str = kwargs.get('lan_server_url') or (args[0] if len(args) > 0 else self._server_info.url)
        url = formatUrl(url)
        transport = AIOHTTPTransport(url=url)
        async with Client(
            transport=transport
        ) as session:
            result = await session.execute(*await func(self, *args, **kwargs))
            return result
    return inner

def _getLanServers(API_KEY: str) -> Dict:
    response = requests.post(monitors_url, json={
                                "api_key": API_KEY, "format": "json", "all_time_uptime_ratio": 1})
    return response.json() if response.ok else response

def _getAllGamesUrlList() -> Dict:
    response = requests.get(list_all_games_url)
    return response.json() if response.ok else response