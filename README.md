# Youtube-Downloader
WELCOME TO MY YOUTUBE DOWNLOADER
This program is designed to download any YouTube videos in any resolution. YouTube videos can be in 2 different streams.

Progressive streams have audio and video integrated in one file, but they offer resolutions up until 720p.
For better resolutions, you need to download DASH (adaptive) ones.

DASH (adaptive) streams have either video or audio files and these files have to be downloaded separately.
Separate audio and video files must be merged together to obtain 1 video file with audio, but DASH streams offer the resolutions higher than 720p.

To merge these audio and high resolution video files, I used ffmpeg-python.

Please follow these steps:
1. Installations:

pytube:
pip install pytube

ffmpeg-python:
pip install ffmpeg-python

P.S: If you had installed ffmpeg earlier, please uninstall it before continue. Be sure that you only pip-installed ffmpeg-python:
pip uninstall ffmpeg
pip uninstall ffmpeg-python

2. You need to download ffmpeg build package from http://ffmpeg.zeranoe.com/builds/.

3. Download the ffmpeg build package, open it and <Extract All> files.

4. Open the folder and you should see 3 folders named 'bin', 'doc', 'presets' accompanied by 2 .txt files, 'LICENSE' and 'README'.
Select all of them and copy or cut.

5. Open your drive C:/ and create a new folder. Name it 'FFmpeg'. Paste the copied or cut files into the FFmpeg folder.

6. You need to add C://FFmpeg/bin directory to the environment variables as PATH.
System Properties -> Advanced (Tab) -> Environment Variables -> System Variables, Path (double click) -> New -> Type the directory: C:\FFmpeg\\bin\

7. Find* the extract.py file in pytube, open it and find the line (line 301):
parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
Change the line as follows:
parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)

*P.S: You can find the installed location via;
pip show pytube

8. Run this script and enjoy downloading/archiving high quality YouTube videos and subtitles. :)

NOTE: Merging subtitles with downloaded video is not working properly. I will update Subtitler.py file.
NOTE-2: The default download folder for videos and subtitles is defined as "C://YT_Downloads/".
