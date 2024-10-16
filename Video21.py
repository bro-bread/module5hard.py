class Video:
    list_video = []
    def __init__(self,  title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        Video.list_video.append(title)

    def str21(self):
        return f"{self.title},{self.duration},{self.time_now}"

BID = Video("dota2",200,34)
BID2 = Video("KS4",134,10)
BID3 = Video("VAVE",100,99)