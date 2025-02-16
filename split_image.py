import os
from PIL import Image

def split_image(input_path, rows, cols, out_dir='out'):
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
            left = col * cell_width
            upper = row * cell_height
            right = left + cell_width
            lower = upper + cell_height
            cropped = img.crop((left, upper, right, lower))
            out_path = os.path.join(out_dir, f"{row}_{col}_{base_name}.png")
            cropped.save(out_path)
            print(f"Saved: {out_path}")

