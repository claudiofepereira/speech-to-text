# Info:
- For now, can only use .mp4 and .wav files.

# Problems:
- If the 30s chunk doesn't have any audio, google recognition will throw an error. Solution right now is to delete the last chunk.

# To-Do:
- [ ] Make the program accept files as an argument - import convert.py to the speech2text.py.
- [ ] Implement a way to make paragraphs and dots in the text, where need be. (got the time working in chunks of 30 seconds.)
- [ ] Define a way to get the language of the audio automatically.
- [ ] Try to use other types of video/audio files.
- [ ] Implement a way to reduce background noise.
- [ ] Make this program accessible as a webapp, using flask.
- [ ] Implement a way to count when each sentence is said (in time), in a way as the subtitles work.
