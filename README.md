
<h1 align="center"> DEDSEC CLI </h1>
<h4 align="center">A powerful Python library for creating beautiful and customizable command-line interfaces with rich text formatting, banners, tables, and interactive elements.</h4>

`
pip install dedsec-cli
`

### Quick Start

```python
from dedsec_cli import cli

# Create a banner
text = [f'{cli.green_bg}A powerful Python library for creating beautiful and customizable command-line interfaces{cli.reset}', 
		f'developed by {cli.green_blink}0xbit{cli.reset}']

cli.banner(logo="DEDSEC_CLI", logo_color="green", text=text, style=142, align='center', top_space=3, bottom_space=0, text_align="center", text_top_space=0, text_bottom_space=2, width=100) 
```

### INSTALLATION
```
pip install dedsec-cli==1.0
git clone https://github.com/0xbitx/dedsec_cli_utils.git
cd dedsec_cli_utils
python3 sample.py
```

## Display styled text
```python
cli.text(f"{cli.green_bold}Hello World!{cli.reset}", left_padding=2)
```

## Create interactive menus
```python
name = cli.input("Enter your name: ", left_padding=4)
```

## Features
 * Rich Text Styling - Colors, backgrounds, and text effects
 * ASCII Art Banners - Custom fonts and alignment
 * Beautiful Tables - Multiple styles and layout
 * Table Boxes - Boxed content areas
 * Interactive Input - Styled input with validation
 * Menu Systems - Easy menu creation
 * Responsive Design - Auto-width calculations


## Text Styling
The library provides extensive text styling options through dynamic attribute access:

### Colors

```python
cli.red, cli.green, cli.blue, cli.yellow, cli.magenta, cli.cyan
cli.orange, cli.pink, cli.purple, cli.violet, cli.gray, cli.brown
```

### Styles

```python
cli.bold, cli.italic, cli.underline, cli.blink, cli.strike
cli.overline, cli.dim, cli.hidden, cli.faint, cli.bg
```

### Backgrounds
```python
cli.red_bg, cli.green_bg, cli.blue_bg, cli.yellow_bg
```

### Symbols and Indicators
```python
cli.green_dot, cli.red_warning, cli.blue_q
cli.green_leftarrow, cli.green_rightarrow
cli.green_line, cli.violet_line, cli.purple_hash
```

## Usage Examples

### Text Display
```python

# Basic text with padding and margins
cli.text("Normal text", left_padding=4, top_margin=1, bottom_margin=1)

# Styled text examples
cli.text(f"{cli.green_bold}Success message{cli.reset}", left_padding=4)
cli.text(f"{cli.red_warning} Warning: Something went wrong", left_padding=4)
cli.text(f"{cli.blue_q} Question text", left_padding=4)
cli.text(f"{cli.green_dot} List item", left_padding=4)
```

## Banners
Create ASCII art banners with custom fonts and styling:
```python

cli.banner(
    logo="MYAPP",
    style=67,                    # Font style (1-572+)
    align="center",              # Alignment: left, center, right
    top_space=3,                 # Top padding
    bottom_space=1,              # Bottom padding
    text=[                       # Additional text lines
        f"{cli.bold}Subtitle{cli.reset}",
        "Description text"
    ],
    text_align="center",         # Text alignment
    text_top_space=1,            # Text top padding
    text_bottom_space=2,         # Text bottom padding
    width=80,                    # Banner width
    logo_color="green",          # Logo color
    text_color="light_gray"      # Text color
)
```

## Tables
Create beautiful tables with various styles:

```python

headers = ["Name", "Age", "City"]
rows = [
    ["John", "25", "New York"],
    ["Alice", "30", "London"],
    ["Bob", "35", "Tokyo"]
]

# Basic table
cli.table(headers, rows, left_padding=4)

# Styled table
cli.table(
    headers, 
    rows, 
    style="rounded",
    header_color="cyan",
    row_color="white", 
    border_color="purple",
    align="center",
    top_margin=2,
    bottom_margin=1
)
```

## Available Table Styles:
  * default
  * bold
  * double
  * simple
  * rounded

## Table Boxes
Create boxed content areas with multiple styles:

```python

# Single table box
cli.table_box(
    ("INFORMATION",
     "",
     "CVE: 2025-12345",
     "Severity: Critical",
     "Info: Security vulnerability"),
    style="box",
    title_color="green",
    width="auto",
    left_padding=4,
    top_margin=1
)

# Multiple table boxes side by side
cli.table_box(
    ("System", "OS: Linux", "Shell: zsh", "CPU: AMD"),
    ("Network", "IP: 10.0.0.12", "Iface: wlan0", "Status: up"),
    style="smooth",
    width="auto",
    left_padding=5,
    spacing=2,
    content_color="white",
    title_color="yellow"
)
```

