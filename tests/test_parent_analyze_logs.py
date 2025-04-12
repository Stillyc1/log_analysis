def test_read_file(parent_analyze_logs, log_list):
    logs = parent_analyze_logs.read_file("test_log.txt")
    assert logs == log_list


def test_logs_filter(parent_analyze_logs, log_list):
    filtered_logs = parent_analyze_logs.logs_filter("django.request", log_list)
    assert filtered_logs == [
        "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [127.0.0.1]\n",
        "2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [127.0.0.1]\n",
    ]


def test_logs_sorted(parent_analyze_logs, log_list):
    sorted_logs = parent_analyze_logs.logs_sorted("/\\S+/", log_list)
    assert sorted_logs == ["/admin/dashboard/", "/api/v1/reviews/"]


def test_report_generation(parent_analyze_logs):
    result = parent_analyze_logs.report_generation(
        "test_log.txt", "django.request", "/\\S+/"
    )
    expected_result = {
        "/admin/dashboard/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
        "/api/v1/reviews/": {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
        },
    }
    assert result == expected_result
