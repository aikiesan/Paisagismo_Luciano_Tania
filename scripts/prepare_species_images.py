#!/usr/bin/env python3
"""
Prepare species images for Parthenocissus tricuspidata (Hera-falsa).
Copies the source image and generates an optimized thumbnail.
"""

from PIL import Image
import shutil
from pathlib import Path

def prepare_species_images():
    # Source image
    source_image = Path("especies_de_plantas/parthenocissus_tricuspidata_hera_falsa_vinha.webp")

    # Destination paths
    species_dir = Path("public/images/species")
    thumbs_dir = species_dir / "thumbs"

    # Create directories if they don't exist
    species_dir.mkdir(parents=True, exist_ok=True)
    thumbs_dir.mkdir(parents=True, exist_ok=True)

    # Destination files
    full_size_dest = species_dir / "hera-falsa.webp"
    thumbnail_dest = thumbs_dir / "hera-falsa.webp"

    if not source_image.exists():
        print(f"[ERROR] Source image not found: {source_image}")
        return

    try:
        # Copy full-size image
        shutil.copy2(source_image, full_size_dest)
        source_size = source_image.stat().st_size / 1024  # KB
        print(f"[OK] Copied full-size image: {full_size_dest} ({source_size:.1f}KB)")

        # Generate thumbnail
        with Image.open(source_image) as img:
            # Calculate thumbnail size (400px width, maintain aspect ratio)
            original_width, original_height = img.size
            thumbnail_width = 400
            thumbnail_height = int(original_height * (thumbnail_width / original_width))

            # Create thumbnail using high-quality Lanczos resampling
            img_thumb = img.resize((thumbnail_width, thumbnail_height), Image.Resampling.LANCZOS)

            # Save as WebP with quality 85 (higher quality for species showcase)
            img_thumb.save(thumbnail_dest, 'WEBP', quality=85, method=6)

            thumb_size = thumbnail_dest.stat().st_size / 1024  # KB
            print(f"[OK] Generated thumbnail: {thumbnail_dest} ({thumb_size:.1f}KB)")

        print("\nSpecies image preparation complete!")
        print(f"Full-size: {full_size_dest}")
        print(f"Thumbnail: {thumbnail_dest}")

    except Exception as e:
        print(f"[ERROR] Error processing species image: {e}")

if __name__ == "__main__":
    prepare_species_images()
