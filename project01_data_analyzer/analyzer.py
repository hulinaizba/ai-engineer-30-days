#!/usr/bin/env python3
# project01_data_analyzer/analyzer.py
# Дима Еженков — Проект 1: CLI Data Analyzer
# Дата: 30.07.2026

import argparse
import sys
import pandas as pd
from rich.console import Console
from rich.table import Table


def parse_args():
    parser = argparse.ArgumentParser(description="CLI-анализатор CSV-датасетов")
    parser.add_argument(
        "--dataset",
        choices=["titanic", "custom"],
        required=True,
        help="Какой датасет использовать: titanic или custom"
    )
    parser.add_argument(
        "--path",
        help="Путь к локальному CSV-файлу (нужен только для --dataset custom)"
    )
    return parser.parse_args()


def load_dataset(choice, path=None):
    if choice == "titanic":
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        return pd.read_csv(url)
    elif choice == "custom":
        if not path:
            print("Ошибка: для --dataset custom нужно указать --path")
            sys.exit(1)
        try:
            return pd.read_csv(path)
        except FileNotFoundError:
            print(f"Ошибка: файл '{path}' не найден")
            sys.exit(1)


class DataAnalyzer:
    def __init__(self, df):
        self.df = df
        self.console = Console()

    def basic_info(self):
        self.console.print("\n[bold cyan]=== Базовая информация ===[/bold cyan]")
        self.console.print(f"Размер: {self.df.shape[0]} строк, {self.df.shape[1]} колонок")
        self.console.print(f"Колонки: {list(self.df.columns)}")
        self.console.print("\nТипы данных и пропуски:")
        print(self.df.info())

    def numeric_summary(self):
        self.console.print("\n[bold cyan]=== Статистика по числовым колонкам ===[/bold cyan]")
        print(self.df.describe())

    def missing_report(self):
        self.console.print("\n[bold cyan]=== Отчёт по пропускам ===[/bold cyan]")
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]

        if missing.empty:
            self.console.print("Пропусков нет")
            return

        table = Table(title="Пропуски")
        table.add_column("Колонка")
        table.add_column("Количество")
        table.add_column("Процент")

        total = len(self.df)
        for col, count in missing.items():
            pct = count / total * 100
            table.add_row(col, str(count), f"{pct:.1f}%")

        self.console.print(table)

    def top_correlations(self):
        self.console.print("\n[bold cyan]=== Корреляции ===[/bold cyan]")
        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            self.console.print("Недостаточно числовых колонок для корреляции")
            return

        corr = numeric_df.corr()
        print(corr.round(2))

    def full_report(self):
        self.basic_info()
        self.numeric_summary()
        self.missing_report()
        self.top_correlations()

        self.console.print("\n[bold green]=== Автоматические выводы ===[/bold green]")

        # Пропуски
        missing = self.df.isnull().sum()
        for col, count in missing.items():
            pct = count / len(self.df) * 100
            if pct > 50:
                self.console.print(f"• Колонка '{col}' имеет {pct:.0f}% пропусков — использовать с осторожностью")

        # Корреляции
        numeric_df = self.df.select_dtypes(include="number")
        if numeric_df.shape[1] >= 2:
            corr = numeric_df.corr().abs()
            for i in range(len(corr.columns)):
                for j in range(i + 1, len(corr.columns)):
                    val = corr.iloc[i, j]
                    if val > 0.5:
                        col1 = corr.columns[i]
                        col2 = corr.columns[j]
                        self.console.print(f"• '{col1}' и '{col2}' заметно связаны (корреляция {val:.2f})")


def main():
    args = parse_args()
    df = load_dataset(args.dataset, args.path)
    analyzer = DataAnalyzer(df)
    analyzer.full_report()


if __name__ == "__main__":
    main()
