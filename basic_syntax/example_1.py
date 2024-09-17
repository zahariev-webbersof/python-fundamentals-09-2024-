from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Top Programming Languages")

table.add_column("Rank", style="cyan", justify="right")
table.add_column("Language", style="magenta")
table.add_column("Growth", justify="right", style="green")

table.add_row("1", "Python", "+10%")
table.add_row("2", "JavaScript", "+8%")
table.add_row("3", "Rust", "+12%")

console.print(table)
