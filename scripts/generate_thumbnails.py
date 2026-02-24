#!/usr/bin/env python3
"""
Generate optimized thumbnails for 3D render images.
Processes all full-size renders and creates 400px-wide thumbnails.
"""

from PIL import Image
import os
from pathlib import Path

def generate_thumbnails():
    # Directories
    renders_dir = Path("public/images/renders")
    thumbs_dir = renders_dir / "thumbs"

    # Create thumbs directory if it doesn't exist
    thumbs_dir.mkdir(parents=True, exist_ok=True)

    # Process all scene-*.webp files
    render_files = sorted(renders_dir.glob("scene-*.webp"))

    print(f"Found {len(render_files)} render files to process")

    for render_file in render_files:
        try:
            # Open original image
            with Image.open(render_file) as img:
                # Calculate thumbnail size (400px width, maintain aspect ratio)
                original_width, original_height = img.size
                thumbnail_width = 400
                thumbnail_height = int(original_height * (thumbnail_width / original_width))

                # Create thumbnail using high-quality Lanczos resampling
                img_thumb = img.resize((thumbnail_width, thumbnail_height), Image.Resampling.LANCZOS)

                # Save as WebP with quality 80
                thumb_path = thumbs_dir / render_file.name
                img_thumb.save(thumb_path, 'WEBP', quality=80, method=6)

                # Get file sizes for reporting
                original_size = render_file.stat().st_size / 1024  # KB
                thumb_size = thumb_path.stat().st_size / 1024  # KB

                print(f"[OK] {render_file.name}: {original_size:.1f}KB -> {thumb_size:.1f}KB thumbnail")

        except Exception as e:
            print(f"[ERROR] Error processing {render_file.name}: {e}")

    print(f"\nThumbnail generation complete!")
    print(f"Thumbnails saved to: {thumbs_dir}")

if __name__ == "__main__":
    generate_thumbnails()
