#imports
from Requirements.GetRequirements import * # start from here
import Classes.Downloader as Downloader
import Classes.Merger as Merger
import Subtitler #under construction

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

#body function
def body():
    #youtube video link input
    lnk = input("Enter the youtube link after 'watch?v=': ")
    streamer = Downloader.GetStreams(lnk)
    subStreamer = streamer.get_link(lnk)
    streamer.get_stream_attr(0, 0) #stream list

    #stream selection options
    flag = 0
    while (flag == 0):
        sel = int(input("What do you want to do?\n1. Download highest resolution stream that is progressive\n2. Download selected stream by itag\n"))
        if sel == 1: #highest resolution available in progressive format
            streamTmp = streamer.get_stream_attr(sel, 0)
            flag = 1
        elif sel == 2: #stream selection to download by itag
            s_itag = int(input("Enter the itag number of the stream that you want to download: "))
            streamTmp = streamer.get_stream_attr(sel, s_itag)
            flag = 1
        else:
            print("Undefined choice!")
            flag = 0

    #download & combine
    downSelect = input("Want to download? Y/N\n").upper()
    if downSelect == 'Y':
        fn = input("Filename: ") #define custom filename
        fn = fn + ".mp4"
        if streamTmp.is_progressive:
            Downloader.GetProgressive.GP_Download(fn)
            print("Download successful!")
            
        else: # DASH download & combine
            vid = "video_"+fn
            aud = "audio_"+fn
            outp = "{fn}.mp4".format(fn=fn)
            dwn = Downloader.GetAdaptive(vid, aud)
            
            # Adaptives' download
            if streamTmp.includes_audio_track == False: #selected itag doesn't have audio, so it is video
                dwn.VideoAdaptive(vid)
                vidx = "{vid}.{xxx}".format(vid=vid, xxx=streamTmp.mime_type.replace('video/',''))

                #dwn.AudioAdaptive(aud)
                audx = "{aud}.{xxx}".format(aud=aud, xxx=dwn.AudioAdaptive(aud).mime_type.replace('audio/',''))
                print(audx)
            else:
                print("This is an audio file. Available progressive video with highest resolution will be downloaded instead.")
                streamer.get_stream_attr(1, 0)
                Downloader.GetProgressive.GP_Download(fn) #when audio file selected by itag, download progressive instead
                
            # Merger call            
            mrg = Merger.merging(vidx, audx, outp) # instantiating
            mrg.get_inputs(vidx, audx)
            try:
                mrg.merge(outp)
            except:
                print("Merging failed! Downloaded files are kept.")
            else:
                mrg.del_file(vidx,audx)
            
        subSelect = input("Want to download and merge subtitles if available? y/n\n\nSubtitle feature is still under construction! Sorry for the inconvenience.\nEnjoy! :)").upper()
        
        #outp = "{fn}.mp4".format(fn=fn)
        #outp2 = "{fn}_subtitled.mp4".format(fn=fn)
        #Subtitler.GetSubtitle(subSelect, subStreamer, "")
        #subname = subStreamer.title+" ("+Subtitler.GetSubtitle.getSubLang("")+").srt"
        #subHandler = Subtitler.MergeSubtitle(outp, subname, outp2)
        #subHandler.get_inputs(outp, subname)
        ##try:
        #subHandler.merge(outp2)
        ##except:
        ##    print("Error occured! Closing..")
        ##else:
        ##    subHandler.del_file(subname)
        ##    print("Temp subtitle file deleted, merge successful!")

    elif downSelect == 'N':
        print("Sad story")
        exit()
body()