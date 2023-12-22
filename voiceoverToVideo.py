from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

video_path = 'output/output_video.mp4'
audio_path = 'output/speech.mp3'

def add_audio_to_video(video_path, audio_path, output_dir, start_delay=0.5):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    composite_audio = CompositeAudioClip([audio_clip.set_start(start_delay)])
    final_clip = video_clip.set_audio(composite_audio)

    # Write the result to a file
    output_path = f'{output_dir}/video_with_voiceover.mp4'
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

#add_audio_to_video(video_path, audio_path, "output")
