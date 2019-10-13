#python 3.7 snippet to batch cut movies with indication into filename
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def extractSecondsFromString(filename):
    #isolate min and secs from string of the following type:
    #f = "moviesU1DMP_P5_chapter7_01_demarrermattepaint11-v001_#couper_debut_avant_2'55.mp4"
    #and return a tuple : 
    if "_#couper_debut_avant_" in filename:
        timingTrigger = "#couper_debut_avant_"
    elif "#couper_a_" in filename:
        timingTrigger = "#couper_a_"
    
    if timingTrigger:            
        cleanedFilename = "_".join(filename.replace(timingTrigger,"").split("_")[:-1])+"#"+".mp4"
        min2seconds = float(filename.split(timingTrigger)[1].split(".mp4")[0].split("'")[0])*60
        seconds = float(filename.split(timingTrigger)[1].split(".mp4")[0].split("'")[1])
            
        formatedTime = min2seconds+seconds
        #print(formatedTime)
        print(cleanedFilename)
        return (cleanedFilename, formatedTime)

processedFiles = 0
moviesFolder = r"G:\PierreMigeot_Scripting\Git\cutmp4\movies"
cutend_files = [f for f in os.listdir(moviesFolder) if f.lower().endswith(".mp4") and "#couper_a_" in f.lower()]
cutbeginning_files = [f for f in os.listdir(moviesFolder) if f.lower().endswith(".mp4") and "_#couper_debut_avant_" in f.lower()]
doCutFiles = 1

for f in cutbeginning_files:
    currentPath = moviesFolder + """/""" + f
    print(currentPath)
    clip = VideoFileClip(currentPath)
    
    newFilename , start_time = extractSecondsFromString(f)
    end_time = clip.duration
    print(newFilename)    
    print(start_time)
    print(end_time)
    
    if doCutFiles:
        ffmpeg_extract_subclip(currentPath, start_time, end_time, targetname=newFilename)
        processedFiles+=1

for f in cutend_files:
    currentPath = moviesFolder + """/""" + f
    print(currentPath)
    
    start_time = 0.00
    newFilename , end_time = extractSecondsFromString(f)
    print(newFilename)
    print(start_time)
    print(end_time)

    if doCutFiles:
        ffmpeg_extract_subclip(currentPath, start_time, end_time, targetname=newFilename)
        processedFiles+=1

#print(files)
print("done")
if processedFiles:
    print("{} mp4 file(s) have been cut.".format(processedFiles))
else:
    print("0 mp4 file(s) has been cut.")