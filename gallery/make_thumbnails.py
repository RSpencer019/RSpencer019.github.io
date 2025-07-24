"""
- recursively iterate through image files in ./images/**/*.ext
- create thumbnails of size MAX_SIZE x MAX_SIZE
  - maintain aspect ratio
  - fill the thumbnail with the image (cover)
  - crop to center
- save them in ./images/**/*.thumbnail.ext
"""

import os
from pathlib import Path
from PIL import Image


MAX_SIZE = 200
DIR = Path(__file__).resolve().parent / 'images'


def create_thumbnail(
    image_path: Path,
):
    image = Image.open(image_path)
    print(f"Creating thumbnail for '{image_path}' ({image.size})")

    # Crop
    width, height = image.size
    if width > height:
        left = (width - height) / 2
        right = (width + height) / 2
        top = 0
        bottom = height
    else:
        left = 0
        right = width
        top = (height - width) / 2
        bottom = (height + width) / 2
    image = image.crop((left, top, right, bottom))

    # Resize
    image.thumbnail((MAX_SIZE, MAX_SIZE))

    # Save
    thumbnail_path = image_path.with_suffix('.thumbnail' + image_path.suffix)
    image.save(thumbnail_path)


def main():
    for root, _, files in os.walk(DIR):
        for file in files:
            if 'thumbnail' in file:
                continue
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
                create_thumbnail(Path(root) / file)


if __name__ == '__main__':
    main()
