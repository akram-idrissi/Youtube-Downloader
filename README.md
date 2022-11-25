# Youtube Downloader
Youtube Downloader is an automation that makes downloading youtube videos fast and easy.

# Set up
* Clone this repository using: `git clone https://github.com/akram-idrissi/Youtube-Downloader.git`
* Install the required modules using: `pip install -r requirements.txt`

# Arguments

| Short Form    | Long Form    | Descritpion  |
| ------------- | -------------| -------------|
| -h  | --help | show help     |
| -v  | --video | needs a video url     |
| -p  | --playlist | needs a playlist url     |
| -mv  | --multiple_videos | needs path for file that has urls     |
| -mp  | --multiple_playlists | needs path for file that has urls     |

# Usage

```
python main.py -v https://youtube.com/some_video

python main.py -p https://youtube.com/some_playlist

python main.py -mv absolute_file_path

python main.py -mp absolute_file_path

```

The output will be sotred in a file called output that has the downloaded videos.

# Upcoming features
* Keep track of what has been downloaded and not, in case we stop downloading and we want to come back later and start from where we left.
* Make the script multi threading.

# Side Note
* command to generate requirements.txt file: `pip freeze > requirements.txt`
