import whisper_timestamped
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

def add_subtitles_to_video(working_directory, 
            video_file_name, output_video_file_name, 
            commentary_file_name, 
            subtitle_file_name):

    def format_timestamp(seconds):
        """Convert seconds to the SRT time format (hours:minutes:seconds,milliseconds)."""
        millisec = int((seconds % 1) * 1000)
        seconds = int(seconds)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02},{millisec:03}"
    
    def get_subtitle_properties(txt):
        """Function to style the text for subtitles."""
        return TextClip(txt, font='Impact', fontsize=104, color='white', stroke_color='black', stroke_width=3)

    # Load the model
    model = whisper_timestamped.load_model("base")

    # Transcribe the audio
    result = whisper_timestamped.transcribe(model, f"{working_directory}/{commentary_file_name}")

    commentary_file = f"{working_directory}/{subtitle_file_name}"
    with open(commentary_file, 'w+') as srt_file:
        for segment in result["segments"]:
            for i, word in enumerate(segment["words"], start=1):
                start_time = format_timestamp(word["start"])
                end_time = format_timestamp(word["end"])
                text = word["text"]

                srt_file.write(f"{i}\n{start_time} --> {end_time}\n{text}\n\n")

    # Load your video
    video_clip = VideoFileClip(f"{working_directory}/{video_file_name}")

    # Create a subtitle clip
    subtitle = SubtitlesClip(commentary_file, get_subtitle_properties)

    # Calculate vertical position: 1/3rd from the bottom of the video
    video_height = video_clip.size[1]  # Get the height of the video
    subtitle_vertical_pos = video_height * (2 / 3)  # Position at 1/3rd from the bottom

    # Composite video with subtitles
    final = CompositeVideoClip([video_clip, subtitle.set_pos(('center',subtitle_vertical_pos))])

    # Write the result to a file
    final.write_videofile(f"{working_directory}/{output_video_file_name}", codec="libx264")
