# modules/version_control.py

import requests

def check_for_updates():
    try:
        with open("app/version.txt", "r") as version_file:
            version = version_file.read().strip().lower()

        APP_VERSION = version
        VERSION_URL = "https://raw.githubusercontent.com/TheKeops/MyMoney/main/app/version.txt"

        response = requests.get(VERSION_URL)

        if APP_VERSION == response.text.strip().lower():
            return True
        else:
            return False
    except Exception as e:
        return "New version is not controlled! Error Code : " + str(e)
