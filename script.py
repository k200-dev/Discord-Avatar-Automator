# Imports
import os
import requests
import base64
import random
import time
from dotenv import load_dotenv

# Loads enviroment variables (secrets)
load_dotenv()
# Gets the needed secrets from the loaded env file
clientToken = os.getenv("CLIENT_TOKEN")
apiVer = os.getenv("API_VER")

tiemVal1 = 18000  # 5 hours~
timeVal2 = 25200  # 7 hours~

# Change these if you'd like
xSuperProperties = base64.b64encode(
    b'{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","browser_version":"74","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":,"client_event_source":null}'
)
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

# CHANGE THESE
fileNames = ["cat.png", "cat2.png", "cat3.png", "cat4.png"]

while True:
    # Open the png file as binary and encode it into base64
    with open(random.choice(fileNames), "rb") as image:
        encodedPicture = base64.b64encode(image.read())

    # Decode to utf-8 to remove byte properties
    encodedPicture = encodedPicture.decode("utf-8")

    # Set request headers to make request look more human
    reqHeaders = {
        "Content-Length": "69204",
        "Sec-Ch-Ua": "Chromium",
        "X-Debug-Options": "bugReporterEnabled",
        "Accept-Language": "en-US",
        "Sec-Cha-Ua-Mobile": "?0",
        "Authorization": clientToken,
        "Content-Type": "application/json",
        "User-Agent": userAgent,
        "X-Super-Properties": xSuperProperties,
        "Sec-Cha-Ua-Platform": "Windows",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/channels/@me",
        "Accept-Encoding": "gzip, deflate",
    }

    # Add the payload for the request
    reqData = f"""
    {{"avatar": "data:image/png;base64, {encodedPicture}"}}

    """
    # Send the request to the api, using the correct headers and data
    r = requests.patch(
        f"https://discord.com/api/{apiVer}/users/@me", headers=reqHeaders, data=reqData
    )

    if r.status_code == 200:
        print("[+] Success")
    # Checks for "AVATAR_RATE_LIMIT" in the response to see if the ratelimit has been hit, exits immeditately to avoid spamming the API
    elif b"AVATAR_RATE_LIMIT" in r.content:
        print("[-] Critical error, please change times or report bug")
        quit()
    else:
        print("[-] An error occured in the program")
        print(r.content)
    sleepNum = random.randrange(tiemVal1, timeVal2)
    print(
        f"Next change in:\n{sleepNum} seconds\n{sleepNum / 60} minutes\n{(sleepNum / 60) / 60} hours"
    )
    time.sleep(sleepNum)