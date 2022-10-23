from time import sleep
from sys import exit
from warnings import catch_warnings
from pytube import YouTube, Channel
# from pytube import Stream
import os

#accept video url from user
print("-- Youtube video downloader --\n")
video_url = input("Enter url: ")

yt = YouTube(video_url)
ch = Channel(yt.channel_url)

#accept .mp4 or .mp3 file formats
file_format = int(input("Available:\n(1) mp4\n(2) mp3\nChoose your file format: "))
if file_format == 1:
    file_format = ".mp4"
elif file_format == 2:
    file_format = ".mp3"
else:
    print("Invalid input..")
    exit(-1)
    

#accept file name
download_name = input("Save the file\nName: ")
os.system("cls")



#get information of video
print(f"Video: {yt.title}\nChannel: {ch.channel_name}\nFile format: {file_format}\n")

sleep(2)
print("Downloading...\n")
#download the video
# yt.streams.filter(type="video", subtype="mp4", progressive=True).get_highest_resolution().download(filename=download_name)


#------------------ FIX MP3 DOWNLOAD------------

if file_format == ".mp4":
    yt.streams.filter(mime_type="video/mp4", progressive=True).get_highest_resolution().download(filename=download_name+file_format, max_retries=10)
elif file_format == ".mp3":
    yt.streams.filter(mime_type="audio/mp3").get_audio_only().download(filename=download_name+file_format, max_retries=10)
    
print("Successful!")