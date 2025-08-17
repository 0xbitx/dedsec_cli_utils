
dedsec cli-utils: Dedsec UI helpers for Python CLIs

A small utility module for building good-looking terminal interfaces in Python. 


### INSTALLATION
```
pip install dedsec-cli==1.0

git clone https://github.com/0xbitx/dedsec_cli_utils.git
cd dedsec_cli_utils
python3 sample.py
```

### Quick start
```
from dedsec_cli import cli

# Simple colored text with padding
cli.text(f"{cli.green}Ready{cli.reset}", left_padding=2, top_margin=1)

# A nice banner
cli.banner(
    logo="DEDSEC",
    style=67,         
    align="center",
    width=80,
    logo_color="green",
    text=[
        f"{cli.bold}Style Utilities{cli.reset}",
        "Lightweight terminal helpers"
    ],
    text_align="center",
    text_color="light_gray",
    bottom_space=1
)

# Side-by-side tables
cli.table_box(
    ("System", "OS: Linux", "Shell: zsh", "CPU: AMD"),
    ("Network", "IP: 10.0.0.12", "Iface: wlan0", "Status: up"),
    style="smooth",
    width="auto",
    left_padding=5,
    spacing=2,
    content_color=cli.white,
    title_color=cli.yellow,
    line_color=cli.white,
    top_margin=1,
    bottom_margin=1,
)

# Prompt with color and padding
name = cli.input(f"{cli.green}Enter your name{cli.reset}: ", password=False, left_padding=6, top_margin=1)
print(name)
```

### Colors, styles, and symbols
```
#colors
black
red
green
yellow
blue
magenta
cyan
white
gray
brown
pink
purple
orange
violet

print(f'{cli.red} sample')

#styles
bold
faint
italic
underline
blink
bg
hidden
strike
overline

print(f'{cli.italic} sample')
print(f'{cli.orange_italic} sample')
print(f'{cli.blue_bg} sample')

#symbols
dot
line
q
warning
leftarrow
rightarrow
hash
dollar

print(f'{cli.red_dot} sample')
print(f'{cli.purple_line} sample')
print(f'{cli.red_Warning} sample')

```
