<h1>AI short video creator</h1>

<h2>Why was this code written?</h2>

I wanted to learn about AI and prompting basics. I also saw a short statistical analysis
about the amount of AI generated content on YouTube and decided to add my own share of 
content of the utmost quality.

Needless to say, that plan failed. But I had fun learning some new stuff.

<h2>Anyway, what exactly does this code do?</h2>

This code generates multiple short "animal fact" type videos, with the video slowly 
zooming in to an AI-generated image of an animal, with a (also AI-generated) voiceover
of an animal fact. And, of course, subtitles.

<b>Samples of the generated videos can be found in the /output folder.</b>

1. (using ai) Generate ideas - generate a given count of image ideas

The idea consists of 3 parts:
* Image title (used for image and video naming)
* Image description
* A fact about the animal on the picture

(For every generated idea:)

2. (using ai) Generate a base image using the image description
3. (using ai) Generate a voiceover for the video using the fact about the animal
4. Generate a video using the image (the same image with a zoom in effect)
5. Add the voiceover to the video
6. (using ai) Add subtitles to the video