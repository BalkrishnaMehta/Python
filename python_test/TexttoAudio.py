import gtts
from playsound import playsound
tts = gtts.gTTS("how are you", lang ="gu")
tts.save("hello.mp3")
playsound("hello.mp3")
