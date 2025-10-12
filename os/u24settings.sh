gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Alt>Shift_L']"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo tee /etc/apt/keyrings/sublimehq-pub.asc > /dev/null
echo -e 'Types: deb\nURIs: https://download.sublimetext.com/\nSuites: apt/stable/\nSigned-By: /etc/apt/keyrings/sublimehq-pub.asc' | sudo tee /etc/apt/sources.list.d/sublime-text.sources
sudo apt update && sudo apt upgrade -y
sudo apt install sublime-text sublime-merge
sudo apt install gnome-shell-extension-manager
sudo apt install gnome-tweaks
sudo apt install git
sudo apt install extrepo
sudo extrepo enable librewolf
sudo apt install librewolf
sudo snap install brave
sudo apt install cifs-utils net-tools
sudo apt install vlc
sudo apt install python3-venv
