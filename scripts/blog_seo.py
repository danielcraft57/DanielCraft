"""SEO blog — fil d'Ariane visible et helpers microdata inline."""
from __future__ import annotations

from html import escape

SCHEMA = "https://schema.org"
AUTHOR_NAME = "Loïc DANIEL"
PUBLISHER_NAME = "DanielCraft"


def esc(value: object) -> str:
    return escape(str(value), quote=True)


def block_breadcrumbs(crumbs: list[tuple[str, str]]) -> str:
    """Fil d'Ariane visible + microdata BreadcrumbList.

    Chaque entrée est (label, url). URL vide = page courante.
    """
    if len(crumbs) <= 1:
        return ""
    items: list[str] = []
    for i, (label, href) in enumerate(crumbs, 1):
        if i == len(crumbs) or not href:
            items.append(
                f"""      <li class="blog-breadcrumb-item is-current" aria-current="page" itemprop="itemListElement" itemscope itemtype="{SCHEMA}/ListItem">
        <meta itemprop="position" content="{i}">
        <span itemprop="name">{esc(label)}</span>
      </li>"""
            )
        else:
            items.append(
                f"""      <li class="blog-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="{SCHEMA}/ListItem">
        <meta itemprop="position" content="{i}">
        <a itemprop="item" href="{esc(href)}"><span itemprop="name">{esc(label)}</span></a>
      </li>"""
            )
    return f"""<nav class="blog-breadcrumb" aria-label="Fil d'Ariane" itemscope itemtype="{SCHEMA}/BreadcrumbList">
  <ol class="blog-breadcrumb-list">
{chr(10).join(items)}
  </ol>
</nav>"""


def crumbs_blog_index(site_base: str) -> list[tuple[str, str]]:
    return [("Accueil", f"{site_base.rstrip('/')}/"), ("Blog", "")]


def crumbs_article(
    site_base: str,
    title: str,
    *,
    series_title: str = "",
    series_url: str = "",
) -> list[tuple[str, str]]:
    base = site_base.rstrip("/")
    crumbs: list[tuple[str, str]] = [
        ("Accueil", f"{base}/"),
        ("Blog", f"{base}/blog/"),
    ]
    if series_title and series_url:
        crumbs.append((series_title, series_url))
    crumbs.append((title, ""))
    return crumbs


def crumbs_collection(site_base: str, title: str) -> list[tuple[str, str]]:
    base = site_base.rstrip("/")
    return [
        ("Accueil", f"{base}/"),
        ("Blog", f"{base}/blog/"),
        (title, ""),
    ]
