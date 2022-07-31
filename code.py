from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, path, url):
        self.path = path
        self.url = url

    def get_video_detail(self):
        yt = YouTube(self.url)
        result = f'video title : {yt.title}\nvideo author : {yt.author}'
        return result

    def download(self, resolution):
        yt = YouTube(self.url)
        if resolution == 'high':
            try:
                yt.streams.get_highest_resolution().download(self.path)
                print('Downloading ...')

            except Exception:
                print('Please Check Your Internet Or Proxy(if you are in iran)')

        elif resolution == 'low':
            try:
                yt.streams.get_lowest_resolution().download(self.path)
                print('Downloading ...')
                
            except Exception:
                print('Please Check Your Internet Or Proxy(if you are in iran)')
        
        else:
            print('Please Write Your Resolution Correctly')