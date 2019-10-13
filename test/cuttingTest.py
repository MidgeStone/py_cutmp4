#!/usr/bin/env python3
import subprocess
with open("cuts2.txt") as f:
  for line in f.readlines():
    filename, start, end, outputname,  = line.strip().split(' ')
    cmd = ["ffmpeg", "-i", filename, "-ss", start, "-to", end, "-c", "copy", outputname]
    subprocess.run(cmd, stderr=subprocess.STDOUT)
