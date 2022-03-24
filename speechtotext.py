from fileinput import filename
import speech_recognition as sr
import firebase

filename = "foo.wav"
# user_id = "-MymfleF93MPDO_U5BSJ";
# firebase.upload_audio(user_id)

def generate_keywords(user_id):
  firebase.download_file(f'audio/Mumbai/{user_id}/foo.wav', filename)
  r = sr.Recognizer()

  with sr.AudioFile(filename) as source:
      audio_data = r.record(source)
      text = r.recognize_google(audio_data)
      print(text)
      print(type(text))
      audioinput=text.split(" ")
      print(type(audioinput))
      print(audioinput)

  keywords = []
  det_words = []
  for i in range (0,500):
    keywords.append(i)
  # keywords.extend(['people', 'fire', 'food', 'water', 'help', 'medicine','stuck','dying','starving','famine','children','electricity','injury', 'dead'])
  keywords.extend(['people','help','food','starve','starving','hungry','hunger','famine','water','drought','thirsty''medicine','injury','dead','electricity','trees',''])
  for word in audioinput:
    if word in keywords:
      det_words.append(word)
  final = set(det_words)
  f = ', '.join(det_words)
  firebase.push_keywords(f, user_id)





