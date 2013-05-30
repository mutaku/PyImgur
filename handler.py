#!/usr/bin/env python

import sys
import webbrowser
from pyimgur import UploadImage as U
from subprocess import Popen, PIPE

try:
    fn = sys.argv[1]
    result = U(fn)
    if not result.error:
        url = result.imageURL['url']
        webbrowser.open(url)
	clip = Popen(['xsel', '-ib'], stdin=PIPE)
	clip.communicate(input=url)
    else:
        print result.error
except:
    sys.exit()
