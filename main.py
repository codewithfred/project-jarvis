import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import pywhatkit
from qrgen import makeQRCode

## Created by Alfred Soegiarto @Codewithfred ##

# ============= Bahasa Inggris ==================
# Please make sure to mention me when using this assistant, I would love to repost your stories!

# ============= Bahasa Indonesia ================
# Jangan lupa buat mention gw pas make asisten virtual ini, gw bakal seneng banget buat repost story kalian! 



## ENV_VARIABLES: Diganti pake punya kamu aja
ig_username = 'codewithfred'
favourite_song_link = ''
qr_code_link = 'https://instagram.com/codewithfred'
playlist_link = ''

#########################################################################################


class PersonalBot:
  def Listen(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print('Listening for orders..')
      r.pause_threshold = 0.7
      audio = r.listen(source)

      try:
        print("Recognizing orders..")
        Query = r.recognize_google(audio,language='en-in')
      
      except Exception as e:
        print(e)
        print("Can you please say your orders again?")
        return "None"

    return Query

  def Speak(self, audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
  jarvis = PersonalBot()
  jarvis.Speak('Good day sir, I\'m jarvis, how can i help you?')
  
  while True:
    result = jarvis.Listen()
    print("Your order is", result)

    ## Basic Commands
    if 'jarvis' in result.lower():
      jarvis.Speak('yes, sir?')

    if 'say something' in result.lower():
      jarvis.Speak('Thank you people, for following codewithfred, we can never achieve this without you guys, thank you so much')
      jarvis.Speak('Please stay healthy wherever you are, and keep coding, don\'t forget to share this account to your friends!')
      
    if 'thank you jarvis' in result.lower():
      jarvis.Speak('No problem sir')

    if 'open new browser' in result.lower():
      jarvis.Speak('Opening a new browser for you')
      os.system("start chrome")

    if 'open google' in result.lower():
      jarvis.Speak('Opening google')
      webbrowser.open("http://google.com", new=1)

    if 'open notepad' in result.lower():
      os.system("start notepad")

    if 'go to sleep jarvis' in result.lower(): 
      jarvis.Speak('shutting down')
      break

    if 'make qr code' in result.lower():
      jarvis.Speak('making your QR code')
      makeQRCode(qr_code_link)

    ## Youtube commands (Still simple, advanced method need OAuth)
    if 'open youtube' in result.lower():
      jarvis.Speak('Opening youtube')
      webbrowser.open("http://youtube.com", new=1)
    
    if 'my favorite song in youtube' in result.lower():
      jarvis.Speak('Searching your favourite song in youtube')
      webbrowser.open(favourite_song_link, new=1)
    
    if 'my playlist' in result.lower(): 
      webbrowser.open(playlist_link, new=1)

    ## Khusus Instagram methods
    # klo mo cari insta ngmgnya "search for instagram username tapi sangat susah wkkwkw soalnya jelek speechnya"
    if 'search for instagram' in result.lower():
      result = result.replace(" ", "")
      username = result[18::]
      insta_link = "http://instagram.com/{}".format(username)
      webbrowser.open(insta_link,new=1)

    if 'open my instagram' in result.lower():
      jarvis.Speak('Opening your instagram')
      insta_link = "http://instagram.com/{}".format(ig_username)
      webbrowser.open(insta_link,new=1)

    ## Play random games
    if 'play the worm game' in result.lower():
      jarvis.Speak('Opening slither io')
      webbrowser.open("http://slither.io",new=1)
    
    if 'play battle royale game' in result.lower():
      jarvis.Speak('Opening mini royale')
      webbrowser.open("http://miniroyale2.io",new=1)

    if 'play the shooting game' in result.lower():
      webbrowser.open("http://krunker.io",new=1)

    ## Open microsoft stuff
    if 'open word' in result.lower():
      jarvis.Speak('Opening microsoft word')
      os.system("start word")

    if 'open powerpoint' in result.lower():
      jarvis.Speak('Opening microsoft powerpoint')
      os.system("start powerpnt")

    if 'open excel' in result.lower():
      jarvis.Speak('Opening microsoft excel')
      os.system("start excel")

    ## Write in handwriting
    if 'write' in result.lower():
      jarvis.Speak('Writing your text using handwriting')
      command = str(result.lower())
      index_start = command.find("write")
      text = command[index_start+6:len(command)]

      pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
