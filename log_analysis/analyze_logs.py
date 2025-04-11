from log_analysis.parent_analyze_logs import ParentAnalyzeLogs


class AnalyzeLogs(ParentAnalyzeLogs):
    """Класс анализа файлов логирования."""

    def __init__(self, report_name: str, path_to_logs: list):
        super().__init__(report_name, path_to_logs)

    def report_output(self) -> None:
        """Формируем отчёт, выводим в терминал"""

        header = f"{self.report_name.upper()}"
        total_counts = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
        print(f"{header:<20}" + "".join(f"{head:<20}" for head in total_counts.keys()))

        for key, value in self.total_logs.items():
            for level, count in value.items():
                total_counts[level] += count
            print(f"{key:<20}" + "".join([f"{x:<20}" for x in value.values()]))

        print(
            "_" * 120
            + "\n"
            + " " * 20
            + "".join([f"{x:<20}" for x in total_counts.values()])
        )
        print(f"Total requests: {sum([x for x in total_counts.values()])}")

    def handlers(self, path: str) -> None:
        """
        Отчёт о состоянии ручек API по каждому уровню логирования
        """
        self.report_generation(path, "django.request", "/\\S+/")

    def bubble(self, path: str) -> None:
        """
        Отчёт о состоянии статусов запросов API по каждому уровню логирования
        """
        self.report_generation(path, "GET", " \\d\\d\\d ")
