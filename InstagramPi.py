#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# InstagramPi Gafas for Instagram with Raspberry Pi Zero
#
# Autor: Andrés Sabas @ Feb 2017
#
#
# Use text editor to edit the script and type in valid Instagram username/password
import atexit
import picamera
import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

saveIdx         = -1      # Image index for saving (-1 = none set yet)

# Init camera and set up default values
camera            = picamera.PiCamera()
atexit.register(camera.close)
#camera.resolution = sizeData[sizeMode][1]
#camera.crop       = sizeData[sizeMode][2]
camera.crop       = (0.0, 0.0, 1.0, 1.0)

PhotoPath = "/home/pi/images" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "Xhabas" # Change to your Instagram USERNAME
PASSWD    = "IGPassword" # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Hi from Raspberry Pi #PInstagram"

os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print ("Total Photo in this folder:" + str (len(ListFiles)))

#Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() # login

while True:
			filename = PhotoPath + '/IMG_' + '%04d' % saveIdx + '.JPG'
			if not os.path.isfile(filename): break
			saveIdx += 1
			if saveIdx > 9999: saveIdx = 0

camera.capture(filename, splitter_port=1, use_video_port=True, format='jpeg',
		thumbnail=None)

for i in range(len(ListFiles)):
    photo = ListFiles[i]
    print ("Progress :" + str([i+1]) + " of " + str(len(ListFiles)))
    print ("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo,caption=IGCaption,upload_id=None)
    # sleep for random between 600 - 1200s
    n = randint(600,1200)
    print ("Sleep upload for seconds: " + str(n))
    time.sleep(n)
