from moviepy.editor import *


def concat_images_in_pictures_dir_to_video():
    os.system("ffmpeg -framerate 1/5 -pattern_type glob -i 'pictures/*.jpeg' -c:v libx264 -r 30 -pix_fmt yuv420p output_old.mp4")
def add_output_mp3_audio_to_output_old_mp4():   
    os.system("ffmpeg -i output_old.mp4 -i output.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4")
    os.system("ffmpeg -y -i 'https://chunk.lab.zalo.ai/eff36db690d1798f20c0' -codec:a libmp3lame meens.mp3")
