import os
from common import get_openai_client
from ideaGenerator import generate_ideas
from imageCreator import generate_image
from videoGenerator import generate_video_from_image
from subtitleManager import add_subtitles_to_video
from voiceGenerator import generate_commentary_audio
from voiceoverToVideo import add_audio_to_video

#todo generate voice of length n, make sure video and voice are almost as long
# todo make video, commentary etc names parameters not hardcoded into smaller files

count = 2
client = get_openai_client()

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

        # image to video todo
        generate_video_from_image(output_directory,
                                    200, 25,
                                    1, 0.5, 0.5,
                                    1.2, 0.5, 0.5)

        # generate voicover
        generate_commentary_audio(client, commentary, output_directory)

        # add voiceover to video
        add_audio_to_video(f"{output_directory}/initial_video.mp4", f"{output_directory}/commentary.mp3",
                           output_directory, start_delay=0) # todo increase start delay to 0.3/0.4

        # add subtitles
        add_subtitles_to_video(output_directory, "initial_video.mp4", "video_with_subtitles.mp4", 
                               "commentary.mp3", "subtitles.srt")


        # upload video to yt (title, hastags?)