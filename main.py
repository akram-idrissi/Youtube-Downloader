import os
import pytube
import sys

MP3 = '.mp3'
SINGLE_SONGS_DIR = 'single-songs'


def validate_args(args):
    if len(args) < 2:
        print('The provided arguments are not enough')
        return False

    return True


def get_links(path):
    links = []

    with open(f'{path}', 'r') as file:        
        for link in file.readlines():
            links.append(link.replace('\n', ''))

    return links   


def to_mp3(audio_mp4):
    name, _ = os.path.splitext(audio_mp4)
    audio_mp3 = name + MP3
    os.rename(os.path.join(SINGLE_SONGS_DIR, audio_mp4), 
        os.path.join(SINGLE_SONGS_DIR, audio_mp3))


def download(link):
    try:
        video = pytube.YouTube(link)
        print(f'Downloading {video.title}')
        audio = video.streams.filter(only_audio=True).first()
        audio = audio.download(SINGLE_SONGS_DIR)
        to_mp3(audio)
    except Exception as e:
        print(f'Error {str(e)}')
    

def main():

    args = sys.argv
    if not validate_args(args): return
    input = args[1]

    links = get_links(input)

    if not os.path.exists(SINGLE_SONGS_DIR):
        os.mkdir(SINGLE_SONGS_DIR)

    for link in links:
        download(link)


if __name__ == '__main__':
    main()
