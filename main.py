from rich.console import Console
from rich.prompt import Prompt
from libs.styles import info, warning, error, critical, success, default


def mainLoop():
  console.clear(4)
  console.print("🧀 FontinaTP v0.0.1 by ProsD\n", justify="center", style="bold")
  console.rule("[bold]Main Menu", style="gold3")
  console.print("1. Upload a File")
  console.print("2. Download a File")
  console.print("3. Read the Tutorial")
  console.print("4. Exit")
  choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4"], default="1")
  match choice:
    case "1":
     pass
    case "2":
      pass
    case "3":
      pass
    case "4":
      return False
  return True


if __name__ == "__main__":
  console = Console()
  console.style = default
  with console.screen():
    continueVar = True
    while continueVar:
      continueVar = mainLoop()
