#!/usr/bin/env python3
"""Render 1280x640 social preview cards for the pinned repos.

GitHub has no API for social preview images, so these are generated here and
uploaded by hand under Settings -> Social preview.
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
W, H = 1280, 640
BG = "#0f172a"
FG = "#f8fafc"
MUTED = "#94a3b8"
ACCENT = "#38bdf8"

CARDS = [
    {
        "name": "benchmark-harness",
        "kicker": "X12 STREAMING PARSER",
        "number": "255,000 transactions",
        "line1": "14.2 s inside a 25 MB V8 heap cap",
        "line2": "node-x12 takes 49% longer under the same cap",
    },
    {
        "name": "valkey-kv-l2",
        "kicker": "KV CACHE TIERED INTO VALKEY",
        "number": "200 of 200",
        "line1": "sequences served, against 4 of 200 with a fixed pool",
        "line2": "restore beats prefill only above ~4k tokens",
    },
    {
        "name": "kv-serving-scheduler",
        "kicker": "KV SERVING SCHEDULER",
        "number": "120% of capacity",
        "line1": "admission control and preemption against a block budget",
        "line2": "p99 TTFT and goodput per policy",
    },
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(card):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect x="0" y="0" width="{W}" height="8" fill="{ACCENT}"/>
<text x="96" y="170" font-family="DejaVu Sans, sans-serif" font-size="26" letter-spacing="6" fill="{ACCENT}">{esc(card['kicker'])}</text>
<text x="96" y="320" font-family="DejaVu Sans, sans-serif" font-size="88" font-weight="bold" fill="{FG}">{esc(card['number'])}</text>
<text x="96" y="410" font-family="DejaVu Sans, sans-serif" font-size="34" fill="{FG}">{esc(card['line1'])}</text>
<text x="96" y="466" font-family="DejaVu Sans, sans-serif" font-size="34" fill="{MUTED}">{esc(card['line2'])}</text>
<text x="96" y="570" font-family="DejaVu Sans, sans-serif" font-size="24" fill="{MUTED}">github.com/DrMkdaddy/{esc(card['name'])}</text>
</svg>
"""


def main():
    for card in CARDS:
        stem = HERE / card["name"]
        stem.with_suffix(".svg").write_text(svg(card))
        subprocess.run(
            ["rsvg-convert", "-w", str(W), "-h", str(H),
             str(stem.with_suffix(".svg")), "-o", str(stem.with_suffix(".png"))],
            check=True,
        )
        print(f"wrote {stem.with_suffix('.png')}")


if __name__ == "__main__":
    main()
