# Terminal Save and Restore
I recommend having one session per project or workspace. Sessions are stored in `~/.config/terminal-sessions/`.

## Install
```
mkdir ~/git
cd ~/git
git clone https://github.com/tagadvance/Terminal-Save-and-Restore.git
echo "export PATH=\$PATH:~/git/Terminal-Save-and-Restore/" >> ~/.bashrc
source ~/.bashrc
```

## Update
```
cd ~/git/Terminal-Save-and-Restore/
git pull
```

## Usage
```
# Note: Leave out `--session sessionName` to use the default session.

# Add current terminal to the sessionName session with name task0.
# `top` will be run after restoration.
tsr --session sessionName --add task0 --command top
tsr --session sessionName --add task1
# List saved terminals.
tsr --session sessionName --list
# Remove terminal with name task1.
tsr --session sessionName --remove task1
# Restore task0.
tsr --session sessionName --restore task0
# Restore all saved terminals.
sudo tsr --session sessionName --restore
```

## Compatibility
Requires Python 3.6. Tested on Ubuntu 18.04 LTS. Currently only `gnome-terminal` is supported.
