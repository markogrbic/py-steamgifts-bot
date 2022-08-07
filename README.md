# py-steamgifts-bot
A bot for https://www.steamgifts.com/ written in Python.

# Install and run

Log in to STeamGifts with your browser and find your PHPSESSID cookie data.
Add the cookie data to the settings.ini file and save.

In termianl position yourself in the src folder.

Run the following:
```
python -m venv .venv
source .venv/bin/activate
pip isntall -r requirements.txt
python main.py
```

# Notes

This is based of the code from https://github.com/stilManiac/steamgifts-bot. The original project has a lot of dependencies and no longer works out of the box on latest version of Python without some tweaks. The initial version of this project is a slimmed down version with minimum dependencies.
