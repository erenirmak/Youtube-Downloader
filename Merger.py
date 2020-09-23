import ffmpeg #to combine DASH audio and video files
import os 

class merging:

    def __init__(self, vid, aud, outp): #input declarations
        self.vid = vid
        self.aud = aud
        self.outp = outp

    def get_inputs(self, vid, aud): #ffmpeg inputs
        global vid_s #keep the value globally
        global aud_s
        vid_s = ffmpeg.input("C://YT_Downloads/"+self.vid)
        aud_s = ffmpeg.input("C://YT_Downloads/"+self.aud)
        print("inputs successful!")

    def merge(self, outp): #ffmpeg merge function
        ffmpeg.concat(vid_s, aud_s, v=1, a=1).output("C://YT_Downloads/"+self.outp).run()
        print("Successfully merged!")

    def del_file(self, vid, aud): #delete tmp files
        os.chdir("C://YT_Downloads/")
        os.remove(self.vid)
        os.remove(self.aud)