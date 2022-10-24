from time import sleep
from sys import exit
from pytube import YouTube, Channel
import os

#accept video url from user
while True:
    print("-- Youtube video downloader --\n")
    video_url = input("Enter url: ").strip()
    if video_url.find("https://") == -1:
        print("Invalid input")
        sleep(2)
        os.system("cls")
    else:
        break
while True:
    try:
        yt = YouTube(video_url)
        ch = Channel(yt.channel_url)
    except:
        print("Connection error occurred while trying to get information of the video\nTrying again...")
        sleep(2)
    else:
        os.system("cls")
        break


#accept .mp4 or .mp3 file formats
while True:
    file_format = int(input("Available:\n(1) mp4\n(2) mp3\nChoose your file format: ").strip())
    if file_format == 1 or file_format == ".mp4" or file_format == "mp4":
        file_format = ".mp4"
        break
    elif file_format == 2 or file_format == ".mp3" or file_format == "mp3":
        file_format = ".mp3"
        break
    else:
        os.system("cls")
        print("Invalid input..")
    
#accept file name
download_name = input("Save the file\nName: ")

#get information of video
def getVideoInfo():
    os.system("cls")
    print(f"Video: {yt.title}\nChannel: {ch.channel_name}\nFile format: {file_format}\n")
    sleep(2)
    print("Downloading...\n")

getVideoInfo()

retries = 5
for i in range(5):
    try:
        if file_format == ".mp4":
            yt.streams.filter(mime_type="video/mp4", progressive=True).get_highest_resolution().download(filename=download_name+file_format, max_retries=10)
        elif file_format == ".mp3":
            yt.streams.get_audio_only().download(filename=download_name+file_format, max_retries=10)
    except:
        print(f"Something went wrong! Retries left {retries}")
        retries -= 1
        sleep(3)
        getVideoInfo()
    else:
        print("Successful!")
        sleep(5)
        break