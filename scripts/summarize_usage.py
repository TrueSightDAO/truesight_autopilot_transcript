#!/usr/bin/env python3
"""summarize_usage.py — answer "how much did X cost?" from the audit trail.

Scans session usage.jsonl + worker usage/<date>/workers.jsonl and prints a
rollup. Supports --session, --date, --since, and provider/model filters.

Usage:
  summarize_usage.py --session 0ea2405224ff
  summarize_usage.py --date 2026-08-31
  summarize_usage.py --since 2026-08-01 --by provider_model
  summarize_usage.py --since 2026-08-01 --by caller
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


def _iter_lines(path: Path):
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def _collect(session: str | None, date: str | None, since: str | None) -> list[dict]:
    recs: list[dict] = []
    base = Path(".")
    if session:
        sess_root = base / "sessions"
        if sess_root.exists():
            for d in sorted(sess_root.iterdir()):
                p = d / session / "usage.jsonl"
                recs.extend(_iter_lines(p))
    else:
        # worker usage + all session usage for date range
        if date:
            p = base / "usage" / date / "workers.jsonl"
            recs.extend(_iter_lines(p))
            sd = base / "sessions" / date
            if sd.exists():
                for sid in sd.iterdir():
                    recs.extend(_iter_lines(sid / "usage.jsonl"))
        elif since:
            for up in (base / "usage").glob("*/workers.jsonl") if (base / "usage").exists() else []:
                if up.parent.name >= since:
                    recs.extend(_iter_lines(up))
            for sd in (base / "sessions").glob(f"{since[:4]}-*") if (base / "sessions").exists() else []:
                if sd.name >= since:
                    for sid in sd.iterdir():
                        recs.extend(_iter_lines(sid / "usage.jsonl"))
    return recs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--session", default=None)
    ap.add_argument("--date", default=None)
    ap.add_argument("--since", default=None)
    ap.add_argument("--by", choices=["provider_model", "provider", "caller"], default="provider_model")
    args = ap.parse_args(argv)

    recs = _collect(args.session, args.date, args.since)
    if not recs:
        print("no usage records found", file=sys.stderr)
        return 1

    def key(r):
        if args.by == "provider":
            return r.get("provider", "?")
        if args.by == "caller":
            return r.get("caller", "?")
        return f"{r.get('provider','?')}/{r.get('model','?')}"

    agg: dict[str, dict] = defaultdict(
        lambda: {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "est_usd": 0.0}
    )
    for r in recs:
        k = key(r)
        a = agg[k]
        a["calls"] += 1
        a["prompt_tokens"] += int(r.get("prompt_tokens") or 0)
        a["completion_tokens"] += int(r.get("completion_tokens") or 0)
        a["total_tokens"] += int(r.get("total_tokens") or 0)
        a["est_usd"] += float(r.get("est_usd") or 0.0)

    totals = {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "est_usd": 0.0}
    for r in recs:
        totals["calls"] += 1
        totals["prompt_tokens"] += int(r.get("prompt_tokens") or 0)
        totals["completion_tokens"] += int(r.get("completion_tokens") or 0)
        totals["total_tokens"] += int(r.get("total_tokens") or 0)
        totals["est_usd"] += float(r.get("est_usd") or 0.0)

    print(f"records: {totals['calls']}")
    print(f"prompt_tokens: {totals['prompt_tokens']:,}")
    print(f"completion_tokens: {totals['completion_tokens']:,}")
    print(f"total_tokens: {totals['total_tokens']:,}")
    print(f"est_usd: ${totals['est_usd']:.4f}")
    print(f"by {args.by}:")
    for k in sorted(agg, key=lambda kk: -agg[kk]["total_tokens"]):
        a = agg[k]
        print(f"  {k}: calls={a['calls']} tokens={a['total_tokens']:,} est_usd=${a['est_usd']:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
