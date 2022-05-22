[![Stargazers][stars-shield]][stars-url]

## About

Script that changes a users discord avatar from a selection of files at random time intervals, supports server avatars

## Disclaimer

Automating or "self botting" your user account is against Discord's ToS and may get your account banned. If you don't know what a user token is or aren't sure about the risk of getting your account banned do not use this script

### Setup

1. Clone the repo
   ```sh
   git clone https://github.com/k200-dev/Discord-Avatar-Automator
   ```
2. Rename `config.example.yaml` to `config.yaml` and edit the values inside
   ```yaml
   CLIENT_TOKEN: 'YOUR_DISCORD_AUTH_TOKEN_HERE'
   API_VER: 'v9'
   GUILD_ID: ''
   ```
   Leave `GUILD_ID` blank unless you want the script to run on a server avatar

3. Put the images you want to use into the ./avatars directory

4. Edit the time values in `config.yaml` (in seconds) to change the range of times your avatar will change from
   ```yaml
   TIME_VAL_1: TIME_VALUE_1_HERE_SECONDS
   TIME_VAL_2: TIME_VALUE_2_HERE_SECONDS
   ```

## Usage

Run `script.py` through Python or a process manager like pm2

[stars-shield]: https://img.shields.io/github/stars/k200-dev/Discord-Avatar-Automator.svg?style=for-the-badge
[stars-url]: https://github.com/k200-dev/Discord-Avatar-Automator/stargazers
