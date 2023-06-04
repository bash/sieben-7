#!/usr/bin/env python3

from defcon import Font
from ufo2ft import compileOTF, compileTTF
from subprocess import check_call

ufo = Font("Sieben-7.ufo")
compileOTF(ufo).save("Sieben-7-Regular.otf")
compileTTF(ufo).save("Sieben-7-Regular.ttf")
check_call(["woff2_compress", "Sieben-7-Regular.ttf"])
