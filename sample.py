
from dedsec_cli import cli

#ALL BANNER STYLES
# for i in range(0, 572):
#     text = [f'{cli.green_bg}Lorem ipsum is a dummy or placeholdery [{i}] {cli.reset}', f'developed by {cli.green_blink}0xbit{cli.reset}']
#     cli.banner(logo="DEDSEC", logo_color="green", text=text, style=i, align='center', top_space=3, bottom_space=0, text_align="center", text_top_space=0, text_bottom_space=2, width=100) 


#MY SELECTED BANNER STYLE
#banner = [99,142,148,225,226,238,256,287,355,401,417,422,439,452,456,459,468,474,481,342,329,307,287,266,261,239,228,154,136,110,101,97,87,81,482]
# for i in banner:
#     text = [f'{cli.green_bg}Lorem ipsum is a dummy or placeholdery. [{i}] {cli.reset}', f'developed by {cli.green_blink}0xbit{cli.reset}']
#     cli.banner(logo="DEDSEC", logo_color="green", text=text, style=i, align='center', top_space=3, bottom_space=0, text_align="center", text_top_space=0, text_bottom_space=2, width=100) 

cli.banner(logo="DEDSEC", style=67, align="center", width=80, logo_color="green", text=[ f"{cli.bold}Style Utilities{cli.reset}", "Lorem ipsum is a dummy or placeholdery"], text_align="center", text_color="light_gray", top_space=2, bottom_space=1)

cli.table_box(
    (f'{cli.green_line} MENU',
     "",
     f" 1. Text",
     f" 2. Input",
     f" 3. Tables",),

    style="plain",
    title_color=cli.white,
    width="auto",
    left_padding=4,
    top_margin=1,
)

select = cli.input(f"option:", default="1", allow_empty=True, allow_none=False, left_padding=6, top_margin=0)

if select == "1":
    cli.text("Hello World", left_padding=5, top_margin=1)
    cli.text(f"{cli.green_line} Hello World", left_padding=5)
    cli.text(f"{cli.violet_line} Hello World", left_padding=5)
    cli.text(f"{cli.blue_line} Hello World", left_padding=5)
    cli.text(f"{cli.green_dot} Hello World", left_padding=5)
    cli.text(f"{cli.violet_dot} Hello World", left_padding=5)
    cli.text(f"{cli.orange}Hello World", left_padding=5, top_margin=1, bottom_margin=1)
    cli.text(f"{cli.white_italic}Hello World", left_padding=5)
    cli.text(f"{cli.green_blink}Hello World", left_padding=5)
    cli.text(f"{cli.purple_underline}Hello World", left_padding=5)
    cli.text(f"{cli.green_overline}Hello World", left_padding=5)
    cli.text(f"{cli.red_overline}Hello World", left_padding=5)
    cli.text(f"{cli.strike}Hello World", left_padding=5)
    cli.text(f"{cli.bold}Hello World", left_padding=5)
    cli.text(f"{cli.purple_hash} {cli.purple_italic}Hello World", left_padding=5)

    warning_text = 'File "/usr/lib/code/code.py", line 146, in _raw_input'

    cli.text(f"{cli.red_warning} warning: {cli.red_blink}{warning_text}", left_padding=5)

    warning_text = 'File "/usr/lib/code/code.py", line 146, in _raw_input'

    cli.text(f"{cli.red_warning} warning: {cli.red}{warning_text}", left_padding=5)

    cli.text(f"{cli.blue_q} Hello World", left_padding=5)
    cli.text(f"{cli.blue_q}{cli.violet_blink} {cli.italic}Hello World", left_padding=5)
    cli.text(f"{cli.green_leftarrow} Hello World", left_padding=5)
    cli.text(f"{cli.green_rightarrow}{cli.violet_blink} Hello World", left_padding=5)
    cli.text(f"{cli.green_leftarrow} Hello World", left_padding=5)
    cli.text(f"{cli.green_rightarrow} {cli.violet_bg}Hello World", left_padding=5)

elif select == "2":
    name = cli.input(f"{cli.green}Enter your name{cli.reset}: ", password=False, left_padding=6, top_margin=1)
    pwd = cli.input(f"{cli.green}Enter your password{cli.reset}: ", password=True, left_padding=6, top_margin=1)

    cli.table_box(
        (None,
        f" {cli.violet_line} {cli.green}{name} Password{cli.reset}: {cli.blink}{cli.green_bg}{pwd}"),
        title_color=cli.green,
        style="plain",
        width="auto",
        left_padding=4,
    )

