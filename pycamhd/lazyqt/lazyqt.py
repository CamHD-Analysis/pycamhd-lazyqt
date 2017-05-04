#!/usr/bin/env python

import pylazyqt

import numpy as np
from PIL import Image

ENCODING = 'utf-8'

def get_metadata( url ):
    burl = url.encode(ENCODING)
    return pylazyqt.movie_info( burl )


## Retrieve the frame'th frame from the mirror site at url
def get_frame( url, frame_num, format = 'np' ):
    burl = url.encode(ENCODING)
    img = pylazyqt.get_frame( burl, frame_num )

    ## TODO:: Validation here
    if format == 'np':
        return img
    elif format == 'image':
        return Image.fromarray( img )
    else:
        print("Don't understand format type \"%s\"" % format)
        return
