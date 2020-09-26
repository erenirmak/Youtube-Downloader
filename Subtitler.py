import ffmpeg
import os

class GetSubtitle:
    def __init__(self, choice, subStream, langCode):
        self.choice = choice
        self.subStream = subStream
        self.langCode = langCode
        GetSubtitle.subList(self, choice, subStream)
        
    def subList(self, choice, subStream):
        global subLangCode

        print("Captions:")
        cap_all = self.subStream.captions
        n_cap_all = str(cap_all).replace(', ','\n')
        n_cap_all = n_cap_all.replace('{','\n')
        n_cap_all = n_cap_all.replace('}','\n')
        n_cap_all = n_cap_all.replace('>','')
        print(n_cap_all)

        flag = 0
        while flag == 0:
            if self.choice == 'Y':
                subLangCode = input("Language code of subtitle you want to download: ")
                GetSubtitle.getSub(self, self.subStream, subLangCode)
                flag = 1

            elif self.choice == 'N':
                print("no subs as you wish")
                flag = 1
            else:
                print("wrong choice!")
                flag = 0

    def getSub(self, subStream, langCode):
        subDown = self.subStream.captions['{LC}'.format(LC = langCode)]
        subDown.download(title = self.subStream.title, output_path = 'C://YT_Downloads/')

    def getSubLang(self):
        return subLangCode

class MergeSubtitle:
    def __init__(self, vidFile, subFile, outMerged):
        self.subFile = subFile
        self.vidFile = vidFile
        self.outMerged = outMerged

    def get_inputs(self, vidFile, subFile):
        global vidF #keep the value globally
        global subF
        
        vidF = ffmpeg.input("C://YT_Downloads/"+self.vidFile)
        subF = ffmpeg.input("C://YT_Downloads/"+self.subFile)
        print("vid & sub inputs successful")

    def merge(self, outMerged): #ffmpeg merge function
        ffmpeg.overlay(vidF, subF).output("C://YT_Downloads/"+self.outMerged).run()
        print("Successfully merged!")
        

    def del_file(self, subFile): #delete tmp files
        os.chdir("C://YT_Downloads/")
        os.remove(self.subFile)