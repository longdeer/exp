gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Alt>Shift_L']"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo tee /etc/apt/keyrings/sublimehq-pub.asc > /dev/null
echo -e 'Types: deb\nURIs: https://download.sublimetext.com/\nSuites: apt/stable/\nSigned-By: /etc/apt/keyrings/sublimehq-pub.asc' | sudo tee /etc/apt/sources.list.d/sublime-text.sources
sudo apt update && sudo apt upgrade -y
sudo apt install sublime-text sublime-merge gnome-shell-extension-manager gnome-tweaks git extrepo cifs-utils net-tools vlc gimp python3-venv virtualbox virtualbox-guest-additions-iso
sudo extrepo enable librewolf
sudo apt install librewolf
sudo snap install brave
