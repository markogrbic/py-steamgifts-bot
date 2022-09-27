import configparser

from steamgifts import SteamGifts

print("Welcome to Steam Gifts bot v0.2.2.")

config_file = "settings.ini"
config = configparser.ConfigParser()
config.read(config_file)

if not config['SteamGifts'].get('cookie'):
    print("No cookie settings found.")
    exit()
elif not config['SteamGifts'].get('section'):
    print("No section settings found.")
    exit()
elif not config['SteamGifts'].get('pinned'):
    print("No pinnned settings found.")
    exit()
elif not config['SteamGifts'].get('min_points'):
    print("No minimum points settings found.")
    exit()

cookie = config['SteamGifts'].get('cookie')
website_section_type = config['SteamGifts'].get('section')
pinned = config['SteamGifts'].getboolean('pinned')
min_points = int(config['SteamGifts'].get('min_points'))

sg = SteamGifts(cookie, website_section_type, pinned, min_points)
sg.start()
