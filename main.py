import os, math
from common import get_openai_client
from ideaGenerator import generate_ideas
from imageCreator import generate_image
from videoGenerator import generate_video_from_image
from subtitleManager import add_subtitles_to_video
from voiceGenerator import generate_commentary_audio
from voiceoverToVideo import add_audio_to_video
from moviepy.editor import AudioFileClip

# todo make video, commentary etc names parameters not hardcoded into smaller files
# todo delay for audio and subtitles, about 0.2, 0.3
# TODO text file into folder with title, description? and tags

def clean_everything_but_final_video(working_directory, file_to_keep="final_video.mp4"):
    for file in os.listdir(working_directory):
        if file != file_to_keep:
            file_path = os.path.join(working_directory, file)
            os.remove(file_path)

count = 5
client = get_openai_client()
video_frame_rate = 25 # frames per second

# generate prompts
generate_ideas(client, count)

with open('output/list_of_ideas.txt', 'r') as file:
    # for each prompt:
    for line in file:
        line = line.split('|')
        if len(line) == 1: #skip empty lines
            continue

        short_description = line[1].strip()
        image_description = line[2].strip()
        commentary = line[3].strip()

        output_directory = f'output/{short_description}'
        os.makedirs(output_directory, exist_ok=True) #TODO throw error if folder exists and ignore?
        print(f'[info] {short_description}:')

        # generate the base image
        generate_image(client, image_description, output_directory, 'original_image')

        # generate voicover
        generate_commentary_audio(client, commentary, output_directory)

        # calculate the duration of the video to math the length of the audio
        audio_duration = AudioFileClip(f"{output_directory}/commentary.mp3").duration
        video_duration_in_frames = (int) (math.ceil(audio_duration * video_frame_rate * 100) / 100)
        
        # generate video
        generate_video_from_image(output_directory, video_duration_in_frames, video_frame_rate,
                                    1, 0.5, 0.5,
                                    1.2, 0.5, 0.5)

        # add voiceover to video
        add_audio_to_video(f"{output_directory}/initial_video.mp4", f"{output_directory}/commentary.mp3",
                           output_directory, start_delay=0) # todo increase start delay to 0.3/0.4

        # add subtitles
        add_subtitles_to_video(output_directory, "video_with_voiceover.mp4", "final_video.mp4", 
                               "commentary.mp3", "subtitles.srt")

        clean_everything_but_final_video(output_directory)
        # upload video to yt (title, hastags?)