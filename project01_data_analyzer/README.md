# Data Analyzer CLI

CLI-инструмент для быстрого анализа CSV-датасетов.  
Загружает данные, показывает статистику, пропуски, корреляции и делает простые автоматические выводы.

## Установка

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Использование

\`\`\`ash
python project01_data_analyzer/analyzer.py --dataset titanic

cd project01_data_analyzer
python analyzer.py --dataset titanic

python analyzer.py --dataset custom --path path/to/your_file.csv
\`\`\`

## Пример вывода

\`\`\`text
=== Отчёт по пропускам ===
Age — 177 (19.9%)
Cabin — 687 (77.1%)
Embarked — 2 (0.2%)

=== Автоматические выводы ===
• Колонка 'Cabin' имеет 77% пропусков — использовать с осторожностью
• 'Pclass' и 'Fare' заметно связаны (корреляция 0.55)
\`\`\`

## Что я использовал

- Python 3
- argparse
- pandas
- rich
- ООП (класс DataAnalyzer)
