from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

wallpaper='~/.config/qtile/assets/wallpaper.png'

bar = bar.Bar(
            [
                widget.Sep(
                    padding=3,
                    linewidth=0,
                    background=colors["background"]
                ),
                widget.Image(
                    filename='~/.config/qtile/assets/menu.png',
                    margin=3,
                    background=colors["background"],
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn("rofi -show combi")
                    }
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    background=colors["background"]
                ),
                widget.GroupBox(
                    highlight_method='line',
                    this_screen_border=colors["purple"],
                    this_current_screen_border=colors["purple"],
                    active=colors["foreground"],
                    inactive=colors["comment"],
                    background=colors["background"]
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground=colors["purple"], fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': (colors["red"], colors["foreground"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(length=5, background=colors["background"]),
                widget.CurrentLayoutIcon(
                    scale=0.6,
                    background=colors["background"]
                ),
                widget.Systray(icon_size=20, background=colors["background"]),
                widget.Spacer(length=5, background=colors["background"]),
                widget.TextBox(
                    text='婢',
                    fontsize=24,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('ponymix toggle')
                    },
                    background=colors["background"],
                    foreground=colors["purple"]
                ),
                widget.TextBox(
                    text='ﱜ',
                    fontsize=24,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('ponymix decrease 5')
                    },
                    background=colors["background"],
                    foreground=colors["purple"]
                ),
                widget.TextBox(
                    text='ﱛ',
                    fontsize=24,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('ponymix increase 5')
                    },
                    background=colors["background"],
                    foreground=colors["purple"]
                ),
                volume,
                widget.Spacer(length=5, background=colors["background"]),
                widget.TextBox(
                    text='',
                    fontsize=24,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('xfce4-terminal -e qalc')
                    },
                    background=colors["background"],
                    foreground=colors["purple"]
                ),
                widget.Spacer(length=5, background=colors["background"]),
                widget.TextBox(
                    text='',
                    font='Font Awesome 5 Free',
                    background=colors["background"],
                    foreground=colors["green"]
                ),
                widget.Clock(format='%a, %d %b %Y %H:%M',
                             background=colors["background"],
                             foreground=colors["green"]),
                widget.Spacer(length=5, background=colors["background"]),
                widget.Spacer(length=5, background=colors["red"]),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('rofi -show p -modi p:rofi-power-menu')
                    },
                    fontsize=20,
                    background=colors["red"],
                    foreground=colors["foreground"]
                ),
                widget.Spacer(length=5, background=colors["red"]),

            ],
            30,
            background=colors["current_line"]
        )

screens = [
    Screen(wallpaper=wallpaper, top=bar),
    Screen(wallpaper=wallpaper, top=bar)
]
