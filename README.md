# py-steamgifts-bot
A bot for https://www.steamgifts.com/ written in Python.

# Motivation

The idea behind this project is to have a bot run in the background on your PC and enter giveaways (e.g. your wishlist) while you're away so that you do not miss any potentially interesting giveaways.

# Install and run

Log in to SteamGifts with your browser and find your PHPSESSID cookie data.
Add the cookie data to the settings.ini and save the file.

In terminal position yourself in the src folder.

Run the following:
```
python -m venv .venv
source .venv/bin/activate
pip isntall -r requirements.txt
python main.py
```

The bot is currently configured to only enter giveaways in your Wishlist (it also skips any pinned giveaways).
It also waits until you have at least 100 poitns avilable on your account before it starts entering giveaways.
It will also skip pinned gieaways.
These settings can be configured in the provided "settings.ini" file.

__Please note that the bot is configured (hard coded) to run every 15 minutes. Please refrain from shortening this time as this would cause additional stress on the server.__

# Features

## Skip Giveaways

It is possbile to skip wishlisted giveaways by including the Steam game URL exactly as provided in the SteamGifts website to the skip_giveaway.txt file.

## Docker

Running from Docker is supported via the included Dockerfile.

# Notes

This is based of the code from https://github.com/stilManiac/steamgifts-bot. The original project has a lot of dependencies and no longer works out of the box on latest version of Python without some tweaks. The initial version of this project is a slimmed down version with minimum dependencies.
