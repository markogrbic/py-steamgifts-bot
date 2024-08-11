# py-steamgifts-bot
A bot for https://www.steamgifts.com/ written in Python.

# Motivation

The idea behind this project is to have a bot run in the background on your PC and enter giveaways (e.g. your wishlist) while you're away so that you do not miss any potentially interesting giveaways.

# Setup

1) Download the latest [tagged release](https://github.com/markogrbic/py-steamgifts-bot/tags)
2) Navigate to the downladed folde and unzip it and enter it.
    ```
    unzip py-steamgifts-bot-x.x.x.zip
    cd py-steamgifts-bot-x.x.x
    ```
3) Log in to SteamGifts with your browser and [find your PHPSESSID](#find-your-phpsessid) cookie data. Add the cookie data to the settings.ini file located in the src folder and save the file.

## Find your PHPSESSID

__Safari__
1) In the top menu select "Develop" and then click "Show Web Inspector".
2) In the Web Inspector tool click on the "Storage" tab and click on "Cookies".
3) There you will find your PHPSESSID value.

__Firefox__
1) In the top menu select "Tool" and then click "Browser Tools" and finally "Web Developer Tools".
2) In the Web Developer Tools click on the "Storage" tab and click on "Cookies".
3) There you will find your PHPSESSID value.

## Run

__Please note that the bot is configured (hard coded) to run every 15 minutes. Please refrain from shortening this time as this would cause additional stress on the server.__

The bot is currently configured to only enter giveaways in your Wishlist (it also skips any pinned giveaways).
It also waits until you have at least 100 poitns avilable on your account before it starts entering giveaways.
It will also skip pinned gieaways.
These settings can be configured in the provided "settings.ini" file.

You can run the bot through Docker or as a Python script in your terminal.

### Docker

1) From the root project folder run the following to create the image via the included Dockerfile:
    ```
    sudo docker build -t pysgbot .
    ```
2) Enter the following command to create a container and run it:
    ```
    sudo docker run -d --name pysgbot -e PYTHONUNBUFFERED=1 pysgbot
    ```
    This will run it in a detached state and will enable the python output to be included in the docker logs. See https://stackoverflow.com/questions/55200135/python-docker-container-use-print for more info.
3) You can check if the current container is running with the following command:
    ```
    sudo docker ps -a
    ```
4) If you wish to stop or start the existing container you can do it with the following commands:
    ```
    sudo docker container stop <CONTAINER_NAME/ID>
    sudo docker container start <CONTAINER_NAME/ID>
    ```
5) To see the log of the container run the following:
    ```
    sudo docker logs <CONTAINER_NAME/ID>
    ```

### Python

In terminal position yourself in the src folder and Run the following:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

# Features

## Skip Giveaways

It is possbile to skip wishlisted giveaways by including the Steam game URL exactly as provided in the SteamGifts website to the skip_giveaways.txt file.

# Notes

This is based of the code from https://github.com/stilManiac/steamgifts-bot. The original project has a lot of dependencies and no longer works out of the box on latest version of Python without some tweaks. The initial version of this project is a slimmed down version with minimum dependencies.
