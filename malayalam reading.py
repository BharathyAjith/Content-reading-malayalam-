import io
from gtts import gTTS
from playsound import playsound
fp =io.open("abdulkalam.txt",mode="r",encoding="utf-8")
kalam_content = fp.read()
ob = gTTS(kalam_content,lang='ml')
ob.save("abdulkalam.mp3")
playsound("abdulkalam.mp3")