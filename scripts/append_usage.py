#!/usr/bin/env python3
"""append_usage.py — append one LLM usage row to the transcript audit trail.

Schema (SCHEMA.md §3 / §4): one JSON object per line, append-only.
  session usage -> sessions/<date>/<sid>/usage.jsonl
  worker usage  -> usage/<date>/workers.jsonl   (session_id = null)

Usage:
  append_usage.py --json '{"provider":"deepseek","model":"deepseek-chat",...}'
  append_usage.py --worker --date 2026-09-01 --json '{...}'
  echo '{...}' | append_usage.py --session 0ea2405224ff --date 2026-08-31
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = {"provider", "model", "caller"}
# "ts" is auto-set if absent
KNOWN = {
    "provider",
    "model",
    "caller",
    "session_id",
    "turn",
    "round",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
    "cached_tokens",
    "est_usd",
    "latency_ms",
    "had_tool_calls",
    "finish_reason",
    "ts",
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def validate(rec: dict) -> list[str]:
    errs = [f"missing required field: {k}" for k in REQUIRED if k not in rec]
    unknown = [k for k in rec if k not in KNOWN]
    if unknown:
        errs.append(f"unknown field(s): {', '.join(sorted(unknown))}")
    return errs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--session", metavar="SID", help="session_id (hex, 12 chars)")
    src.add_argument("--worker", action="store_true", help="worker call (no session)")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--json", dest="json_str", default=None, help="usage record as JSON string")
    ap.add_argument("--file", default=None, help="read record from file ('-' = stdin)")
    args = ap.parse_args(argv)

    if args.json_str:
        try:
            rec = json.loads(args.json_str)
        except json.JSONDecodeError as e:
            print(f"error: invalid --json: {e}", file=sys.stderr)
            return 2
    elif args.file:
        try:
            raw = sys.stdin.read() if args.file == "-" else Path(args.file).read_text()
            rec = json.loads(raw)
        except (OSError, json.JSONDecodeError) as e:
            print(f"error: cannot read record: {e}", file=sys.stderr)
            return 2
    else:
        print("error: --json or --file required", file=sys.stderr)
        return 2

    errs = validate(rec)
    if errs:
        print("error: " + "; ".join(errs), file=sys.stderr)
        return 2

    rec.setdefault("schema_version", 1)
    rec.setdefault("ts", _now_iso())
    if args.worker:
        rec["session_id"] = None
    elif "session_id" not in rec or not rec["session_id"]:
        rec["session_id"] = args.session

    date = args.date or _now_iso()[:10]
    if args.worker:
        path = Path("usage") / date / "workers.jsonl"
    else:
        sid = rec.get("session_id")
        if not sid:
            print("error: --session required (or session_id in record)", file=sys.stderr)
            return 2
        path = Path("sessions") / date / sid / "usage.jsonl"

    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(rec, sort_keys=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"appended -> {path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
