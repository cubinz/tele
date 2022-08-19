from enum import Enum
from pytube import Playlist


class Genre(Enum):
    mass = 1
    melody = 2
    motivation = 3

def download_mp3(type: Genre, id: int):

    if type == Genre.mass:
        target_playlist = "https://www.youtube.com/playlist?list=PLTabLFF7_AUDAiDASiMxpmMOenVfJUl9Y"
    elif type == Genre.melody:
        target_playlist = "https://www.youtube.com/playlist?list=PLTabLFF7_AUDAiDASiMxpmMOenVfJUl9Y"
    elif type == Genre.motivation:
        target_playlist = "https://www.youtube.com/playlist?list=PLTabLFF7_AUDAiDASiMxpmMOenVfJUl9Y"
    else:
        target_playlist = "https://www.youtube.com/playlist?list=PLTabLFF7_AUDAiDASiMxpmMOenVfJUl9Y"

    p = Playlist(target_playlist)
    required_video = p.videos[id]
    required_video.streams.filter(only_audio=True).first().download(filename=f"output.mp3")
