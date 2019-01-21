#!/usr/bin/python

# Receives as an argument, an .mp4 file and converts it into .wav
# Implemented a way to split audio file into chunks of 30 seconds

import subprocess
import sys
import os

newFile = "source/new-audio.wav"
filePath = sys.argv[1]

def convertFileToWav(filePath):
   command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(filePath, newFile)
   subprocess.call(command, shell=True)

def SplitWav():
   command = "ffmpeg -i {} -f segment -segment_time 30 -c copy parts/out%09d.wav".format(newFile)
   subprocess.call(command, shell=True)

if __name__ == '__main__':
   convertFileToWav(filePath)
   print("File converted to wav.")
   SplitWav()
   print("File split into 30s chunks.")
