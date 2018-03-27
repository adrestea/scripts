#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
img = Image.open('/work/.Trash-1000/files/Blaze.9/hdk/htc/lib1/HtcCommonControl/src/androidTest/res/drawable/htcgridview_sample_0.jpg')
exif_data = img.getexif()
