# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import os
import subprocess

mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()
terminal = '/home/vismay/builds/alacritty/target/release/alacritty'

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home+'/.config/qtile/autostart.sh'])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # quick access
    Key([mod], "Return", lazy.spawn("rofi -show window"), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("alacritty -t xplr -e xplr"), desc="Launch terminal"),
    # Key([mod1], "Return", lazy.spawn("rofi -show window"), desc="Launch terminal"),
    Key([mod1], "Tab", lazy.spawn("rofi -show window -auto-select"), desc="Launch terminal"),
    Key([mod1 , "shift"], "Return", lazy.spawn("rofi -show run"), desc="Launch terminal"),
    Key([mod], "o", lazy.spawn(terminal), desc="Launch terminal"),
    KeyChord([mod1], "Return", [
         Key([], "Tab", lazy.spawn("rofi -show window"))
        ,Key([], "d", lazy.spawn("rofi -show drun -show-icon"))
        ,Key([], "e", lazy.spawn("rofi -show emoji -modi emoji"))
        ,Key([], "f", lazy.spawn("alacritty -t xplr -e xplr"))
        ,Key([], "c", lazy.spawn("rofi -show calc -modi calc"))
        ,Key([], "t", lazy.spawn(os.path.expanduser('~/.config/rofi/custom_menu.sh')))
    ]),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # browser
    Key([mod], "m", lazy.spawn("firefox")),

    #emacs
    Key([mod], "u", lazy.spawn("emacs")),

    # change screen not used
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),

    # screen shot
    Key([mod], "Print", lazy.spawn('xfce4-screenshooter')),

    # Volume control
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -c 0 -q set Master toggle")
    ),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#eb4034",
            "border_normal": "#181e23",
            }

layout_theme = init_layout_theme()


layouts = [
    #layout.MonadTall(margin=8, border_width=3, border_focus="#384149", border_normal="#1f252a"),
    #layout.MonadWide(margin=8, border_width=3, border_focus="#384149", border_normal="#1f252a"),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
   ]
"""
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


"""
widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=3,
    margin=3
)
extension_defaults = widget_defaults.copy()

soft_sep = {
    'linewidth': 2, 'size_percent': 80,
    'foreground': '707070', 'padding' :7
}

icon_theme_path = '/usr/share/icons/Adwaita/24x24/status/'
screens = [
    Screen(
        wallpaper= os.path.expanduser('~')+'/.config/qtile/wallpapers/sunset_landscape.jpg',
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Sep(**soft_sep),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Sep(**soft_sep),
                widget.Volume(),
                widget.Sep(**soft_sep),
                widget.Battery(foreground='247052', low_percentage=0.20,
                               low_foreground='fa5e5b', update_delay=10,
                               format='{percent:.0%} {hour:d}:{min:02d} '
                                      '{watt:.2}W'),
                widget.Sep(**soft_sep),
                widget.CheckUpdates(),
                widget.Sep(**soft_sep),
                widget.QuickExit(),
            ],
            30,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["#afedc0", "#afedc0", "#afedc0", "#afedc0"], # Borders are magenta
            opacity=0.8,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="xplr"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
