# py-steamgifts-bot
A bot for https://www.steamgifts.com/ written in Python.

# Motivation

The idea behind this project is to have a bot run in the background on your PC and enter giveaways (e.g. your wishlist) while you're away so that you do not miss any potentially interesting giveaways.

# Install and run

Log in to SteamGifts with your browser and find your PHPSESSID cookie data.
Add the cookie data to the settings.ini file and save.

In terminal position yourself in the src folder.

Run the following:
```
python -m venv .venv
source .venv/bin/activate
pip isntall -r requirements.txt
python main.py
```

The bot is currently configured to only enter giveaways in your Wishlist (it also skipps any pinned giveaways).
It also waits untill you have at least 100 poitns avilable onn your account before it starts entering giveaways.

# Notes

This is based of the code from https://github.com/stilManiac/steamgifts-bot. The original project has a lot of dependencies and no longer works out of the box on latest version of Python without some tweaks. The initial version of this project is a slimmed down version with minimum dependencies.
