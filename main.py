'''
1. Copy all files Temp 1
2. Rename all files
3. Get thumbnails Temp 2
4. Convert all files Temp 3
5. Add cover art
6. Give output Output
'''

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, os
import ffmpeg
import eyed3

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(150,150,400,300)
    win.setWindowTitle("Godlike Video Converter")

    win.show()
    sys.exit(app.exec())

def rename():
    base_dir="D:/Converter/Copied/"
    to_rename= os.listdir(path=base_dir)
    for x in to_rename:
        new_name=x.replace(' ','_')
        os.rename(base_dir+x,base_dir+new_name)
    print(base_dir)
    print(len(to_rename))

def get_thumbnail():
    base_dir = "D:/Converter/Copied/"
    thumbnail_dir= "D:/Converter/Thumbnails/"
    to_get_thumbnail = os.listdir(path=base_dir)
    for x in to_get_thumbnail:
        video_file=base_dir+x
        thumbnail=thumbnail_dir+x+'.png'
        cmd = "ffmpeg -i {} -ss 00:00:30 -vframes 1 {}".format(video_file, thumbnail)
        os.system(cmd)


def convert():
    base_dir = "D:/Converter/Copied/"
    converted_dir = "D:/Converter/Converted/"
    to_convert = os.listdir(path=base_dir)
    for x in to_convert:
        video_file = base_dir + x
        audio_file = converted_dir + x + '.mp3'
        cmd="ffmpeg -i {} -vn {}".format(video_file,audio_file)
        os.system(cmd)



def add_cover_art():
    base_dir = "D:/Converter/Converted/"
    base_dir2 = "D:/Converter/Copied/"
    thumbnail_dir= "D:/Converter/Thumbnails/"
    to_add_cover_art = os.listdir(path=base_dir2)
    for x in to_add_cover_art:
        audio_file=base_dir+ x + '.mp3'
        thumbnail=thumbnail_dir+x+'.png'
        print(audio_file)
        print(thumbnail)
        audiofile = eyed3.load(audio_file)
        audiofile.initTag()
        audiofile.tag.images.set(3, open(thumbnail, 'rb').read(), 'image/png')
        audiofile.tag.save(version=eyed3.id3.ID3_V2_3)




rename()
get_thumbnail()
convert()
add_cover_art()
#window()



