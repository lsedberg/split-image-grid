import argparse
from split_image import split_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split an image into a grid.')
    parser.add_argument('path', help='Input image file path')
    parser.add_argument('--rows', type=int, default=3, help='Number of rows (default: 3)')
    parser.add_argument('--cols', type=int, default=3, help='Number of columns (default: 3)')
    parser.add_argument('--out', default='out', help='Output directory (default: out)')
    args = parser.parse_args()

    split_image(args.path, rows=args.rows, cols=args.cols, out_dir=args.out)