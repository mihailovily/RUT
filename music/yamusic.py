import yandex_music


token = open('tokens/music.txt').readline()
print(token)
client = yandex_music.Client(token).init()

def track_dl(link):
    client_track = client.tracks(decompose_link(link))[0]
    client_track.download('track.mp3')
    return title_artist(client_track)


def decompose_link(link):
    link = link.split('/')[3:]
    album, track = link[1], link[3].split('?')[0]
    return track + ':' + album

def title_artist(client_track):
    artists = ''
    if client_track.artists:
        artists = ' - ' + ', '.join(artist.name for artist in client_track.artists)
    user_result_text = client_track.title + artists
    return user_result_text

