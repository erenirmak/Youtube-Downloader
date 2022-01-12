from pytube import YouTube #need it to reach YouTube video streams and attributes

class GetStreams:
    def __init__(self, link):
        self.link = link

    def get_link(self, link):
        global yt
        yt = YouTube("https://www.youtube.com/watch?v="+self.link)
        return yt

    def get_stream_attr(self, streamSelect, itagSelect):

        global streaming
                
        if streamSelect == 1:
            streaming = yt.streams.get_highest_resolution()
            GetStreams.otherAttr(streaming)
            return streaming
        elif streamSelect == 2:
            streaming = yt.streams.get_by_itag(itag = itagSelect)
            GetStreams.otherAttr(streaming)
            return streaming
        else:
            linkStreamList = yt.streams.order_by(attribute_name = 'resolution')
            print("Title of the stream: "+yt.title)
            print("Available streams:")
            print(GetStreams.printArrange(linkStreamList))

    def printArrange(self): # in-class method
        n_s_all = str(self).replace(', ','\n') #new_stream_all #arrangement of new lines #Type: String
        n_s_all = n_s_all.replace('[','\n')
        n_s_all = n_s_all.replace(']','\n')
        return n_s_all

    def streamFilesize(self): # Stream of Interest # in-class method
        fs = self.filesize
        if fs < 1073741824:
            fsmb = fs / pow(1024, 2)
            print("Filesize: %.2f MB" % fsmb)
        else:
            fsgb = fs / pow(1024, 3)
            print("Filesize: %.2f GB" % fsgb)

    def otherAttr(self): #in-class method
        GetStreams.streamFilesize(self) #filesize of the selected stream
        #other attributes' value checks
        print("Stream itag: ", self.itag)
        print("Stream res: ", self.resolution)
        print("Fps value: ", self.fps)
        print("Condition of being progressive: ", self.is_progressive)
        print("Type: ", self.mime_type)

class GetProgressive:
    def __init__(self, fileName):
        self.fileName = fileName

    def GP_Download(self):
        print("Downloading the video is starting...")
        streaming.download(output_path = './Downloads/', filename = self)

class GetAdaptive:
    def __init__(self, vidn, audn):
        self.vidn = vidn
        self.audn = audn

    def VideoAdaptive(self, vidn):
        print("Downloading the adaptive video is starting...")
        streaming.download(output_path = './Downloads/', filename = self.vidn)
    
    def AudioAdaptive(self, audn):
        print("Downloading the audio is starting...")
        audstream = yt.streams.get_audio_only() #find audio with the highest bitrate
        audstream.download(output_path = './Downloads/', filename = self.audn) #download audio with highest bitrate onlypass
        return audstream