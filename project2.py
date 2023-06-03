import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS 

def textTospeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language,slow=False)
    myobj.save(filename)

def mergeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)    
    return combined

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        textTospeech(item['from'], 'WhatsApp Audio 2022-05-03 at 2.41.04 PM.mpeg')

        # audios = [f"{i}"] 
        announcement = mergeAudio(audio)
        announcement.export('WhatsApp Audio 2022-05-03 at 2.14.20 PM.mpeg') 

if __name__ == "__main__":
    print("Generating Announcement...")
    generateAnnouncement('WhatsApp Audio 2022-05-03 at 2.14.20 PM.mpeg')              