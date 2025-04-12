def test_report_output(capsys, analyze_logs):
    analyze_logs.total_logs = {
        '/admin/dashboard/': {'DEBUG': 0, 'INFO': 1, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0},
        '/api/v1/reviews/': {'DEBUG': 0, 'INFO': 1, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
    }
    analyze_logs.report_output()
    assert capsys.readouterr().out is not None


def test_handlers(capsys, analyze_logs):
    analyze_logs.handlers("test_log.txt")
    assert capsys.readouterr().out is not None
