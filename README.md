[![Stargazers][stars-shield]][stars-url]

## About

Python script that changes a users discord avatar from a selection of files at random time intervals

## Disclaimer

Automating or "self botting" your user account is against Discord's ToS and getting banned from Discord is possible 

### Built With

* [Python 3](https://www.python.org/)

### Setup

1. Clone the repo
   ```sh
   git clone https://github.com/k200-dev/Discord-Avatar-Automator
   ```
2. Rename `config.example.yaml` to `config.yaml` and edit the values inside
   ```sh
   CLIENT_TOKEN: 'YOUR_DISCORD_AUTH_TOKEN_HERE'
   API_VER: 'v9'
   ```
3. Put the images you want into this directory

4. Edit the array in `config.yaml` to have the file names
   ```python
   FILE_NAMES : ["FILE_1_HERE", "FILE_2_HERE", "FILE_3_HERE", "FILE_4_HERE"]
   ```

5. Edit the time values in `script.py` (in seconds) to set how often your avatar should change
   ```python
   tiemVal1 = MINIMUM_TIME_HERE
   timeVal2 = MAXIMUM_TIME_HERE
   ```

## Usage

Run `script.py` through Python or a process manager like pm2

[stars-shield]: https://img.shields.io/github/stars/k200-dev/Discord-Avatar-Automator.svg?style=for-the-badge
[stars-url]: https://github.com/k200-dev/Discord-Avatar-Automator/stargazers
