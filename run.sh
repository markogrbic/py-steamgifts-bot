# Position yourself in the root folder and run "zsh run.sh" or "source run.sh"
# https://stackoverflow.com/questions/61906957/how-to-activate-a-python-virtualenv-using-a-bash-script-and-keep-it-after-the-sc

source src/.venv/bin/activate
cd src
python main.py
