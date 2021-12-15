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
   ```yaml
   CLIENT_TOKEN: 'YOUR_DISCORD_AUTH_TOKEN_HERE'
   API_VER: 'v9'
   ```
3. Put the images you want to use into the ./avatars directory

4. Edit the time values in `config.yaml` (in seconds) to set how often your avatar should change
   ```yaml
   TIME_VAL_1: TIME_VALUE_1_HERE_SECONDS
   TIME_VAL_2: TIME_VALUE_2_HERE_SECONDS
   ```

## Usage

Run `script.py` through Python or a process manager like pm2

[stars-shield]: https://img.shields.io/github/stars/k200-dev/Discord-Avatar-Automator.svg?style=for-the-badge
[stars-url]: https://github.com/k200-dev/Discord-Avatar-Automator/stargazers
