import os

path = "./"
basepath = os.path.abspath(os.path.dirname('Task3'))
folder = os.path.join(basepath, 'Task3')

with open(os.path.join(folder, 'Task3.txt'), 'r') as f:    
    music_names: list = f.readlines() 

music_names = [x.rstrip() for x in music_names]
for i, music_name in enumerate(music_names):
    music_names[i] = music_name[:music_name.rfind(':')] + '.' + music_name[music_name.rfind(':')+1:] + '.mp3'

files = [f for f in os.listdir(folder) 
        if os.path.isfile(os.path.join(folder, f)) and f.endswith('.mp3')]

for file in files:
    for name in music_names:
        if file[:-4] in name: os.rename(os.path.join(folder, file), os.path.join(folder, name))