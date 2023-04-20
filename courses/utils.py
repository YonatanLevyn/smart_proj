from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyAntkQDpLWoxaf6IfQ0O3bFhuldQEO41vQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_youtube_video_info(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)
    response = youtube.videos().list(
        id=video_id,
        part='snippet, contentDetails'
    ).execute()

    if response['items']:
        video = response['items'][0]
        return {
            'title': video['snippet']['title'],
            'description': video['snippet']['description'],
            'duration': video['contentDetails']['duration'],
            'thumbnail_url': video['snippet']['thumbnails']['medium']['url'],
        }
    return None
