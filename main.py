#!/usr/bin/env python3

import argparse
import shutil
from split_image import split_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split an image into a grid.')
    parser.add_argument('path', help='Input image file path')
    parser.add_argument('--rows', type=int, default=3, help='Number of rows (default: 3)')
    parser.add_argument('--cols', type=int, default=3, help='Number of columns (default: 3)')
    parser.add_argument('--out', default='out', help='Output directory (default: out)')
    parser.add_argument('--zip', nargs='?', const='output', help='Zip the output (default: output.zip)')

    args = parser.parse_args()

    split_image(args.path, rows=args.rows, cols=args.cols, out_dir=args.out)

    if args.zip:
        zip_name = f"{args.zip}.zip" if not args.zip.endswith('.zip') else args.zip
        shutil.make_archive(zip_name.replace('.zip', ''), 'zip', args.out)
        print(f"Zipped output to {zip_name}")
