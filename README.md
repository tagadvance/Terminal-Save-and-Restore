# Terminal Save and Restore
Allow terminal position, size, current working directory, and virtual environment to be saved and restored. This is useful for preserving terminals between restarts.

## Install
```
mkdir ~/git
cd ~/git
git clone git@github.com:tagadvance/Terminal-Save-and-Restore.git
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