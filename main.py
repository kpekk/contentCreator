import os
from common import get_openai_api_key
from openai import OpenAI
from ideaGenerator import generate_ideas
from imageCreator import generate_image
from imageToVideo import generate_video_from_image
from voiceGenerator import generate_commentary_audio

count = 2
client = OpenAI(api_key=get_openai_api_key())

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

        break
        # generate voicover
        generate_commentary_audio(client, commentary, output_directory)

        # add voiceover to video

        # add subtitles???????



        # upload video to yt (title, hastags?)