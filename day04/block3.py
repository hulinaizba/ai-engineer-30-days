# day04/block3.py
# Дима Еженков — День 4, Блок 3: rich
# Дата: 28.07.2026




from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Мои животные")

table.add_column("Имя", style="cyan")
table.add_column("Тип", style="magenta")
table.add_column("Звук", style="green")

table.add_row("Бобик", "Собака", "Гав!")
table.add_row("Мурка", "Кошка", "Мяу")
table.add_row("Зорька", "Корова", "Му")

console.print(table)
