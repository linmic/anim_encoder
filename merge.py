#!/usr/bin/python
# coding: utf-8

"""
./merge.py loop 43 107 loop
"""

import sys
from PIL import Image

path = sys.argv[1]
idx_from = int(sys.argv[2])
idx_to = int(sys.argv[3])
filename = sys.argv[4]

if not len(sys.argv) == 5:
    print sys.argv
    print 'invalid args'
    sys.exit(0)

images_range = range(idx_from, idx_to + 1)
el_width = el_height = 160

new_im_width = el_width*(len(images_range)-1)
new_im = Image.new('RGBA', (new_im_width, el_height))

"""
0 - 43
43 - 107
227 - 259
"""

for i, n in enumerate(images_range):
    try:
        im = Image.open("%s/%d.png" % (path, n))
        new_im.paste(im, (el_width*i, 0))
    except:
        pass

new_im.save("./%s.png" % filename, 'png')