## Available Table Box Styles:
   * box
   * bold_box
   * double_box
   * smooth
   * plain
   * simple
   * simple1
   * through
   * simple8

## User Input
Get user input with styling and validation:

```python

# Basic input
name = cli.input("Enter your name: ", left_padding=4)

# Input with default value
option = cli.input("Choose option: ", default="1", left_padding=4)

# Password input (hidden typing)
password = cli.input("Enter password: ", password=True, left_padding=4)

# Input with validation
data = cli.input(
    "Required field: ", 
    allow_empty=False,  # Don't allow empty input
    allow_none=False,   # Don't allow None
    left_padding=4
)

```

## Menu Systems
Create interactive menus:

```python

cli.table_box(
    (f'{cli.green_line} MENU',
     "",
     f" 1. Text Examples",
     f" 2. Input Examples", 
     f" 3. Table Examples"),
    style="plain",
    title_color="white",
    width="auto",
    left_padding=4,
    top_margin=1
)

try:
    select = cli.input(
        "option:", 
        default="1", 
        allow_empty=True,
        left_padding=6
    )
except KeyboardInterrupt:
    exit(0)

if select == "1":
    # Handle option 1
    pass
elif select == "2":
    # Handle option 2
    pass
```

## Advanced Examples
System Information Display

```python
# System info table
cli.table_box(
    ("SYSTEM INFO",
     "",
     f"{cli.green_dot} OS: Linux Ubuntu 22.04",
     f"{cli.green_dot} Kernel: 5.15.0-91-generic", 
     f"{cli.green_dot} Shell: zsh 5.8.1",
     f"{cli.green_dot} CPU: AMD Ryzen 7 5800X",
     f"{cli.green_dot} Memory: 32GB DDR4"),
    style="double_box",
    title_color="green",
    line_color="green",
    width="auto",
    left_padding=4
)
```

## Status Dashboard
```python
headers = ["Component", "Status", "Usage", "Health"]
rows = [
    ["CPU", "Online", "45%", f"{cli.green}Good"],
    ["Memory", "Online", "78%", f"{cli.yellow}Warning"],
    ["Disk", "Online", "92%", f"{cli.red}Critical"],
    ["Network", "Online", "12%", f"{cli.green}Good"]
]

cli.table(
    headers, 
    rows, 
    style="rounded",
    header_color="green",
    row_color="dim_white",
    align="center",
    left_padding=4
)
```

## File System Display
```python
headers = ["Filesystem", "Type", "Disk", "Used", "Use", "Free", "Mount Point"]
rows = [
    ["/dev/nvme0n1p2", "ext4", "SSD", "477G", "90% ████▌", "24G", "/"]
]

cli.table(
    headers, 
    rows, 
    style="default", 
    header_color="cyan", 
    row_color="white"
)
```


## Create ASCII art banners with text.

### Parameters:
```
    logo: Text to display as logo
    style: Font style number (1-572+)
    align: Alignment ("left", "center", "right")
    text: List of additional text lines
    logo_color, text_color: Color names
    width: Banner width

cli.text()
```

## Display styled text with padding.

### Parameters:
```
    message: Text to display
    left_padding: Left padding spaces
    top_margin, bottom_margin: Vertical spacing

cli.table_box()
```

## Create boxed content areas.

### Parameters:
```
    tables: One or more table data tuples
    style: Box style name
    width: Width or "auto"
    content_color, title_color, line_color: Color names
    spacing: Space between multiple tables

cli.table()
```

## Create formatted tables.

### Parameters:
```
    headers: List of column headers
    rows: List of row data
    style: Table style
    header_color, row_color, border_color: Color names
    align: Text alignment ("left", "center", "right")

cli.input()
```

## Get user input with styling.

### Parameters:
```
    prompt: Input prompt text
    default: Default value if empty
    password: Hide input (for passwords)
    allow_empty: Allow empty input
    allow_none: Allow None return
```
## Color Reference
### Basic Colors
```
    black, red, green, yellow, blue, magenta, cyan, white
    gray, brown, pink, purple, orange, violet
```
### Special Colors
```
    dim_white - Dimmed white text
    thin_dim_white - Thin dimmed white
```

## Style Combinations

Combine colors with styles using underscores:

```python
cli.green_bold        # Green bold text
cli.red_underline     # Red underlined text  
cli.blue_bg           # Blue background
cli.yellow_blink      # Yellow blinking text
cli.purple_italic     # Purple italic text
```
