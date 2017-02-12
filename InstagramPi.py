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
import atexit
import RPi.GPIO as GPIO
from InstagramAPI import InstagramAPI

buttonOption = 17 # Broadcom pin 17 (P1 pin 11)
buttonTake = 27 # Broadcom pin 17 (P1 pin 11)
ledPin = 16 # Broadcom pin 17 (P1 pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonOption, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonTake, GPIO.IN, pull_up_down=GPIO.PUD_UP)

saveIdx         = -1      # Image index for saving (-1 = none set yet)
Option          = True

# Init camera and set up default values
camera           = picamera.PiCamera()
atexit.register(camera.close)
#camera.resolution = sizeData[sizeMode][1]
#camera.crop       = sizeData[sizeMode][2]
#camera.crop       = (0.0, 0.0, 1.0, 1.0)

PhotoPath = "/home/pi/images" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "xhabas" # Change to your Instagram USERNAME
PASSWD    = "" # Change to your Instagram Password

# Change to your Photo Hashtag
IGCaption = "Hi from Raspberry Pi #PInstagram"

# Change to your Video Hashtag
IGCaptionVideo = "Hi from Raspberry Pi #PInstagram"

def TakeVideo():
    os.chdir(PhotoPath)
    bashCommand = "rm -rf video.h264 video.avi photothumbnail.JPG"
    os.system(bashCommand)
    print ("Record Video")
    camera.capture("photothumbnail.JPG", format='jpeg',thumbnail=None)
    camera.start_recording('video.h264' )
    time.sleep(5)
    camera.stop_recording()
    bashCommand = "ffmpeg -f h264 -i video.h264 -c libx264 -an video.avi -y"
    os.system(bashCommand)
    print ("Now Uploading this Video to instagram")
    igapi.uploadVideo("video.avi", thumbnail="photothumbnail.JPG", caption=IGCaptionVideo);
    print ("Progress : Done")
    n = randint(600,1200)
    print ("Sleep upload for seconds: " + str(n))
    time.sleep(n)

def TakePhoto():
    global saveIdx

    print ("Take Photo")
    os.chdir(PhotoPath)
    ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
    print ("Total Photo in this folder:" + str (len(ListFiles)))

    while True:
			filename = PhotoPath + '/IMG_' + '%04d' % saveIdx + '.JPG'
			if not os.path.isfile(filename): break
			saveIdx += 1
			if saveIdx > 9999: saveIdx = 0

    camera.capture(filename, format='jpeg',thumbnail=None)
    for i in range(len(ListFiles)):
        photo = ListFiles[i]
        print ("Progress :" + str([i+1]) + " of " + str(len(ListFiles)))
        print ("Now Uploading this photo to instagram: " + photo)
        igapi.uploadPhoto(photo,caption=IGCaption,upload_id=None)
        # sleep for random between 600 - 1200s
        n = randint(600,1200)
        print ("Sleep upload for seconds: " + str(n))
        time.sleep(n)

#Start Login and Uploading Photo
print(PASSWD)
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() # login

try:
    while 1:
            if GPIO.input(butTake): # button is released
                if Option:
                    TakeVideo()
                else:
                    TakePhoto()
            if GPIO.input(butOp):
                Option=True;
            else:
                Option=False;


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
