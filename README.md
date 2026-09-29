# EMX Controls Documentation — offline edition

**English** · [Русский](README.ru.md)

Source of the documentation site for **Eremex Avalonia UI Controls** (EMX Controls) in three
languages: English, Russian (`/ru/`) and Chinese (`/zh/`). This repository lets you host a copy
of the site **in an air-gapped network with no internet access**: the built site is plain static
files; fonts, search and images are bundled, and no CDNs or analytics are used.

Official site: <https://eremexcontrols.net/>

## Fastest way: prebuilt package

1. On a machine with internet, open **Releases** in this repository and download `emx-docs-offline.zip`
   (or take the artifact of the latest run under **Actions**).
2. Move the archive into the closed network and unzip it.
3. Install Python 3.8+ and run:

   ```bash
   python serve.py
   ```

4. Open <http://127.0.0.1:8080/> (Russian: `/ru/`, Chinese: `/zh/`).

To share it with colleagues on the network:

```bash
python serve.py --host 0.0.0.0 --port 8080
```

Instead of `serve.py` you can serve the `site/` folder with any web server (nginx, Apache, IIS, Caddy) as static files.

> **Note.** The site is built with plain [Zensical](https://zensical.org/) in its *offline mode*: all links
> are relative, so it works from any folder or URL sub-path (e.g. `https://intranet/docs/`). Pages can also be
> opened straight from disk (`site/index.html`), but browsers block search index loading on `file://`,
> so use a web server (`serve.py` is enough) if you need the search box.

## Build from source

Requires Python 3.10+ (the build machine needs internet to install dependencies — see the fully
offline build below).

```bash
python build.py            # creates .venv, installs deps, builds into site/
python build.py --package  # same + dist/emx-docs-offline.zip (site + serve.py)
python build.py --serve    # build and serve on http://127.0.0.1:8080
python serve.py            # serve an already built site
```

It is just three plain Zensical runs in offline mode (`OFFLINE=true zensical build`, once per language;
Russian and Chinese end up in `site/ru` and `site/zh`). No custom hooks, plugins or templates are used, and
the built site makes no requests to external hosts.

### Fully offline build

On an internet-connected machine with the same OS and Python version as the target:

```bash
pip download -r requirements.in -d wheels
```

Move the repository together with the `wheels` folder into the closed network and run:

```bash
python build.py --wheels wheels
```

### Docker

```bash
docker build -t emx-docs .
docker run -d -p 8080:80 emx-docs
```

Move the image into an air-gapped network without a registry:

```bash
docker save emx-docs | gzip > emx-docs.tar.gz      # internet-connected machine
gunzip -c emx-docs.tar.gz | docker load            # closed network
```

## Repository layout

| Path | Purpose |
|---|---|
| `docs/`, `ru/docs/`, `zh/docs/` | Markdown sources (en / ru / zh) |
| `mkdocs.yml`, `base-mkdocs.yml` (+ in `ru/`, `zh/`) | Site navigation and configuration |
| `docs/vendor/glightbox/` | Image lightbox, bundled so the theme does not fetch it from a CDN |
| `build.py`, `serve.py` | Build wrapper and optional local server |
| `requirements.in` | Python dependencies (Zensical only) |

The site is generated with [Zensical](https://zensical.org/) (MkDocs Material compatible).

## Updates

This repository is synchronized from Eremex's private repository. Do not edit files here
directly — changes will be overwritten by the next sync. New versions are published as releases (`v*` tags).

## Support

Product questions: <https://www.eremexcontrols.ru/>, Telegram: <https://t.me/emxControls>.

## License

See [LICENSE](LICENSE) ([Russian translation](LICENSE.ru.md)). You may use the documentation and host it inside your own closed network; publishing it on the public internet requires written permission from Eremex.
