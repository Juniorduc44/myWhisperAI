__version__="0.0.1"
#txtParserGUI
#python 3.10.12
import whisper
'''
The choices for model are:
tiny = 39M == 1GB
base = 74M == 1GB
small = 244M == 2GB
medium = 769M == 5GB
large = 1550M == 10GB
'''

md ="base"
model = whisper.load_model(md)
rs = list()
result = model.transcribe("random_innovationAudio_128 kbps.mp3")

d = (list(result.items()))


for i in d:
    rs.append(i[1])
dd = (rs[0])
print(dd)


with open(f"{md}.txt", 'w') as f:
    f.write(dd)
    f.close()