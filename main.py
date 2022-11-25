import argparse
import os
import pytube

MP3 = '.mp3'
OUTPUT_DIR = 'output'


def get_args():
    my_parser = argparse.ArgumentParser(
        prog='main',
        usage='%(prog)s options',
        description='Download and convert youtube videos to mp3 format')

    my_parser.add_argument('-v', '--video', metavar='', help='needs a video url')    
    my_parser.add_argument('-p', '--playlist', metavar='', help='needs a playlist url')
    my_parser.add_argument('-mv', '--multiple_videos', metavar='', help='needs path for file that has urls')
    my_parser.add_argument('-mp', '--multiple_playlists', metavar='', help='needs path for file that has urls')

    return my_parser.parse_args()

  
def get_links(path):
    links = []

    with open(f'{path}', 'r') as file:        
        for link in file.readlines():
            links.append(link.replace('\n', ''))

    return links   


def to_mp3():
    os.chdir(OUTPUT_DIR)
    for song in os.listdir():
        name, _ = os.path.splitext(song)
        audio_mp3 = name + MP3
        os.rename(song, audio_mp3)    


def download(video):
    try:
        print(f'Downloading {video.title}')
        audio = video.streams.filter(only_audio=True).first()
        audio = audio.download(OUTPUT_DIR)
        to_mp3()
    except Exception as e:
        print(f'Error {str(e)}')


def download_playlist(url):
    playlist = pytube.Playlist(url)
    print(f'Downloading: {playlist.title}')

    for video in playlist.videos:
        download(video)


def download_video(url):
    video = pytube.YouTube(url)
    download(video)


def main():
    args = get_args()

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    if args.video:
        download_video(args.video)

    elif args.playlist:
        download_playlist(args.playlist)

    elif args.multiple_videos:
        links = get_links(args.multiple_videos)
        for link in links:
            download_video(link)

    elif args.multiple_playlists:
        links = get_links(args.multiple_playlists)
        for link in links:
            download_playlist(link)

    else:
        print('You didn\'n provide enough arguments. Get help by running: python main.py -h')


if __name__ == '__main__':
    main()
