import os
import sys

from log_analysis.analyze_logs import AnalyzeLogs


def main():
    enter_consol = sys.argv  # Считываем с терминала запрос
    if len(enter_consol) >= 2 and enter_consol[-2] != "--report":
        raise Exception("Необходимо указать название отчёта, с помощью флага --report")

    report_name = enter_consol[-1]
    paths = enter_consol[1:-2]  # Забираем пути до файлов с логами

    analyze_logs = AnalyzeLogs(report_name, paths)
    report = analyze_logs.__getattribute__(
        report_name
    )  # Находим метод по флагу --report для выполнения отчёта

    for path in paths:
        if not os.path.exists(path):
            raise Exception(f"Файл '{path}' не существует, укажите правильный путь.")
        report(path)

    analyze_logs.report_output()


if __name__ == "__main__":
    main()
