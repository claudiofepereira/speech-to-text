# Info:
- For now, can only use .mp4 and .wav files. (maybe not?)

# Problems:
- If the 30s chunk doesn't have any audio, google recognition will throw an error. Solution right now is to delete the last chunk.

# To-Do:
- Make the program accept files as an argument - import convert.py to the speech2text.py.
- Implement a way to make paragraphs and dots in the text, where need be. (got the time working in chunks of 30 seconds.)
- Define a way to get the language of the audio automatically.
- Get the audio file size (in time) and check if the program needs to consider more than blocks of 45 seconds (max time is 60 seconds per request i believe). Sending requests of more than 60 seconds breaks the program for now. Consider changing API. - Got this by dividing the audio source into parts of 30 seconds.
- The text is being saved in a dictionary ("text"), test out another ways of saving it. - Done did it.
- Try to use other types of video/audio files.

# Dreamy To-Do:
- Implement a way to reduce background noise.
- Make this program accessible as a webapp.
- Implement a way to count when each sentence is said (in time), in a way as the subtitles work.
