import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent


def run(args, cwd):
    return subprocess.run(
        [sys.executable, str(SCRIPTS / args[0]), *args[1:]], capture_output=True, text=True, cwd=cwd
    )


@pytest.fixture
def tmp_session(tmp_path):
    d = tmp_path / "sessions" / "2026-08-31" / "abc123def456"
    d.mkdir(parents=True)
    return tmp_path


def test_append_usage_creates_session_file(tmp_session):
    rec = {
        "provider": "deepseek",
        "model": "deepseek-chat",
        "caller": "chat",
        "prompt_tokens": 100,
        "completion_tokens": 20,
        "total_tokens": 120,
        "est_usd": 0.001,
        "latency_ms": 500,
        "had_tool_calls": True,
        "finish_reason": "stop",
    }
    r = run(
        ["append_usage.py", "--session", "abc123def456", "--date", "2026-08-31", "--json", json.dumps(rec)],
        tmp_session,
    )
    assert r.returncode == 0, r.stderr
    p = tmp_session / "sessions" / "2026-08-31" / "abc123def456" / "usage.jsonl"
    assert p.exists()
    row = json.loads(p.read_text().strip().splitlines()[0])
    assert row["provider"] == "deepseek"
    assert row["session_id"] == "abc123def456"
    assert row["schema_version"] == 1


def test_append_usage_rejects_missing_required(tmp_session):
    r = run(
        ["append_usage.py", "--session", "abc123def456", "--date", "2026-08-31", "--json", '{"provider":"deepseek"}'],
        tmp_session,
    )
    assert r.returncode == 2
    assert "required" in r.stderr


def test_append_usage_worker_path(tmp_session):
    rec = {"provider": "grok", "model": "grok-4-1-fast-non-reasoning", "caller": "aws_monitor", "total_tokens": 50}
    r = run(["append_usage.py", "--worker", "--date", "2026-09-01", "--json", json.dumps(rec)], tmp_session)
    assert r.returncode == 0, r.stderr
    p = tmp_session / "usage" / "2026-09-01" / "workers.jsonl"
    assert p.exists()
    row = json.loads(p.read_text().strip().splitlines()[0])
    assert row["session_id"] is None


def test_write_meta_creates_and_merges(tmp_session):
    r = run(
        ["write_meta.py", "--session", "abc123def456", "--date", "2026-08-31", "--json", '{"governor":"Gary Teh","msg_count":10}'],
        tmp_session,
    )
    assert r.returncode == 0, r.stderr
    p = tmp_session / "sessions" / "2026-08-31" / "abc123def456" / "meta.json"
    m = json.loads(p.read_text())
    assert m["governor"] == "Gary Teh"
    assert m["msg_count"] == 10
    assert m["session_id"] == "abc123def456"
    # merge preserves existing
    r = run(["write_meta.py", "--session", "abc123def456", "--date", "2026-08-31", "--json", '{"msg_count":12}'], tmp_session)
    m2 = json.loads(p.read_text())
    assert m2["governor"] == "Gary Teh"
    assert m2["msg_count"] == 12


def test_summarize_session(tmp_session):
    for i in range(3):
        rec = {
            "provider": "deepseek",
            "model": "deepseek-chat",
            "caller": "chat",
            "prompt_tokens": 1000,
            "completion_tokens": 200,
            "total_tokens": 1200,
            "est_usd": 0.01,
        }
        run(["append_usage.py", "--session", "abc123def456", "--date", "2026-08-31", "--json", json.dumps(rec)], tmp_session)
    r = run(["summarize_usage.py", "--session", "abc123def456"], tmp_session)
    assert r.returncode == 0, r.stderr
    assert "records: 3" in r.stdout
    assert "total_tokens: 3,600" in r.stdout
    assert "deepseek/deepseek-chat" in r.stdout
