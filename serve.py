#!/usr/bin/env python3
"""
Zero-dependency static web server for the built documentation site.

    python serve.py                          # http://127.0.0.1:8080/
    python serve.py --port 9000
    python serve.py --host 0.0.0.0           # make it available to the LAN
    python serve.py --root path/to/site

Looks for the site in ./site (after `python build.py`, or from the offline zip).
Uses only the Python standard library (3.8+).
"""

import argparse
import functools
import http.server
import mimetypes
import socketserver
import sys
from pathlib import Path

# Windows takes MIME types from the registry, where .js/.css/.svg are often
# wrong or missing - which makes browsers refuse scripts and styles.
for ext, mime in {
    ".js": "text/javascript", ".mjs": "text/javascript", ".css": "text/css",
    ".json": "application/json", ".svg": "image/svg+xml", ".md": "text/markdown; charset=utf-8",
    ".txt": "text/plain; charset=utf-8", ".woff": "font/woff", ".woff2": "font/woff2",
    ".wasm": "application/wasm", ".xml": "application/xml", ".webp": "image/webp",
}.items():
    mimetypes.add_type(mime, ext)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *a):
        if "-q" not in sys.argv:
            super().log_message(fmt, *a)


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def find_root(explicit):
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve().parent
    cand = here / "site"
    if (cand / "index.html").exists():
        return cand
    sys.exit("Site not found. Run `python build.py` first (or pass --root).")


def main():
    ap = argparse.ArgumentParser(description="Serve the built documentation site.")
    ap.add_argument("--host", default="127.0.0.1", help="bind address (default 127.0.0.1; use 0.0.0.0 for LAN)")
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--root", help="folder with the built site")
    ap.add_argument("-q", action="store_true", help="do not log requests")
    args = ap.parse_args()

    root = find_root(args.root)
    handler = functools.partial(Handler, directory=str(root))
    with Server((args.host, args.port), handler) as srv:
        shown = "localhost" if args.host in ("127.0.0.1", "0.0.0.0") else args.host
        print(f"Serving {root}\n  http://{shown}:{args.port}/   (Ctrl+C to stop)")
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
