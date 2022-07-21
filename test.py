from googleapiclient.discovery import build

from config import API_KEY

# channel_id = UCwPzq5yQwczLmivBX8zq7Mw
youtube = build('youtube', 'v3', developerKey=API_KEY)


def search(page_token=None):
    request = youtube.search().list(
        part='id',
        type='video',
        channelId='UCI0t9OsDta3rJwjN_GG3_Aw',
        order='date',
        publishedAfter='2011-03-02T00:00:00Z',
        publishedBefore='2022-06-30T23:59:59Z',
        maxResults=50444,
        pageToken=page_token
    )
    response = request.execute()
    return response


def filter(response):
    list_with_all_id_videos = []
    def extract_id_videos(text_for_extract):
        for video in text_for_extract['items']:
            list_with_all_id_videos.append(video['id']['videoId'])
    try:
        while response['nextPageToken']:
            extract_id_videos(response)
            response = search(page_token=response['nextPageToken'])
    except Exception:
        extract_id_videos(response)
    return list_with_all_id_videos

result = search()
filtered_result = filter(result)
print(filtered_result)
print(len(filtered_result))
import ipdb; ipdb.set_trace()



