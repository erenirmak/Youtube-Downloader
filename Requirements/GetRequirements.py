#introduction
print("2 items are needed:\n- Pytube (to detect video streams and download)\n- ffmpeg (to merge adaptive video streams with audio)\nThey will be checked automatically and if not found, they will be downloaded if you choose to do so.\nEnjoy!\n\n")

#check for pytube module, if not available, pip install it
try:
    import pytube
    print("Importing pytube is successful!\n")
except ImportError:
    choice = input("You don't have the pytube module which is required to find and download the YouTube video streams.\nWant to download? Y/N\n")
    if list(choice.lower())[0] == 'y':
        from pip._internal import main as pip
        pip(['install', '--user', 'pytube'])
        import pytube
        print("Importing pytube is successful!\n")
    else:
        print("Goodbye...")

#ffmpeg controls
import os
import requests

if not os.path.exists('./ffmpeg'):
    print("The highest resolution available progressive video streams are 720p.\nFor higher resolutions, you need to download adaptive video streams and audio files seperately and merge them together.\n")
    print("WARNING:\nffmpeg is not found! ffmpeg is necessary to merge adaptive video streams and audio files.\nIt is highly recommended to have ffmpeg.\nArchive file must have ffmpeg; please re-download the archive.\n")
    
    # You can download ffmpeg package from here:
    # 'https://www.gyan.dev/ffmpeg/builds/
    # You should open the archive in the same place of YouTube_Downloader.py
    # Rename the folder to 'ffmpeg'

#create folder for downloaded videos & audios
if not os.path.exists('./Downloads'):
    os.mkdir('Downloads')

def adaptive_file_paths():
    dir_video = './Downloads/Adaptive Video Streams/'
    dir_audio = './Downloads/Adaptive Audio Streams/'

    if not os.path.exists(dir_video):
        os.mkdir(dir_video)
    
    if not os.path.exists(dir_audio):
        os.mkdir(dir_audio)

    return True