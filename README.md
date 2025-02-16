# Split image grid

Splits an image into a grid of images.
Outputs each 'cell' as a separate `.png` image.
Useful for extracting images from a collage.

You can specify overlap to make them overlap to neighboring cells, if it extends beyond the OG image's dimensions, it will default to the specified background color (default transparent).
 
Run `python3 main.py --help` for more.

```ps
$ python3 main.py --help
usage: main.py [-h] [--rows ROWS] [--cols COLS] [--zip [ZIP]]
               [--overlap-t OVERLAP_T] [--overlap-b OVERLAP_B]
               [--overlap-l OVERLAP_L] [--overlap-r OVERLAP_R]
               [--overlap-y OVERLAP_Y] [--overlap-x OVERLAP_X]
               [--background-color BACKGROUND_COLOR]
               input_path output_path

Split an image into a grid. You can specify the number of rows and columns and
the overlap between cells. The output will be saved in a directory.

positional arguments:
  input_path            Input image file path
  output_path           Output directory path

options:
  -h, --help            show this help message and exit
  --rows ROWS           Number of rows (default: 3)
  --cols COLS           Number of columns (default: 3)
  --zip [ZIP]           Zip the output (default: output.zip)
  --overlap-t OVERLAP_T
                        Overlap pixels at the top (default: 0)
  --overlap-b OVERLAP_B
                        Overlap pixels at the bottom (default: 0)
  --overlap-l OVERLAP_L
                        Overlap pixels at the left (default: 0)
  --overlap-r OVERLAP_R
                        Overlap pixels at the right (default: 0)
  --overlap-y OVERLAP_Y
                        Overlap pixels at the top and bottom (default: 0)
  --overlap-x OVERLAP_X
                        Overlap pixels at the left and right (default: 0)
  --background-color BACKGROUND_COLOR
                        Background color RGBA for when overlapping out of
                        range. Comma separated without spaces. Default
                        transparent. (default: 0,0,0,0)

```