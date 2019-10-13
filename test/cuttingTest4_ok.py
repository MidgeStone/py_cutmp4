from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

start_time = 0.00
end_time = 110.68
ffmpeg_extract_subclip("a.mp4", start_time, end_time, targetname="test_alt.mp4")

clip = VideoFileClip("G:/PierreMigeot_Scripting/Git/cutmp4/b.mp4")

start_time = 110.98
end_time = clip.duration
print(clip.duration)

ffmpeg_extract_subclip("b.mp4", start_time, end_time, targetname="test_altb.mp4")