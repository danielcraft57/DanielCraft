#!/usr/bin/env python3
"""SVG hero pour les vitrines SaaS UX."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"


def w(rel: str, body: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.strip() + "\n", encoding="utf-8")


def main() -> None:
    w(
        "saas-landing/images/hero.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0b1220"/><stop offset="100%" stop-color="#1e1b4b"/></linearGradient>
    <linearGradient id="bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#6366f1"/><stop offset="100%" stop-color="#a5b4fc"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#bg)"/>
  <g transform="translate(120 80)">
    <rect x="0" y="0" width="960" height="360" rx="16" fill="#141c2e" stroke="#334155"/>
    <rect x="40" y="280" width="80" height="180" rx="6" fill="url(#bar)"/>
    <rect x="140" y="220" width="80" height="240" rx="6" fill="url(#bar)" opacity=".85"/>
    <rect x="240" y="160" width="80" height="300" rx="6" fill="url(#bar)" opacity=".7"/>
    <rect x="340" y="200" width="80" height="260" rx="6" fill="#4ade80"/>
    <path d="M480 120 Q620 60 760 140 T920 100" fill="none" stroke="#6366f1" stroke-width="4"/>
    <circle cx="920" cy="100" r="8" fill="#4ade80"/>
  </g>
  <text x="600" y="480" text-anchor="middle" font-family="system-ui,sans-serif" font-size="16" fill="#94a3b8">FlowMetrics · funnel activation</text>
</svg>""",
    )
    w(
        "saas-onboarding/images/hero.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img">
  <rect width="800" height="520" fill="#e0f2fe"/>
  <rect x="80" y="60" width="640" height="400" rx="12" fill="#fff" stroke="#0ea5e9" stroke-width="2"/>
  <rect x="120" y="100" width="560" height="12" rx="6" fill="#e2e8f0"/>
  <rect x="120" y="100" width="280" height="12" rx="6" fill="#0ea5e9"/>
  <text x="400" y="200" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" fill="#0f172a">Offre publiée ✓</text>
  <rect x="200" y="240" width="400" height="120" rx="8" fill="#f0fdf4" stroke="#16a34a"/>
  <text x="400" y="310" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#166534">Première victoire — aha moment</text>
</svg>""",
    )
    w(
        "saas-dashboard/images/hero.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img">
  <rect width="1200" height="520" fill="#f1f5f9"/>
  <rect x="0" y="0" width="200" height="520" fill="#0f172a"/>
  <rect x="240" y="60" width="200" height="100" rx="10" fill="#fff" stroke="#e2e8f0"/>
  <rect x="460" y="60" width="200" height="100" rx="10" fill="#fff" stroke="#e2e8f0"/>
  <rect x="680" y="60" width="200" height="100" rx="10" fill="#fff" stroke="#8b5cf6" stroke-width="2"/>
  <rect x="240" y="200" width="640" height="260" rx="10" fill="#fff" stroke="#e2e8f0"/>
  <rect x="280" y="320" width="120" height="100" rx="4" fill="#8b5cf6" opacity=".3"/>
  <rect x="420" y="280" width="120" height="140" rx="4" fill="#8b5cf6" opacity=".5"/>
  <rect x="560" y="300" width="120" height="120" rx="4" fill="#8b5cf6" opacity=".4"/>
  <rect x="700" y="260" width="120" height="160" rx="4" fill="#8b5cf6"/>
</svg>""",
    )
    w(
        "saas-empty/images/hero.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" role="img">
  <rect width="800" height="400" fill="#fafafa"/>
  <circle cx="400" cy="140" r="48" fill="none" stroke="#059669" stroke-width="4"/>
  <line x1="430" y1="170" x2="460" y2="200" stroke="#059669" stroke-width="4"/>
  <rect x="120" y="240" width="560" height="48" rx="24" fill="#fff" stroke="#d4d4d4" stroke-width="2"/>
  <text x="150" y="272" font-family="system-ui,sans-serif" font-size="16" fill="#737373">rapport fiscal Q4</text>
</svg>""",
    )
    w(
        "saas-notifications/images/hero.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img">
  <rect width="800" height="520" fill="#111827"/>
  <path d="M400 120 L440 200 L520 210 L460 270 L480 350 L400 310 L320 350 L340 270 L280 210 L360 200 Z" fill="#f59e0b" opacity=".9"/>
  <circle cx="480" cy="160" r="20" fill="#ef4444"/>
  <rect x="160" y="380" width="480" height="80" rx="10" fill="#1f2937" stroke="#374151"/>
  <rect x="180" y="400" width="120" height="16" rx="4" fill="#f59e0b"/>
  <rect x="180" y="430" width="320" height="10" rx="3" fill="#4b5563"/>
</svg>""",
    )
    print("[OK] 5 hero SVG SaaS générés")


if __name__ == "__main__":
    main()
