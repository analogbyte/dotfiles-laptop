# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",
    format="%a %-d %H:%M:%S",)

status.register("temp",
    format="{temp:.0f}°C",)

status.register("battery",
    format="{status}{percentage_design:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

status.register("network",
    interface="enp0s25",
    format_down="{interface}:no connection",
    format_up="{interface}:{v4cidr}",
    ignore_interfaces=['lo'],)

status.register("disk",
    path="/home",
    format="disk:{avail}G",)

status.register("pulseaudio",
    step=1,
    format="♪{volume}",)

status.register("mpd",
    format="{status} {title} - {artist}",
    on_downscroll = "next_song",
    on_upscroll = "previous_song",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

status.run()
