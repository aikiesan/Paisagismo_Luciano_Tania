#!/bin/bash
# Copy and rename 43 new render scenes from Images_webp/webp_output/

set -e  # Exit on error

SOURCE_DIR="Images_webp/webp_output"
DEST_DIR="public/images/renders"

echo "=== Copying New Render Scenes ==="

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Remove old render files
echo "Removing old render files..."
rm -f "$DEST_DIR"/scene-*.webp

echo "Copying new render files..."

# Copy scenes 1-40 (use _1 suffix pattern)
for i in {1..40}; do
    # Zero-pad the scene number
    scene_num=$(printf "%02d" $i)

    source_file="$SOURCE_DIR/PREVIAS_2026Scene ${i}_1.webp"
    dest_file="$DEST_DIR/scene-${scene_num}.webp"

    if [ -f "$source_file" ]; then
        cp "$source_file" "$dest_file"
        size=$(du -h "$dest_file" | cut -f1)
        echo "✓ Copied scene-${scene_num}.webp ($size)"
    else
        echo "✗ Warning: Source file not found: $source_file"
    fi
done

# Copy scenes 41-43 (use _2 suffix pattern)
for i in {41..43}; do
    # Zero-pad the scene number
    scene_num=$(printf "%02d" $i)

    source_file="$SOURCE_DIR/PREVIAS_2026Scene ${i}_2.webp"
    dest_file="$DEST_DIR/scene-${scene_num}.webp"

    if [ -f "$source_file" ]; then
        cp "$source_file" "$dest_file"
        size=$(du -h "$dest_file" | cut -f1)
        echo "✓ Copied scene-${scene_num}.webp ($size)"
    else
        echo "✗ Warning: Source file not found: $source_file"
    fi
done

# Count copied files
file_count=$(ls -1 "$DEST_DIR"/scene-*.webp 2>/dev/null | wc -l)
echo ""
echo "=== Copy Complete ==="
echo "Total files copied: $file_count"
echo "Destination: $DEST_DIR"
