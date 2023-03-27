from pytube import YouTube



def dl_video(link, res='720p'):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_by_resolution(res)
    try:
        youtubeObject.download(filename='video.mp4')
    except:
        print("An error has occurred")
