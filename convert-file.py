#!/usr/bin/python

# Receives as an argument, an .mp4 file and converts it into .wav.
# Faster to make it speech into text later on.

import subprocess
import sys

filePath = sys.argv[1]

def convertFile(filePath):
   command = "ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn new-audio.wav" % filePath
   print(command)
   subprocess.call(command, shell=True)

convertFile(filePath)
print("File converted to wav.")