import speech_recognition as sr
import os
from tqdm import tqdm

# Get text with google speech to text API
# Limited to 50 requests per day
# Audio input needs to be wav, output is text

r = sr.Recognizer()
files = sorted(os.listdir('parts/'))
all_text = []
newFile = "source/new-audio.wav"

def transcriptFile():
   for f in tqdm(files):
      name = "parts/" + f
      #Loading audio file
      with sr.AudioFile(name) as source:
         audio = r.record(source)
      #Transcribe audio file
      text = r.recognize_google(audio)
      all_text.append(text)

   transcript = ""
   for i, t in enumerate(all_text):
      total_seconds = i*30
      m, s = divmod(total_seconds, 60)
      h, m = divmod(m, 60)

      transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t)

   print(transcript)
   return transcript

if __name__ == "__main__":
   with open("transcript.txt", "w") as f:
      f.write(transcriptFile())
   if os.path.isfile(newFile):
      os.remove(newFile)
   else:
      print("Error: %s file not found" % newFile)