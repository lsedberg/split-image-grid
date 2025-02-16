#!/usr/bin/env python3

import argparse
import shutil
from split_image import split_image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split an image into a grid. You can specify the number of rows and columns and the overlap between cells. The output will be saved in a directory."
    )
    parser.add_argument("input_path", help="Input image file path")
    parser.add_argument("output_path", help="Output directory path")
    parser.add_argument(
        "--rows", type=int, default=3, help="Number of rows (default: 3)"
    )
    parser.add_argument(
        "--cols", type=int, default=3, help="Number of columns (default: 3)"
    )
    parser.add_argument(
        "--zip", nargs="?", const="output", help="Zip the output (default: output.zip)"
    )
    parser.add_argument(
        "--overlap-t",
        type=int,
        default=0,
        help="Overlap pixels at the top (default: 0)",
    )
    parser.add_argument(
        "--overlap-b",
        type=int,
        default=0,
        help="Overlap pixels at the bottom (default: 0)",
    )
    parser.add_argument(
        "--overlap-l",
        type=int,
        default=0,
        help="Overlap pixels at the left (default: 0)",
    )
    parser.add_argument(
        "--overlap-r",
        type=int,
        default=0,
        help="Overlap pixels at the right (default: 0)",
    )
    parser.add_argument(
        "--overlap-y",
        type=int,
        default=0,
        help="Overlap pixels at the top and bottom (default: 0)",
    )
    parser.add_argument(
        "--overlap-x",
        type=int,
        default=0,
        help="Overlap pixels at the left and right (default: 0)",
    )
    parser.add_argument(
        "--background-color",
        type=lambda x: tuple(map(int, x.split(","))),
        default=(0, 0, 0, 0),
        help="Background color RGBA for when overlapping out of range. Comma separated without spaces. Default transparent. (default: 0,0,0,0)",
    )

    args = parser.parse_args()

    if args.overlap_y:
        args.overlap_t = args.overlap_b = args.overlap_y
    if args.overlap_x:
        args.overlap_l = args.overlap_r = args.overlap_x

    split_image(
        args.input_path,
        rows=args.rows,
        cols=args.cols,
        out_dir=args.output_path,
        overlap_top=args.overlap_t,
        overlap_bottom=args.overlap_b,
        overlap_left=args.overlap_l,
        overlap_right=args.overlap_r,
        background_color=args.background_color,
    )

    print(f"Output saved in {args.output_path}")
    print(f"Saved {args.rows * args.cols} images.")

    if args.zip:
        zip_name = f"{args.zip}.zip" if not args.zip.endswith(".zip") else args.zip
        shutil.make_archive(zip_name.replace(".zip", ""), "zip", args.output_path)
        print(f"Zipped output to {zip_name}")
