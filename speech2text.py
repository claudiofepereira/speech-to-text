import speech_recognition as sr

# Get text with google speech to text API
# Limited to 50 requests per day
# Audio input needs to be wav, output is text

# To-Do:
## Implement a way to make paragraphs and dots where need be.
## Define a way to get the language automatically.
## Get the audio file size (in time) and check if the program needs to
## consider more than 45 seconds (max time is 60seconds per request i believe).

r = sr.Recognizer()

text = {}
i = 0

som = sr.AudioFile('new-audio.wav')

with som as source:
   for audio in range(0,4):
      if i == 0:
         audio = r.record(source, duration = 34)
         #text["1 sentence"] = r.recognize_google(audio, language='pt-PT')
         text["1 sentence"] = r.recognize_google(audio)
         i = 1
         del audio
      # else:
      #    audio = r.record(source, offset = (45*i), duration = 45)
      #    text[str(i+1) + " sentence"] = r.recognize_google(audio, language='pt-PT')
      #    i += 1
      #    del audio

for key, value in text.items():
   print(value, end = " ")