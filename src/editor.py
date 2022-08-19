from moviepy.editor import *


def concat_images_in_pictures_dir_to_video():
    clips = [ImageClip(f'./pictures/1.jpeg').set_duration(3)]
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile("input1.mp4", fps=30)
    clips = [ImageClip(f'./pictures/1.jpeg').set_duration(3)]
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile("input2.mp4", fps=30)

def add_output_mp3_audio_to_output_old_mp4():   
    os.system('ffmpeg -i input1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate1.ts')
    os.system('ffmpeg -i input2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate2.ts')
    os.system('ffmpeg -i "concat:intermediate1.ts|intermediate2.ts" -c copy -bsf:a aac_adtstoasc output_old.mp4')
    os.system("ffmpeg -i output_old.mp4 -i output.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4")
