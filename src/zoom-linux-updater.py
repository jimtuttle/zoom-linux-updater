#!/usr/bin/env python3

from os import remove
from subprocess import run
from sys import exit

import requests


def get_local_zoom_version(version_file):
    try:
        with open(version_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def get_latest_zoom_version(url):
    response = requests.head(url)
    if response.status_code == 302:
        return response.headers['location'].split('/')[-2]
    return None


def download_latest_zoom(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open('/tmp/zoom_latest.deb', 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print("Latest Zoom version downloaded successfully.")
    else:
        print("Failed to download the latest Zoom version.")
        exit(1)


def main():
    version_file = '/opt/zoom/version.txt'
    url = "https://zoom.us/client/latest/zoom_amd64.deb"

    local_version = get_local_zoom_version(version_file)
    if local_version:
        print(f"The currently installed Zoom version is: {local_version}")
    else:
        print("Could not determine the currently installed Zoom version.")
        exit(1)
    latest_version = get_latest_zoom_version(url)
    if latest_version:
        print(f"The latest Zoom version for Linux is: {latest_version}")
    else:
        print("Could not determine the latest Zoom version.")
        exit(1)
    if local_version != latest_version:
        print("A new version of Zoom is available. Downloading...")
        download_latest_zoom(url)
        print("Installing the latest Zoom version...")
        run(['sudo', 'dpkg', '-i', '/tmp/zoom_latest.deb'])
        remove('/tmp/zoom_latest.deb')
        local_version = get_local_zoom_version(version_file)
        if local_version == latest_version:
            print("Zoom has been updated to the latest version successfully.")
        else:
            print("Failed to update Zoom to the latest version.")
            exit(1)
    else:
        print("You already have the latest version of Zoom installed.")


if __name__ == "__main__":
    main()
