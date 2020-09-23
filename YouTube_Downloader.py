#YAPILACAKLAR

#altyazı bulma, seçme, indirme ve videoya entegrasyonu #### WILL_BE_DONE

#imports
from pytube import YouTube #download youtube streams audio/video
import os #handling files
import webbrowser as wb #dependency ffmpeg download
#for console-line command execution
import subprocess as sp
import sys
import Merger


def exit(): #exit function
    cntrl = 0
    a = 0 #while-loop flag determinant
    while cntrl == 0:
        cikis = input("Want to exit ? yes/no\n").upper()
        if cikis == 'YES' or cikis == 'Y':
            cntrl = 1
            a = 1
        elif cikis == 'NO' or cikis == 'N':
            cntrl = 1
            a = 0
        else:
            print("Please type 'yes' or 'no'")
            cntrl = 0
    return a

#README file
def readme():
    rmf = open("README.txt", "w+") # ReadMeFile handler variable and file creation/open
    rmf.write("WELCOME TO MY YOUTUBE DOWNLOADER\n\nThis program is designed to download any YouTube videos in any resolution.")
    rmf.write("\nYouTube videos may be in 2 different streams.\n\nProgressive streams have audio and video integrated in one file, but they offer resolutions\nup until 720p. For better resolutions, you need to download DASH (adaptive) ones.\n\n")
    rmf.write("DASH (adaptive) streams have either video or audio files and these files have to be\ndownloaded separately. Separate audio and video files must be merged together to obtain\n1 video file with audio, but DASH streams offer the resolutions higher than 720p.\n\n")
    rmf.write("To merge these audio and high resolution video files, I used ffmpeg, which is the external\ndependency of this script.\n\n")
    rmf.write("Please follow these instructions:\n1. If you had ffmpeg earlier, please uninstall it. Open command-line and type:\npip uninstall ffmpeg\npip uninstall ffmpeg-python\nThis step is automated in this script.\n")
    rmf.write("2. Install only ffmpeg python binding via console with\npip install ffmpeg-python\nThis step is automated in this script.\n")
    rmf.write("3. You need to download ffmpeg build package from http://ffmpeg.zeranoe.com/builds/. \nThis script is automated for some steps. It should direct you to the website.\n")
    rmf.write("4. Download the ffmpeg build package, open it and <Extract All> files.\n")
    rmf.write("5. Open the folder and you should see 3 folders named 'bin', 'doc', 'presets' accompanied\nby 2 .txt files, 'LICENSE' and 'README'. Select all of them and copy or cut.\n")
    rmf.write("6. Open your drive C:/ and create a new folder. Name it 'FFmpeg'. Paste the copied or cut\nfiles into the FFmpeg folder. This step is scripted, though. You should be able to find\nthe folder.\n")
    rmf.write("7. You need to add C://FFmpeg/bin directory to the environment variables as PATH.\nSystem Properties -> Advanced (Tab) -> Environment Variables -> System Variables, Path (double click)\n-> New -> Type the directory: C:\FFmpeg\"bin\n")
    rmf.write("8. Re-Run this script and enjoy downloading/archiving high quality YouTube videos. :)\n\nThere is also a surprise when the download will be completed! ;)")
    rmf.close()

