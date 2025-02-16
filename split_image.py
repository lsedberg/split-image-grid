import os
from PIL import Image


def split_image(
    input_path,
    rows,
    cols,
    out_dir="out",
    overlap_top=0,
    overlap_bottom=0,
    overlap_left=0,
    overlap_right=0,
    background_color=(0, 0, 0, 0),
):
    # Load the image
    img = Image.open(input_path)
    img_width, img_height = img.size

    # Calculate size of each cell
    cell_width = img_width // cols
    cell_height = img_height // rows

    # Ensure output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # Extract the original name without extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    # Split the image
    for row in range(rows):
        for col in range(cols):
            left = col * cell_width - overlap_left
            upper = row * cell_height - overlap_top
            right = col * cell_width + cell_width + overlap_right
            lower = row * cell_height + cell_height + overlap_bottom

            # Create a background image with the same size as the cell
            crop_width, crop_height = (right - left, lower - upper)
            cropped = Image.new("RGBA", (crop_width, crop_height), background_color)

            # Crop only the valid portion and paste it on top of the background
            valid_crop = img.crop(
                (
                    max(0, left),
                    max(0, upper),
                    min(img_width, right),
                    min(img_height, lower),
                )
            )

            paste_x = max(0, -left)
            paste_y = max(0, -upper)

            cropped.paste(valid_crop, (paste_x, paste_y))
            out_path = os.path.join(out_dir, f"{row}_{col}_{base_name}.png")
            cropped.save(out_path)
            width, height = cropped.size
            is_overlapping = width != cell_width or height != cell_height
            print(
                f"Saved: {out_path} ({cell_width} x {cell_height}){" + overlap " if is_overlapping else " "}= ({width} x {height})"
            )
