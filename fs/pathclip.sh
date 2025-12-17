#!/usr/bin/bash
echo $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS \
| tr -d '\n' \
| xclip -selection clipboard