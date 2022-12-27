from libqtile import widget
from libqtile import qtile

colors = dict(
    background="#282a36",
    current_line="#44475a",
    selection="#44475a",
    foreground="#f8f8f2",
    comment="#6272a4",
    cyan="#8be9fd",
    green="#50fa7b",
    orange="#ffb86c",
    pink="#ff79c6",
    purple="#bd93f9",
    red="#ff5555",
    yellow="#f1fa8c"
)

widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume <= 15:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume < 50:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume <= 100:
            self.text = ' ' + str(self.volume) + '%'
        else:
            self.text = ' ' + str(self.volume) + '%'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume <= 15:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume < 50:
            self.text = ' ' + str(self.volume) + '%'
        elif self.volume <= 100:
            self.text = ' ' + str(self.volume) + '%'
        else:
            self.text = ' ' + str(self.volume) + '%'
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")


volume = MyVolume(
    font='Font Awesome 5 Free',
    foreground=colors["purple"],
    background=colors["background"],
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
