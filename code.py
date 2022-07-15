from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, path, url):
        self.path = path
        self.url = url

    def get_video_detail(self):
        yt = YouTube(self.url)
        result = f'video title : {yt.title}\nvideo author : {yt.author}'
        return result