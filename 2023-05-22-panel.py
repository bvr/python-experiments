
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

console.clear()
user_renderables = [Panel(user, expand=True) for user in ['one', 'two', 'three']]
console.print(Columns(user_renderables))
