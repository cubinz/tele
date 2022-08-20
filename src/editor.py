from moviepy.editor import *


def concat_images_in_pictures_dir_to_video():
    clips = [ImageClip(m).set_duration(3) for m in [f'./pictures/{x}' for x in os.listdir("pictures")]]
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile("output_old.mp4", fps=24)

def add_output_mp3_audio_to_output_old_mp4():
    os.system("ffmpeg -i output_old.mp4 -i output.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4")    
    #os.system("ffmpeg -y -i 'https://chunk.lab.zalo.ai/eff36db690d1798f20c0' -codec:a libmp3lame file1.mp3")
    #os.system("ffmpeg -y -i 'https://chunk.lab.zalo.ai/c3b670f18d9664c83d87' -codec:a libmp3lame file2.mp3")    
    #os.system("ffmpeg -i 'concat:file1.mp3|file2.mp3' -acodec copy meens.mp3") 
