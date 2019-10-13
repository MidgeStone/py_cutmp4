#!/usr/bin/env python3
import subprocess
start = "00:00:00"
end = "00:00:10"
cmd = ["ffmpeg", "-i", "totoro.mp4", "-ss", start, "-to", end, "-c", "copy", "totoro2.mp4"]
subprocess.run(cmd, stderr=subprocess.STDOUT)