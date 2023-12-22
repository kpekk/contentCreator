import requests, os

def generate_image(client, prompt, output_folder, output_file_name):

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792", # 9/16 ratio
        quality="standard",
        n=1,
    )

    image_data = response.data[0]

    image_response = requests.get(image_data.url)
    if image_response.status_code == 200:
        # Write the image data to a file
        with open(f'{output_folder}/{output_file_name}.png', 'wb') as f:
            f.write(image_response.content)

        print("[info]    Successfully downloaded the image")

    else:
        print("[info]    Failed to download the image")
