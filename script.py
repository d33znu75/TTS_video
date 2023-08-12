import os
from gtts import gTTS
from audiotsm import wsola
from audiotsm.io.wav import WavReader, WavWriter
from pydub import AudioSegment
from moviepy.editor import *
import subprocess

print("directory is : ",os.getcwd())

print("detecting files ...")

output_folder = os.getcwd()
output_audio_path = os.path.join(output_folder, "audio.mp3")

folder_path = os.getcwd()

#IF THE TEXT IS IN A TEXT FILE
#filename = "text.txt"
#file_path = os.path.join(folder_path, filename)
#with open(file_path, "r", encoding='UTF-8') as file:
#    content = file.read()

texto=input("Give text-to-speech :")
accent=input("Choose Language (ar/fr/en/es/...) :")
print("converting to WAV...")
#tts = gTTS(text=texto, lang='ar' )  //FOR TEXT FILE
tts = gTTS(text=texto, lang=accent)
tts.save(output_audio_path)


output_audio_path = os.getcwd()
output_audio = os.path.join(output_audio_path, "converted_audio.wav")


filename = "audio.mp3"

file_path = os.path.join(folder_path, filename)
                                                                     
src = file_path
dst = output_audio
                                                          
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

speedo=float(input("Choose Speed (0.5/1/1.2/2.8/...):"))

filename = "converted_audio.wav"

output_audio_path = os.getcwd()
output_filename = os.path.join(output_audio_path, "final_audio.wav")

with WavReader(filename) as reader:
    with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
        tsm = wsola(reader.channels, speed=speedo)
        tsm.run(reader, writer)

print("Deleting Cache Files...")

f1=os.path.join(folder_path, "audio.mp3")
f2=os.path.join(folder_path, "converted_audio.wav")
os.remove(f1)
os.remove(f2)

print("adding audio to video...")

input_video= os.getcwd()

input_video_path = os.path.join(input_video, "input_video.mp4")

output_video= os.getcwd()
output_video_path = os.path.join(output_video, "output_video.mp4")

output_audio = os.getcwd()
output_audio_path = os.path.join(output_audio, "final_audio.wav")

clip = VideoFileClip(input_video_path)

audio = AudioFileClip(output_audio_path)

if clip.duration < audio.duration :
    videoclip = clip.set_audio(audio)
    loopedClip = videoclip.loop(duration = audio.duration)
    loopedClip.write_videofile(output_video_path, fps=24, codec="libx264")
else:
    videoclip = clip.set_audio(audio)
    videoclip.write_videofile(output_video_path, fps=24, codec="libx264")


print("Deleting Cache Files...")

f3=os.path.join(folder_path, "final_audio.wav")
os.remove(f3)

print("Doneeee !")
