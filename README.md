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

# Table of Contents
- [Installation](#installation)
- [Get API Key](#get-api-key)
- [Script Example](#script-example)
- [Contributing](#contributing)
- [License](#license)

## Installation

```python
pip install lanplaypy
```

## Get API Key
To use the LanPlay package you will need a specific, non-transferable API key that can be retrieved from <a href="http://www.lan-play.com">LanPlay</a>.<br>
Please follow these steps :

1. Open a Web Browser and go to http://www.lan-play.com
2. Open a Console Mode (<b>Ctrl + Shift + C</b> should work, or Google is your friend to find how to access the Console Mode 🫠)
3. Go to <b>Network</b> tab and refresh the current page
4. Search a line named <b>getMonitors</b> and click on it
5. Open the <b>Payload</b> tab
6. Copy the <b>api_key</b> value and paste it into the <b>LanPlay('LAN_PLAY_API_KEY')</b> definition below (replace 'LAN_PLAY_API_KEY' with the <b>api_key</b> value)


## Script Example
### Before doing anything be sure to get your <b>api_key</b> from [Get API Key](#get-api-key) section
Here is an example of a simple script using LanPlay API that gets server infos refreshed every 1 second

```python
import asyncio
import lanplay
import time
import os


async def main(time_to_refresh: int = 1):
    # time_to_refresh let you update the informations of the server every 1 seconds
    # You can change this variable from execution in loop.run_until_complete(main()) at the end of this script with some other values
    # For example to update the infos of the server every 0.5 seconds or 500ms, you can use await main(0.5)

    lan = lanplay.LanPlay('LAN_PLAY_API_KEY')
    # Create an instance of the LanPlay class with LAN_PLAY_API_KEY
    # It's the main variable where all data will be stored

    print('List of all LanPlay servers available : ', lan.servers)
    # Useful when you don't know wich LanPlay server to choose...

    await lan.setServer('joinsg.net:11453')
    # Initialize the server with any LanPlay server you want
    # Here is an example with the joinsg.net:11453 server
    # Replace with 'http:/joinsg.net:11453/' will works too

    # You can now access all data from 'lan' variable

    while True:
        os.system('clear')
        # Clear the console to get a clean UI with updated server's infos

        # See below some useful examples

        for room in lan.rooms:
            # Display games info of a room

            print(room.advertise_data)
            print(f'Room {lan.rooms.index(room) + 1} :')
            print('Host Player : ', room.host_player)
            print('Unique Nintendo Host Player Name : ',
                  room.host_player_nintendo_name)
            # Unique Nintendo host player name

            if room.game:
                print('Game : ', room.game.name)
                # Or 'room.game' will also displays the name of the game

                print('Icon URL of the Game : ', room.game.icon_url)
                # Useful when you want a cool picture of the current game played

                print('Game Size : ', room.game.size)
                # To see if you've enough space to download this game on your Switch...

                print('Publisher of the Game : ', room.game.publisher)
                # Get the publisher of the actual played game

            print('Max Players number in the room : ', room.node_count_max)
            # Max Players allowed to play in a room

            print('Actual number of Players in the room: ', room.node_count)
            # Actual number of Players playing in a room

            for player in room.players:
                # Display players infos of a room

                print(f'Player {room.players.index(player) + 1} : ', player)
                # Or 'player.player_name' will also displays the name of the player

        print('Players Online : ', lan.server_info.online)
        # Displays the current number of Online players in the server

        print('Players Idle : ', lan.server_info.idle)
        # Displays the current number of Idle players in the server

        await lan.refreshServer()
        # Function that refresh all infos of the server, rooms, games and players to stay up-to-date

        time.sleep(time_to_refresh)
        # Wait 'time_to_refresh' seconds (1 second in this example) before continue the loop

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