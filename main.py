from display import *
from draw import *
import random

s = new_screen()
r = 255
g = 0
b = 255

c = [ r, g, b ]

x0 = 0
y0 = 0
x1 = 499
y1 = 499

for i in range(500):
    draw_line(x0, y0, x1, y1, s, c)
    x0 = (x0 + 1) % 500
    y0 = (y0 + 2) % 500
    x1 = (x1 - 3) % 500
    y1 = (y1 - 3) % 500

    r = (r - 1) % 256
    g = (g + 3) % 256
    b = (b - 3) % 256
    c[RED] = r
    c[BLUE] = b
    c[GREEN] = g







'''
DW's code:
#octants 1 and 5
draw_line(0, 0, 499, 499, s, c)
draw_line(0, 0, 499, 250, s, c)
draw_line(499, 499, 0, 250, s, c)

#octants 8 and 4
c[BLUE] = 255;
draw_line(0, 499, 499, 0, s, c);
draw_line(0, 499, 499, 250, s, c);
draw_line(499, 0, 0, 250, s, c);

#octants 2 and 6
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, 250, 499, s, c);
draw_line(499, 499, 250, 0, s, c);

#octants 7 and 3
c[BLUE] = 255;
draw_line(0, 499, 250, 0, s, c);
draw_line(499, 0, 250, 499, s, c);
#horizontal and vertical

c[BLUE] = 0;
c[GREEN] = 255;
draw_line(0, 250, 499, 250, s, c);
draw_line(250, 0, 250, 499, s, c);
'''


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
