
## Run the following commands in the terminal
# pip install pafy
# pip install youtube_dl

import pafy
import time

video_url = "https://www.youtube.com/watch?v=Hn4sfC2PbhI"

download_dir = "/home/darealappu/Music"

video = pafy.new(video_url)

#Audiofile of the Youtube Video
bestaudio = video.getbestaudio()

#Filename is title of the Youtube video along with the extension
filename = video.title+'.'+bestaudio.extension

# Filesize in MB
# Print it upto 2 decimal places
filesize = "{0:.2f}".format(float(bestaudio.get_filesize()/(1000000)))

print("\n\nYOUTUBE AUDIO EXTRACTOR (YAE)")
print("=====================================================================\n")
print("Filename : ",filename)
print("Duration : ",video.duration)
print("Bitrate : ",bestaudio.bitrate)
print("Filesize : ",filesize," MB")
print("Download Directory : ",download_dir)
print("Video URL : ",video.watchv_url)
print("\nPlease do not abort the python script till the download is completed...\n")

# The Main Downloading Part
start_time = time.time()
bestaudio.download(download_dir)
end_time = time.time()
download_time = end_time - start_time;

print(filename,"successfully Downloaded.")
print("Download Time : ",str(int(download_time))," seconds")
print("\n=====================================================================\n")