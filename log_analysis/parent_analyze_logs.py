import re
from collections import Counter


class ParentAnalyzeLogs:
    """Класс анализа и формирования файлов логирования."""

    def __init__(self, report_name: str, path_to_logs: list):
        self.report_name = report_name
        self.path_to_logs = path_to_logs
        self.total_logs: dict[str, dict] = dict()

    def report_generation(
        self, path_file: str, pattern_filter: str, pattern_sorted: str
    ) -> dict:
        """
        Метод обрабатывает файл с логами,
        формирует структуру отчёта по параметрам и возвращает словарь отсортированных данных.
        """
        total_logs = self.total_logs
        file_logs = self.read_file(path_file)
        logs_filter = self.logs_filter(f"{pattern_filter}", file_logs)
        sorted_handlers = self.logs_sorted(f"{pattern_sorted}", logs_filter)

        counted = Counter(sorted_handlers)
        for k, v in counted.items():
            level_logs = {
                "DEBUG": 0,
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0,
                "CRITICAL": 0,
            }
            for log in range(v):
                # находим элемент в списке логов logs_filter, в котором есть подстрока k, чтобы достать индекс.
                try:
                    result = next(s for s in logs_filter if k in s)
                except StopIteration:
                    continue
                index = logs_filter.index(result)

                log_pop = logs_filter.pop(index)

                # берем уровень лога по индексу и увеличиваем счётчик на 1
                level_log = log_pop.split(" ")[2]
                level_logs[level_log] += 1

            handler = k
            if total_logs.get(handler, None) is None:
                total_logs[handler] = level_logs
            else:
                total_logs[handler] = {
                    k: total_logs[handler].get(k, 0) + level_logs.get(k, 0)
                    for k in total_logs[handler] | level_logs
                }
        return total_logs

    @staticmethod
    def read_file(path: str) -> list[str]:
        """Преобразует файл с логами в список строк."""
        with open(path, "r", encoding="utf-8") as file:
            text = file.readlines()
        return text

    @staticmethod
    def logs_filter(pattern: str, file_logs: list[str]) -> list[str]:
        """Фильтрует список строк, по определённому паттерну."""
        return list(filter(lambda line: re.search(f"{pattern}", line), file_logs))

    @staticmethod
    def logs_sorted(pattern: str, file_logs: list[str]) -> list[str]:
        """Сортируем список строк по определённому паттерну"""
        return sorted(
            [
                re.search(f"{pattern}", log).group()
                for log in file_logs
                if re.search(f"{pattern}", log) is not None
            ]
        )