elif select == "3": 
    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="plain",
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        ('TITLE',
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        f"Severity: {cli.red}Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="plain",
        title_color=cli.green_blink,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="box",
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="double_box",
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="box",
        title_color=cli.green,
        line_color=cli.thin_dim_white,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="bold_box",
        line_color=cli.green,
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="simple3",
        line_color=cli.orange,
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (None,
        "",
        "Information",
        "",
        "CVE: 2025-12345",
        "Severity: Critical",
        "Info: Lorem ipsum is a dummy or placeholder",),

        style="simple8",
        line_color=cli.violet,
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        ("INFO",
        "",
        "Information",
        "",
        f"{cli.green_dot} CVE: 2025-12345",
        f"{cli.green_dot} Severity: {cli.red}Critical",
        f"{cli.green_dot} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),

        style="box",
        title_color=cli.green,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        ("INFO",
        "",
        "Information",
        "",
        f"{cli.green_dot} CVE: 2025-12345",
        f"{cli.green_dot} Severity: {cli.red}Critical",
        f"{cli.green_dot} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),

        style="simple",
        title_color=cli.green_bg,
        width="auto",
        left_padding=4,
        top_margin=1,
    )

    cli.table_box(
        (f'{cli.green_blink}Information',
        "",
        f"{cli.green_bg}Information",
        "",
        f"{cli.red_dot} CVE: 2025-12345",
        f"{cli.black_dot} Severity: Critical",
        f"{cli.black_dot} Info: Lorem ipsum is a dummy or placeholder",),

        (f'{cli.green_bg}Information',
        "",
        f"{cli.purple_bg}Information",
        "",
        f"{cli.green_leftarrow} CVE: 2025-99999",
        f"{cli.green_leftarrow} Severity: {cli.red}High",
        f"{cli.green_leftarrow} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),

        (f'{cli.violet_italic}Information',
        "",
        "Information",
        "",
        f"{cli.green_hash} CVE: 2025-99999",
        f"{cli.green_hash} Severity: {cli.red}High",
        f"{cli.green_hash} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),
        style="box1",
        width='auto',
        content_color=cli.green,
        left_padding=6,
        top_margin=1,
        spacing=3
    )

    cli.table_box(
        ('INFO',
        "",
        "Information",
        "",
        f"{cli.green_leftarrow} CVE: 2025-12345 Execution",
        f"{cli.green_leftarrow} Severity: {cli.red}Critical{cli.reset}",
        f"{cli.green_leftarrow} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder{cli.reset}",),

        (None,
        "",
        "Information",
        "",
        f"{cli.green_line} CVE: 2025-99999",
        f"{cli.violet_line} Severity: {cli.red}High",
        f"{cli.pink_line} Info: {cli.purple}Lorem ipsum is a dummy or placeholder",),

        (None,
        "",
        "Information",
        "",
        f"{cli.purple_dot} CVE: 2025-99999",
        f"{cli.purple_dot} Severity: {cli.pink}High",
        f"{cli.purple_dot} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),
        style="smooth",
        width="auto",
        content_color=cli.green,
        left_padding=13,
        top_margin=1,
        spacing=5
    )

    cli.table_box(
        ('TABLE 1',
        "",
        "Information",
        "",
        f"{cli.green_leftarrow} CVE: 2025-12345 Execution",
        f"{cli.green_leftarrow} Severity: {cli.red}Critical{cli.reset}",
        f"{cli.green_leftarrow} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder{cli.reset}",),

        ('TABLE 2',
        "",
        "Information",
        "",
        f"{cli.green_line} CVE: 2025-99999",
        f"{cli.violet_line} Severity: {cli.red}High",
        f"{cli.pink_line} Info: {cli.purple}Lorem ipsum is a dummy or placeholder",),

        ('TABLE 3',
        "",
        "Information",
        "",
        f"{cli.purple_dot} CVE: 2025-99999",
        f"{cli.purple_dot} Severity: {cli.pink}High",
        f"{cli.purple_dot} Info: {cli.yellow}Lorem ipsum is a dummy or placeholder",),
        style="smooth",
        width="auto",
        content_color=cli.green,
        left_padding=13,
        top_margin=1,
        spacing=0
    )

    cli.table_box(
        ('INFO',
        "",
        f"{cli.purple_line} Information",
        "",
        f"{cli.red_dot} CVE: 2025-12345 Execution Execution Execution Execution ",
        f"{cli.red_dot} Severity: {cli.red}Critical{cli.reset}",
        f"{cli.red_dot} Info: {cli.red}Lorem ipsum is a dummy or placeholder{cli.reset}",),

        (None,
        "",
        f"{cli.green}Information{cli.reset}",
        "",
        f"{cli.purple_line} Lorem ipsum is a dummy or placeholder",
        f"{cli.purple_line} Severity: {cli.red}High{cli.reset}",
        f"{cli.purple_line} Info: {cli.red}Lorem ipsum is a dummy or placeholder{cli.reset}",),

        style="double_box",
        width="auto",
        content_color=cli.cyan,
        left_padding=5,
        top_margin=1,
        spacing=0
    )

    large_Text = f'''
Lorem ipsum is a dummy or placeholder text commonly used in graphic design, 
publishing, and web development. Its purpose is to permit a page layout 
to be designed, independently of the copy that will subsequently 
'''

    cli.table_box(
        (None,
        large_Text,),
        style="simple8",
        width="auto",
        left_padding=5,
        top_margin=1,
        bottom_margin=1
    )

    cli.table_box(
        (None,
        large_Text,),
        style="box",
        width="auto",
        left_padding=5,
        top_margin=1,
        bottom_margin=1
    )

    cli.table_box(
        ('INFORMATION',
        large_Text,),
        style="smooth",
        width="auto",
        left_padding=5,
        top_margin=1,
        bottom_margin=1
    )
    cli.table_box(
        (f'{cli.violet}INFORMATION',
        large_Text,),
        style="smooth",
        width="auto",
        left_padding=5,
        top_margin=1,
        bottom_margin=1
    )

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
    
    headers = ["Name", "Age", "City"]
    rows = [
        ["John", "25", "New York"],
        ["Alice", "30", "London"],
        ["Bob", "35", "Tokyo"]
    ]

    cli.table(headers, rows, left_padding=6, top_margin=1, bottom_margin=1)

    cli.table(headers, rows, style="rounded", header_color="cyan", row_color="white", border_color="purple", align="center")

    cli.table(headers, rows, left_padding=4, top_margin=2, bottom_margin=1)


    headers = ["filesystem", "type", "disk", "used", "use", "free", "mount point", "dev", "size"]
    rows = [["/dev/nvme0n1p1", "ext4", "SSD", "477G", "90% ████▌", "24G", "/", "259:2", "501G"],
            ["/dev/nvme0n1p2", "ext4", "SSD", "477G", "90% ████▌", "24G", "/", "259:2", "501G"],
            ["/dev/nvme0n1p3", "ext4", "SSD", "477G", "90% ████▌", "24G", "/", "259:2", "501G"]]
    
    cli.table(headers, rows, style="default", header_color="purple", row_color="white", left_padding = 5)


    headers = ["filesystem", "type", "disk", "used", "use", "free", "mount point", "dev", "size"]
    rows = [[f"{cli.red}/dev/nvme0n1p1", "ext4", "SSD", "477G", f"90% {cli.green}████▌", "24G", "/", "259:2", "501G"],
            [f"{cli.green}/dev/nvme0n1p2", "ext4", "SSD", "477G", f"90% {cli.green}████▌", "24G", "/", "259:2", "501G"],
            [f"{cli.yellow}/dev/nvme0n1p3", "ext4", "SSD", "477G", f"90% {cli.green}████▌", "24G", "/", "259:2", "501G"]]

    cli.table(headers, rows, style="classic", header_color="purple", row_color="white", left_padding = 5, top_margin=1, bottom_margin = 1)


    headers = ["INFO"]
    rows = [["Lorem ipsum is a dummy or placeholder text commonly used in graphic  design", 
            f"publishing, and {cli.white_italic}web development{cli.reset}. {cli.purple}Its purpose is to permit a page layout{cli.reset}", 
            "to be designed, independently of the copy that will subsequently"]]
    cli.table(headers, rows, style="info", header_color="purple", left_padding = 5, top_margin=1, bottom_margin = 1, row_color="purple", align="center", text_align="center")


    headers = ["INFO"]
    rows = [["Lorem ipsum is a dummy or placeholder text commonly used in graphic  design", 
            f"publishing, and {cli.purple_bg}web development{cli.reset}. Its purpose is to permit a page layout", 
            "to be designed, independently of the copy that will subsequently"]]
    cli.table(headers, rows, style="info", header_color="white", left_padding = 5, top_margin=1, bottom_margin = 1, row_color="white", align="center", text_align="center")

    headers = ["INFO"]
    rows = [[f"{cli.blink}Lorem ipsum is a dummy or placeholder text commonly used in graphic  design", 
            f"{cli.blink}publishing, and web development. Its purpose is to permit a page layout", 
            f"{cli.blink}to be designed, independently of the copy that will subsequently"]]
    cli.table(headers, rows, style="info", header_color="white", left_padding = 5, top_margin=1, bottom_margin = 1, row_color="purple", align="left", text_align="left")

    headers = ["Component", "Status", "Usage", "Health"]
    rows = [
        ["CPU", "Online", "45%", "Good"],
        ["Memory", "Online", "78%", "Warning"],
        ["Disk", "Online", "92%", "Critical"],
        ["Network", "Online", "12%", "Good"]
    ]
    cli.table(headers, rows, left_padding=7, style="classic", header_color="green", align="center")



    headers = ["Username", "Email", "Role", "Last Login"]
    rows = [
        ["john_doe", "john@example.com", "Admin", "2024-01-15"],
        ["jane_smith", "jane@company.com", "User", "2024-01-14"],
        ["bob_wilson", "bob@test.org", "Moderator", "2024-01-13"]
    ]

    cli.table(headers, rows, style="classic", top_margin=5, bottom_margin=5, border_color="purple", left_padding=5, header_color="purple", row_color="dim_white", align="center")
