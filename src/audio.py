from enum import Enum
from pytube import Playlist


class Genre(Enum):
    mass = 1
    melody = 2
    motivation = 3

def download_mp3(type: Genre, id: int):

    if type == Genre.mass:
        target_playlist = "https://www.youtube.com/playlist?list=PLEF3AF2D56CBF2DC2"
    elif type == Genre.melody:
        target_playlist = "https://www.youtube.com/playlist?list=PLEF3AF2D56CBF2DC2"
    elif type == Genre.motivation:
        target_playlist = "https://www.youtube.com/playlist?list=PLEF3AF2D56CBF2DC2"
    else:
        target_playlist = "https://www.youtube.com/playlist?list=PLEF3AF2D56CBF2DC2"

    p = Playlist(target_playlist)
    required_video = p.videos[id]
    required_video.streams.filter(only_audio=True).first().download(filename=f"output.mp3")
