#!/usr/bin/env python3
"""
Builds the EMX Controls documentation (English + Russian + Chinese) into ./site
with plain Zensical in offline mode. Cross-platform: Windows, Linux, macOS.

    python build.py                    # create .venv, install Zensical, build
    python build.py --wheels wheels    # install Zensical offline from a local wheel folder
    python build.py --no-install       # use the Zensical from the current environment
    python build.py --package          # also create dist/emx-docs-offline.zip
    python build.py --serve            # build, then serve on http://127.0.0.1:8080

The result is a static, relative-link site: serve it from any web server or sub-path;
`python serve.py` is a zero-dependency local server (search needs HTTP, not file://).

What it runs (you can do the same by hand):

    OFFLINE=true zensical build --clean
    OFFLINE=true zensical build --clean -f ru/mkdocs.yml    # -> ru/site, copied to site/ru
    OFFLINE=true zensical build --clean -f zh/mkdocs.yml    # -> zh/site, copied to site/zh
"""

import argparse
import os
import shutil
import subprocess
import sys
import venv
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
VENV = ROOT / ".venv"


def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    subprocess.run([str(c) for c in cmd], cwd=ROOT, check=True, **kw)


def venv_python() -> Path:
    return VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def install(wheels):
    if sys.version_info < (3, 10):
        sys.exit("Python 3.10 or newer is required (found %s)." % sys.version.split()[0])
    if not venv_python().exists():
        print("Creating virtual environment in", VENV)
        venv.EnvBuilder(with_pip=True).create(VENV)
    py = venv_python()
    pip = [py, "-m", "pip", "install", "-r", "requirements.in"]
    if wheels:
        pip += ["--no-index", "--find-links", wheels]
    run(pip)
    return py


def zensical_cmd(py):
    exe = Path(py).parent / ("zensical.exe" if os.name == "nt" else "zensical")
    if exe.exists():
        return [exe]
    found = shutil.which("zensical")
    if not found:
        sys.exit("zensical not found. Run `python build.py` (without --no-install) or `pip install -r requirements.in`.")
    return [found]


def build(py):
    for d in (SITE, ROOT / "ru" / "site", ROOT / "zh" / "site"):
        shutil.rmtree(d, ignore_errors=True)
    env = dict(os.environ, OFFLINE="true")  # Zensical offline mode: relative links, works from file://
    z = zensical_cmd(py)
    run(z + ["build", "--clean"], env=env)
    run(z + ["build", "--clean", "-f", "ru/mkdocs.yml"], env=env)
    run(z + ["build", "--clean", "-f", "zh/mkdocs.yml"], env=env)
    for lang in ("ru", "zh"):  # Zensical does not allow a site_dir outside the config folder
        shutil.copytree(ROOT / lang / "site", SITE / lang)
    print("\nSite built:", SITE)


def package():
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / "emx-docs-offline.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in SITE.rglob("*"):
            if f.is_file():
                z.write(f, Path("site") / f.relative_to(SITE))
        z.write(ROOT / "serve.py", "serve.py")
        z.writestr("START-HERE.txt", (
            "EMX Controls documentation (offline)\n"
            "=====================================\n\n"
            "Recommended: run (Python 3.8+)  python serve.py  and open http://127.0.0.1:8080/\n"
            "Share on a network:  python serve.py --host 0.0.0.0 --port 8080\n"
            "Or put the site/ folder on any web server (nginx, Apache, IIS ...), also under a sub-path.\n\n"
            "Pages can also be opened straight from disk (site/index.html), but browsers block the\n"
            "search index on file://, so search needs a web server.\n"
            "Russian: /ru/   Chinese: /zh/\n"
        ))
    print("Package:", out, "(%.1f MB)" % (out.stat().st_size / 1e6))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wheels", help="folder with pre-downloaded wheels (fully offline install)")
    ap.add_argument("--no-install", action="store_true", help="skip venv creation and pip install")
    ap.add_argument("--package", action="store_true", help="create dist/emx-docs-offline.zip")
    ap.add_argument("--serve", action="store_true", help="serve the site after the build")
    args = ap.parse_args()

    py = sys.executable if args.no_install else install(args.wheels)
    build(py)
    if args.package:
        package()
    if args.serve:
        run([sys.executable, "serve.py"])


if __name__ == "__main__":
    main()