#main function
def body():
    #youtube video link input
    inp = input("Enter the youtube link after 'watch?v=': ")
    yt = YouTube("https://www.youtube.com/watch?v="+inp)
    #video title
    print(yt.title) #"Video title: "+

    #streams
    print("Streams:")
    s_all = yt.streams.order_by(attribute_name = 'resolution') #order by resolution #Type: StreamQuery
    n_s_all = str(s_all).replace(', ','\n') #arrangement of new lines #Type: String
    n_s_all = n_s_all.replace('[','\n')
    n_s_all = n_s_all.replace(']','\n')
    print(n_s_all)

    #captions
    print("Captions:")
    cap_all = yt.captions
    n_cap_all = str(cap_all).replace(', ','\n')
    n_cap_all = n_cap_all.replace('{','\n')
    n_cap_all = n_cap_all.replace('}','\n')
    print(n_cap_all)

    #stream selection options
    flag = 0
    while (flag == 0):
        sel = int(input("What do you want to do?\n1. Download highest resolution stream that is progressive\n2. Download selected stream by itag\n"))
        if sel == 1: #highest resolution available in progressive format
            stream = yt.streams.get_highest_resolution()
            flag = 1
        elif sel == 2: #stream selection to download by itag
            s_itag = int(input("Enter the itag number of the stream that you want to download: "))
            stream = yt.streams.get_by_itag(itag = s_itag)
            flag = 1
        else:
            print("Undefined choice!")
            flag = 0

    #filesize of the selected stream
    fs = stream.filesize
    if fs < 1073741824:
        fsmb = fs / pow(1024, 2)
        print("Filesize: %.2f MB" %fsmb)
    else:
        fsgb = fs / pow(1024, 3)
        print("Filesize: %.2f GB" %fsgb)

    #other attributes' value checks
    print("Stream itag: ", stream.itag)
    print("Stream res: ", stream.resolution)
    print("Fps value: ", stream.fps)
    print("Condition of being progressive: ", stream.is_progressive)
    print("Type: ", stream.mime_type)

    #download & combine
    down = input("Want to download? Y/N\n").upper()
    if down == 'Y':
        fn = input("Filename: ") #define custom filename
        if stream.is_progressive:
            stream.download(output_path = 'C://YT_Downloads', filename = fn)
            print("Download successful!")
            
        else: #DASH download & combine
            vid = "video_"+fn
            aud = "audio_"+fn
            outp = "{fn}.mp4".format(fn=fn)

            #Adaptives' download
            if stream.includes_audio_track == False: #selected itag doesn't have audio
                stream.download(output_path = 'C://YT_Downloads/', filename = vid) #download video
                vidx = "{vid}.{xxx}".format(vid=vid, xxx=stream.mime_type.replace('video/',''))
                stream = yt.streams.get_audio_only() #find audio with the highest bitrate
                stream.download(output_path = 'C://YT_Downloads/', filename = aud) #download audio with highest bitrate only
                audx = "{aud}.{xxx}".format(aud=aud, xxx=stream.mime_type.replace('audio/',''))
            else:
                print("This is an audio file. Available progressive video with highest resolution will be downloaded instead.")
                stream = yt.streams.get_highest_resolution() #when audio file selected by itag, download progressive instead
                stream.download(output_path = 'C://YT_Downloads/', filename = fn)

            #ffmpeg-python merger function #merge_func(vidx,audx,outp)
            
            asd = Merger.merging(vidx, audx, outp)
            asd.get_inputs(vidx, audx)
            try:
                asd.merge(outp)
            except:
                print("Merging failed! Downloaded files are kept.")
            else:
                asd.del_file(vidx,audx)
            
    elif down == 'N':
        print("Sad story")
        exit()



#initiate/warning
flag = 0
while flag == 0:
    print("Welcome!\nThis script helps you download YouTube videos for free.\nBefore continue, please read README file.")
    cont = int(input("Press:\n1. If you already read the README file and followed the instructions,\n2. To follow the instructions on README file\n*This is just one-time step!\n"))
    if cont == 1: #end while loop, continue main() function
        body()
        flag = exit()
    elif cont == 2:
        readme()
        auto = input("For automated steps, press 'a'").upper()
        if auto == 'A':
            #create folder
            if os.path.exists("C://FFmpeg/") == False:
                os.mkdir("C://FFmpeg/")
                print("Directory created to copy downloaded files.")
            #download link
            print("Directing to the website...")
            wb.open('http://ffmpeg.zeranoe.com/builds/', new=1) 
            #command-line executions
            sp.check_call([sys.executable, "-m", "pip", "uninstall", 'ffmpeg']) 
            sp.check_call([sys.executable, "-m", "pip", "uninstall", 'ffmpeg-python'])
            try:
                import ffmpeg
            except ImportError:
                sp.check_call([sys.executable, "-m", "pip", "install", 'ffmpeg-python'])
            print("pip modifications are done!")
            flag = 1 #exit while-loop
        else:
            print("Exiting for manuel steps...")
            flag = exit()
    else:
        print("Undefined input! Please enter 1 or 2.")
        flag = 0


#import ffmpeg
#delete files after merged output
#def file_delete(name):
#    os.chdir("C://YT_Downloads/")
#    try:
#        os.remove(name)
#    except:
#        print("{File} cannot be deleted!".format(File = name))
#    else:
#        print("{File} has been deleted.".format(File = name))

##video/audio merger for adaptive files
#def merge_func(v, a, o):
#    try:
#        video_stream = ffmpeg.input("C://YT_Downloads/"+v)
#        audio_stream = ffmpeg.input("C://YT_Downloads/"+a)
#    except:
#        print("ffmpeg.input codes are not working!")
#        file_delete(v)
#        file_delete(a)
#    else:
#        ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output("C://YT_Downloads/"+o).run()
#        file_delete(v)
#        file_delete(a)
#        print("Successfully merged!")