
class RMF:
    def __init__(self, rmf):
        self.rmf = rmf

    #README file
    def readme(self):
        rmf = open("README.txt", "w+") # ReadMeFile handler variable and file creation/open
        rmf.write("WELCOME TO MY YOUTUBE DOWNLOADER\n\nThis program is designed to download any YouTube videos in any resolution.")
        rmf.write("\nYouTube videos may be in 2 different streams.\n\nProgressive streams have audio and video integrated in one file, but they offer resolutions\nup until 720p. For better resolutions, you need to download DASH (adaptive) ones.\n\n")
        rmf.write("DASH (adaptive) streams have either video or audio files and these files have to be\ndownloaded separately. Separate audio and video files must be merged together to obtain\n1 video file with audio, but DASH streams offer the resolutions higher than 720p.\n\n")
        rmf.write("To merge these audio and high resolution video files, I used ffmpeg, which is the external\ndependency of this script.\n\n")
        rmf.write("Please follow these instructions:\n")
        rmf.write("1. If you had ffmpeg earlier, please uninstall it. Open command-line and type:\npip uninstall ffmpeg\npip uninstall ffmpeg-python\n\n")
        rmf.write("2. Install only ffmpeg python binding via console with\npip install ffmpeg-python\n\n")
        rmf.write("3. You need to download ffmpeg build package from http://ffmpeg.zeranoe.com/builds/. \n\n")
        rmf.write("4. Download the ffmpeg build package, open it and <Extract All> files.\n\n")
        rmf.write("5. Open the folder and you should see 3 folders named 'bin', 'doc', 'presets' accompanied\nby 2 .txt files, 'LICENSE' and 'README'. Select all of them and copy or cut.\n\n")
        rmf.write("6. Open your drive C:/ and create a new folder. Name it 'FFmpeg'. Paste the copied or cut\nfiles into the FFmpeg folder.\n\n")
        rmf.write("7. You need to add C://FFmpeg/bin directory to the environment variables as PATH.\nSystem Properties -> Advanced (Tab) -> Environment Variables -> System Variables, Path (double click)\n-> New -> Type the directory: C:\FFmpeg\\bin\n\n")
        rmf.write("8. Find the ffmpeg/cipher.py file, open it and find the line:\nblablabla\nChange the line as follows:\nblablabla\n\n")
        rmf.write("9. Re-Run this script and enjoy downloading/archiving high quality YouTube videos. :)\n\n")
        rmf.close()

        return 1