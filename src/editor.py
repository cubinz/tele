from moviepy.editor import *


def concat_images_in_pictures_dir_to_video():
    clips = [ImageClip(m).set_duration(3) for m in [f'./pictures/{x}' for x in os.listdir("pictures")]]
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile("input1.mp4", fps=30)
    clips = [ImageClip(m).set_duration(3) for m in [f'./pictures/{x+1}' for x in os.listdir("pictures")]]
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile("input2.mp4", fps=30)

def add_output_mp3_audio_to_output_old_mp4():    
    os.system('ffmpeg -i "concat:input1.mp4|input2.mp4" -c copy output_old.mp4')    
    os.system("ffmpeg -i output_old.mp4 -i output.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4")
    
    
