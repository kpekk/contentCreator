import os

def generate_commentary_audio(client, text, output_directory):
  response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=text
  )

  response.stream_to_file(os.path.join(output_directory, 'commentary.mp3'))

  print('[info]    Successfully generated commentary mp3 file')