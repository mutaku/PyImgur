#!/usr/bin/env python

import sys
import webbrowser
from pyimgur import UploadImage as U

try:
    fn = sys.argv[1]
    result = U(fn)
    if not result.error:
        url = result.imageURL['url']
        webbrowser.open(url)
    else:
        print result.error
except:
    sys.exit()
