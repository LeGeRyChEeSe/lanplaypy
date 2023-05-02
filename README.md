<h1 align='center'>LanPlay API</h1>
<p align="center">
<img src="https://github.com/LeGeRyChEeSe/lanplaypy/blob/main/images/lanplay.png?raw=true" align="center" height=205 alt="lanplaypy" />
</p>
<p align="center">
<img src='https://visitor-badge.laobi.icu/badge?page_id=LeGeRyChEeSe.lanplaypy', alt='Visitors'/>
<a href="https://github.com/LeGeRyChEeSe/lanplaypy/stargazers">
<img src="https://img.shields.io/github/stars/LeGeRyChEeSe/lanplaypy" alt="Stars"/>
</a>
<a href="https://github.com/LeGeRyChEeSe/lanplaypy/issues">
<img src="https://img.shields.io/github/issues/LeGeRyChEeSe/lanplaypy" alt="Issues"/>
</a>

<p align="center">
This is the unofficial API for <a href="http://www.lan-play.com">LanPlay</a>.<br>
It's made for getting servers, rooms, games and players easily from LanPlay API.<br>
It was designed to make life easier for developers with LanPlay. It’s a more direct and simple interface with the API.
<p align="center">

## Table of Contents
- [Installation](#installation)
- [Script Example](#script-example)
- [Contributing](#contributing)
- [License](#license)

## Installation

```python
pip install lanplaypy
```

## Script Example

- Here is an example of a simple script using LanPlay API

```python
import asyncio
import lanplay

# The LAN_PLAY_API_KEY can be found in the Console Mode of any Web Browser by following these steps:
# - Open a Web Browser and go to http://www.lan-play.com
# - Open a Console Mode ('Ctrl + Shift + C' should work, or else Google is your friend :))
# - Go to 'Network' tab and refresh the current page
# - Search a line named 'getMonitors' and click on it
# - Open the 'Payload' tab
# - Copy the 'api_key' value and paste it into the LanPlay('LAN_PLAY_API_KEY') definition below

async def main():
    # Create an instance of the LanPlay class with LAN_PLAY_API_KEY
    # It's the main variable where all data will be stored
    lan = lanplay.LanPlay('LAN_PLAY_API_KEY')

    # Initialize the server
    await lan.setServer('joinsg.net:11453') # Or 'http:/joinsg.net:11453/' will works too

    # You can now access all data from 'lan' variable
    # Here are some useful examples below    
    for room in lan.rooms:
        # Display games info of a room
        print(room.host_player_nintendo_name)   # Unique Nintendo host player name
        print(room.game.name)       # Or 'room.game' will also displays the name of the game
        print(room.game.icon_url)   # Useful when you want a cool picture of the current game played
        print(room.game.size)       # To see if you've enough space to download this game on your Switch...
        
        for player in room.players:
            # Display players infos of a room
            print(player.player_name)   # Or 'player' will also displays the name of the player

    print(lan.server_info.online)   # Displays the current number of Online players in the server
    print(lan.server_info.idle)     # Displays the current number of Idle players in the server

    print(lan.servers)      # Useful when you don't know wich LanPlay server to choose...

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

- Or you can also use it in CLI as well with the same syntax.

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request


*Thanks to every [contributors](https://github.com/LeGeRyChEeSe/lanplaypy/graphs/contributors) who have contributed in this project.*

## License

Distributed under the MIT License. See [LICENSE](https://github.com/LeGeRyChEeSe/lanplaypy/blob/main/LICENSE) for more information.

----

Author/Maintainer: [Garoh](https://github.com/LeGeRyChEeSe/) | Discord: GarohRL#4449