import pytest

from log_analysis.analyze_logs import AnalyzeLogs
from log_analysis.parent_analyze_logs import ParentAnalyzeLogs


@pytest.fixture
def parent_analyze_logs():
    return ParentAnalyzeLogs("handlers", ["log1.log", "log2.log"])


@pytest.fixture
def analyze_logs():
    return AnalyzeLogs("handlers", ["log1.log", "log2.log"])


@pytest.fixture
def log_list():
    return [
        "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [127.0.0.1]\n",
        "2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [127.0.0.1]\n",
        "2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected\n",
        "2025-03-28 12:25:45,000 DEBUG django.db.backends: (0.41) SELECT * FROM 'products' WHERE id = 4;\n",
        "2025-03-28 12:03:09,000 DEBUG django.db.backends: (0.19) SELECT * FROM 'users' WHERE id = 32;\n",
    ]
