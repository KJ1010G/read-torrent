# read-torrent

A CLI tool to display contents of a .torrent file in json.

## Usage

    git clone https://github.com/KJ1010G/read-torrent.git
    cd read-torrent 
    python readtorrent.py -h

### Real Life Scenario

    > python readtorrent.py ubuntu-24.04.1-desktop-amd64.iso.torrent 
    {
      "announce": "https://torrent.ubuntu.com/announce",
      "announce-list": [
        [
          "https://torrent.ubuntu.com/announce"
        ],
        [
          "https://ipv6.torrent.ubuntu.com/announce"
        ]
      ],
      "comment": "Ubuntu CD releases.ubuntu.com",
      "created by": "mktorrent 1.1",
      "creation date": 1724947415,
      "info": {
        "length": 6203355136,
        "name": "ubuntu-24.04.1-desktop-amd64.iso",
        "piece length": 262144
      }
    }

## Credits

https://github.com/utdemir/bencoder