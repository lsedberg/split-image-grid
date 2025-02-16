# Split image grid

Splits an image into a grid.
Outputs each cell as a separate `.png` image.
Useful for extracting images from a collage.
 
Run `python3 main.py --help` for more.

```bash
$ python3 main.py --help
usage: main.py [-h] [--rows ROWS] [--cols COLS] [--out OUT] [--zip [ZIP]] path

Split an image into a grid.

positional arguments:
  path         Input image file path

options:
  -h, --help   show this help message and exit
  --rows ROWS  Number of rows (default: 3)
  --cols COLS  Number of columns (default: 3)
  --out OUT    Output directory (default: out)
  --zip [ZIP]  Zip the output (default: output.zip)
```