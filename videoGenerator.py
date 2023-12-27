#from https://medium.com/p/150e698743b5, big ty

import os, shutil
from PIL import Image

def generate_video_from_image(
    working_folder,
    duration, frame_rate,
    initial_zoom, initial_x, initial_y,
    final_zoom, final_x, final_y,
):
    image = Image.open(f'{working_folder}/original_image.png')

    output_folder = os.path.join(working_folder, 'initialVideo')
    os.makedirs(output_folder, exist_ok=True)

    print(f'[info]    Initializing video creation, total frames: {duration}, frame rate {frame_rate}')

    for i in range(duration):
        
        if (i+1) % 50 == 0:
            print(f'[info]    Created frame no.{i+1}')

        # the factor that we use to interpolate between the initial and final values
        interpolation_factor = i / duration

        # calculate the zoom level
        zoom_level = (1 - interpolation_factor) * initial_zoom + interpolation_factor * final_zoom

        # calculate the crop size
        crop_width = image.width / zoom_level
        crop_height = image.height / zoom_level

        # calculate the crop position
        crop_x = (image.width - crop_width) * ((1 - interpolation_factor) * initial_x + interpolation_factor * final_x)
        crop_y = (image.height - crop_height) * ((1 - interpolation_factor) * initial_y + interpolation_factor * final_y)

        # crop the image
        cropped_image = image.crop(
            (crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))

        # resize the image
        resized_image = cropped_image.resize((image.width, image.height))
        
        # save the image
        filename = os.path.join(output_folder, f'frame-{i}.png')

        resized_image.save(filename)

    cmd = f'''
ffmpeg -y -framerate {frame_rate} -i {os.path.join(output_folder, f'frame-%d.png')} {os.path.join(working_folder, 'initial_video.mp4')} -loglevel quiet
    '''.strip()
    os.system(cmd)

    #delete all the generated images
    shutil.rmtree(output_folder)

    print('[info]    Successfully created the initial video')