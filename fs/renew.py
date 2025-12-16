#!/usr/bin/python3
from os import environ
from pathlib import Path
touchable = Path(environ["NAUTILUS_SCRIPT_SELECTED_FILE_PATHS"].split("\n")[0])
touchable.touch()
