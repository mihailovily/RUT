from pytube import YouTube

link = 'https://www.youtube.com/watch?v=1PBg9cIAzr0'
def find_itag(link):
    yt = YouTube(link)
    a = yt.streams.filter(file_extension='mp4', type="video")
    for i in a:
        curr = str(i).split()
        to_dl = 0
        if curr[3] == 'res="720p"':
            to_dl = curr[1]
        if curr[3] == 'res="1080p"':
            to_dl = curr[1]
            break
    if to_dl == 0:
        to_dl = a[0].itag
    else:
        to_dl = to_dl.strip('itag="')
    return to_dl

def dl_video(link):
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(find_itag(link))
    stream.download()

dl_video(link)