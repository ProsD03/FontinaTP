from rich.style import Style

default = Style(color="gold1")
info = Style(color="cyan")
success = Style(color="green")
warning = Style(color="dark_orange", bold=True)
error = Style(color="red1", bold=True)
critical = Style(color="red1", bgcolor="white", bold=True, blink=True)