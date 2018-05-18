#!/bin/bash

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo !!"
    exit 1
fi

python3 Main.py --import-file ~/.terminal-session
exit