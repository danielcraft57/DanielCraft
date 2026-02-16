#!/usr/bin/env python3
"""
Script d'optimisation des images du site DanielCraft.

Objectifs :
- Réduire le poids des images (surtout les JPEG)
- Recadrer légèrement en centre quand il faut respecter un ratio précis
- Garder une architecture simple par dossiers (og, hero, projects)

Usage (depuis la racine du projet DanielCraftFr) :
    python scripts/optimize_images.py

Pré-requis :
    pip install pillow
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional, Tuple

try:
    from PIL import Image
except ImportError:
    print(
        "[ERREUR] La librairie Pillow n'est pas installée.\n"
        "Installe-la avec : pip install pillow"
    )
    sys.exit(1)


BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets" / "images"


def center_crop_to_ratio(
    img: Image.Image, target_ratio: float
) -> Image.Image:
    """
    Recadre l'image au centre pour respecter un ratio largeur/hauteur donné.

    :param img: instance PIL.Image à recadrer
    :param target_ratio: ratio cible (ex: 1200/630 pour les images OG)
    :returns: nouvelle image recadrée au centre
    """
    width, height = img.size
    current_ratio = width / height if height else 1.0

    # Si l'image est plus large que le ratio cible, on coupe en largeur
    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        right = left + new_width
        top = 0
        bottom = height
    else:
        # Sinon on coupe en hauteur
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        bottom = top + new_height
        left = 0
        right = width

    return img.crop((left, top, right, bottom))


def optimize_image(
    img_path: Path,
    *,
    target_ratio: Optional[float] = None,
    exact_size: Optional[Tuple[int, int]] = None,
    max_size: Optional[Tuple[int, int]] = None,
    quality: int = 85,
) -> None:
    """
    Optimise une image individuelle.

    - Optionnel : recadrage au centre selon un ratio précis
    - Optionnel : redimensionnement à une taille exacte ou taille max
    - Compression avec qualité ajustable

    :param img_path: chemin du fichier image à optimiser
    :param target_ratio: ratio largeur/hauteur si recadrage nécessaire
    :param exact_size: taille finale exacte (largeur, hauteur) si imposée
    :param max_size: taille max (largeur, hauteur) pour un simple resize
    :param quality: qualité JPEG (0-100)
    :returns: None, l'image est modifiée sur place
    """
    print(f"[INFO] Optimisation de {img_path}")

    with Image.open(img_path) as img:
        img = img.convert("RGB")

        # Recadrage au ratio demandé (si besoin)
        if target_ratio is not None:
            img = center_crop_to_ratio(img, target_ratio)

        # Redimensionnement
        if exact_size is not None:
            img = img.resize(exact_size, Image.LANCZOS)
        elif max_size is not None:
            max_w, max_h = max_size
            width, height = img.size
            scale = min(max_w / width, max_h / height, 1.0)
            if scale < 1.0:
                new_size = (int(width * scale), int(height * scale))
                img = img.resize(new_size, Image.LANCZOS)

        # Sauvegarde optimisée
        suffix = img_path.suffix.lower()

        if suffix in {".jpg", ".jpeg"}:
            img.save(
                img_path,
                format="JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
            )
        elif suffix == ".png":
            img.save(
                img_path,
                format="PNG",
                optimize=True,
            )
        else:
            # Autres formats : on touche le moins possible
            img.save(img_path)


def process_folder_og() -> None:
    """
    Optimise les images Open Graph (ratio 1200x630).

    - Recadrage centré au ratio 1200/630
    - Redimensionnement exact 1200x630
    - Qualité JPEG à 82 pour un bon compromis poids/qualité
    """
    og_dir = ASSETS_DIR / "og"
    if not og_dir.exists():
        return

    ratio_og = 1200 / 630
    for img_path in og_dir.iterdir():
        if img_path.is_file() and img_path.suffix.lower() in {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
        }:
            optimize_image(
                img_path,
                target_ratio=ratio_og,
                exact_size=(1200, 630),
                quality=82,
            )


def process_folder_generic(subfolder: str, max_size: Tuple[int, int]) -> None:
    """
    Optimise les images d'un sous-dossier générique (hero, projects, etc.).

    - Pas de ratio imposé, mais resize si trop grand
    - Compression JPEG/PNG

    :param subfolder: nom du sous-dossier dans assets/images
    :param max_size: taille maximale (largeur, hauteur)
    """
    folder = ASSETS_DIR / subfolder
    if not folder.exists():
        return

    for img_path in folder.iterdir():
        if img_path.is_file() and img_path.suffix.lower() in {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
        }:
            optimize_image(
                img_path,
                max_size=max_size,
                quality=82,
            )


def main() -> None:
    """
    Point d'entrée principal du script.

    - Optimise les images OG (recadrage + resize 1200x630)
    - Optimise les images hero (par défaut max 1600x900)
    - Optimise les images projects (par défaut max 1600x900)
    """
    print("[START] Optimisation des images DanielCraft")
    print(f"[INFO] Base assets : {ASSETS_DIR}")

    process_folder_og()
    process_folder_generic("hero", max_size=(1600, 900))
    process_folder_generic("projects", max_size=(1600, 900))

    print("[DONE] Optimisation terminée.")


if __name__ == "__main__":
    main()

