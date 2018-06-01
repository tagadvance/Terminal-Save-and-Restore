# Terminal Save and Restore

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
# Note: Leave out `--session project0` to use the default session.

# Add current terminal to the project session with name task0.
tsr --session project --add task0
# List saved terminals.
tsr --session project --list
# Remove terminal with name task1.
tsr --session project --remove task1
# Restore task0.
tsr --session project --restore task0
# Restore all saved terminals.
tsr --session project --restore
```