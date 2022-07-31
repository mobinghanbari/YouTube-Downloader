from code import *

print('Please Turn on your proxy (if you are in iran)')
url = input('Please Insert Your Url =>')
path = input('Please Insert Your Path To Save Video =>')
request_type = input('What is your favorite video resolution ? (high/low)')

obj = YouTubeDownloader(path, url)
print(obj.get_video_detail())
con_in = input('Is It Right? (yes/no)')
if con_in == 'yes':
    obj.download(request_type)

elif con_in == 'no':
    print('Your Information Was Wrong')