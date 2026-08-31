#!/usr/bin/env python3
"""write_meta.py — upsert session meta.json (SCHEMA.md §1).

Merges provided fields into sessions/<date>/<sid>/meta.json, preserving
existing fields not present in the update (idempotent re-runs safe).

Usage:
  write_meta.py --session 0ea2405224ff --date 2026-08-31 \
      --json '{"governor":"Gary Teh","msg_count":484}'
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULTS = {
    "session_id": None,
    "governor": None,
    "governor_email": None,
    "started_at": None,
    "ended_at": None,
    "msg_count": 0,
    "providers_used": [],
    "models_used": [],
    "total_prompt_tokens": 0,
    "total_completion_tokens": 0,
    "total_tokens": 0,
    "est_usd": None,
    "tool_calls_invoked": [],
    "outcome": "completed",
    "client": None,
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--session", required=True, help="session_id (hex, 12 chars)")
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--json", dest="json_str", required=True, help="meta fields as JSON")
    args = ap.parse_args(argv)

    try:
        update = json.loads(args.json_str)
    except json.JSONDecodeError as e:
        print(f"error: invalid --json: {e}", file=sys.stderr)
        return 2
    if not isinstance(update, dict):
        print("error: --json must be an object", file=sys.stderr)
        return 2

    path = Path("sessions") / args.date / args.session / "meta.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    meta = DEFAULTS.copy()
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(existing, dict):
                meta.update(existing)
        except json.JSONDecodeError:
            print(f"warning: existing {path} unparsable — overwriting", file=sys.stderr)
    meta.update(update)
    meta["schema_version"] = 1
    meta["session_id"] = args.session
    if not meta.get("started_at") and update.get("started_at"):
        meta["started_at"] = update["started_at"]
    meta["updated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
