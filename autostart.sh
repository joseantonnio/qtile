#!/bin/sh
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start Conky
conky -c $HOME/.config/qtile/scripts/system_overview & disown
conky -c $HOME/.config/qtile/scripts/shortcut_keys & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
