
## Run the following commands in the terminal
# pip install pafy
# pip install youtube_dl

import pafy
import time

video_url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

download_dir = "/home/darealappu/Music"

video = pafy.new(video_url)

#Audiofile of the Youtube Video
bestvideo = video.getbest()

#Filename is title of the Youtube video along with the extension
filename = video.title+'.'+bestvideo.extension

# Filesize in MB
# Print it upto 2 decimal places
filesize = "{0:.2f}".format(float(bestvideo.get_filesize()/(1000000)))

print("\n\nYOUTUBE VIDEO DOWNLOADER (YVD)")
print("=====================================================================\n")
print("Filename : ",filename)
print("Duration : ",video.duration)
print("Resolution : ",bestvideo.resolution)
print("Filesize : ",filesize," MB")
print("Download Directory : ",download_dir)
print("Video URL : ",video.watchv_url)
print("\nPlease do not abort the python script till the download is completed...\n")

# The Main Downloading Part
start_time = time.time()
bestvideo.download(download_dir)
end_time = time.time()

download_time = end_time - start_time;

print(filename,"successfully Downloaded.")
print("Download Time : ",str(int(download_time))," seconds")
print("\n=====================================================================\n")