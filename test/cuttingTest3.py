#!/usr/bin/env python3
import subprocess
start = "-00:00:01"
end = "00:01:50"
cmd = ["ffmpeg", "-i", "a.mp4", "-ss", start, "-to", end, "-c", "copy", "a2.mp4"]
subprocess.run(cmd, stderr=subprocess.STDOUT)