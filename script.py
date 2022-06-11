import os
import requests
import base64
import random
import time
import yaml


def main():
    last_path = ""
    while True:
        # Loads YAML config file to get variables defined inside
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)

        api_ver = config["API_VER"]
        guild_id = config["GUILD_ID"]
        auth_token = config["CLIENT_TOKEN"]
        time_one = config["TIME_VAL_1"]
        time_two = config["TIME_VAL_2"]

        # Make the request look less robotic
        x_super_properties = base64.b64encode(
            b'{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","browser_version":"74","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":,"client_event_source":null}'
        )
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

        # Defines the image path as a random choice from the avatar directory
        path = "./avatars/" + random.choice(os.listdir("./avatars"))

        # Checks if the path contains the USAGE markdown file or the last used path, changes if it does
        while "USAGE.md" in path or last_path == path:
            path = "./avatars/" + random.choice(os.listdir("./avatars"))
        last_path = path

        # Encodes the image into base64 data
        with open(path, "rb") as image:
            encoded_image = base64.b64encode(image.read())

        encoded_image = encoded_image.decode("utf-8")

        # Make the request look less robotic
        req_headers = {
            "Sec-Ch-Ua": "Chromium",
            "X-Debug-Options": "bugReporterEnabled",
            "Accept-Language": "en-US",
            "Sec-Cha-Ua-Mobile": "?0",
            "Authorization": auth_token,
            "Content-Type": "application/json",
            "User-Agent": user_agent,
            "X-Super-Properties": x_super_properties,
            "Sec-Cha-Ua-Platform": "Windows",
            "Accept": "*/*",
            "Origin": "https://discord.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/channels/@me",
            "Accept-Encoding": "gzip, deflate",
        }

        # Sets the actual data to send with the request
        req_data = f"""
        {{"avatar": "data:image/png;base64, {encoded_image}"}}
        """

        do_request(guild_id, req_headers, req_data, api_ver)

        # Gets the number of seconds to sleep in as a random number between the two chosen times
        sleepNum = random.randrange(time_one, time_two)
        print(
            f"[+] Next change in:\n{sleepNum} seconds\n{sleepNum / 60} minutes\n{(sleepNum / 60) / 60} hours"
        )
        time.sleep(sleepNum)


def do_request(guild_id, req_headers, req_data, api_ver):
    # Checks to see if a guild ID is defined in the YAML config, then chooses which request to make
    if guild_id == "":
        print(f"[+] No Guild ID found changing global avatar {guild_id}")
        r = requests.patch(
            f"https://discord.com/api/{api_ver}/users/@me",
            headers=req_headers,
            data=req_data,
        )
    else:
        print(f"[+] Guild ID found changing guild {guild_id}")
        r = requests.patch(
            f"https://discord.com/api/{api_ver}/guilds/{guild_id}/members/@me",
            headers=req_headers,
            data=req_data,
        )

    if r.status_code == 200:
        print("[+] Success")
    elif r.status_code == 401:
        print("[-] Invalid discord token")
        quit()
    # Makes sure the program is not accidentally spamming the Discord API
    elif b"AVATAR_RATE_LIMIT" in r.content:
        print("[-] Critical error, please change times or report bug")
        quit()
    else:
        print("[-] An error occured in the program")
        print(r.content)


if __name__ == "__main__":
    main()
