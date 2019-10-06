
## Run the following commands in the terminal
# pip install pafy
# pip install youtube_dl

import pafy

# Lofi Playlist - https://www.youtube.com/playlist?list=PLiVsp8NMtMQQExo8Pn7Bcf-D3r9tr3-RX
pl_url = "https://www.youtube.com/playlist?list=PLiVsp8NMtMQQExo8Pn7Bcf-D3r9tr3-RX"

download_dir = "/home/darealappu/Music/PlaylistSongs3"

playlist = pafy.get_playlist(pl_url)

for song in playlist:
    bestaudio = song.getbestaudio()
    bestaudio.download(download_dir)
    print(bestaudio.title,"successfully downloaded")