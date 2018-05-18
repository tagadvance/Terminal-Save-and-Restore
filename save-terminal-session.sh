#!/bin/bash

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo !!"
    exit 1
fi

python3 Main.py --export-file ~/.terminal-session >/tmp/save-terminal-session.log 2>/tmp/save-terminal-session.err-log &
