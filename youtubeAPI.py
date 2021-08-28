from math import ceil

from googleapiclient.discovery import build

from config import API_KEY

youtube = build('youtube', 'v3', developerKey=API_KEY)


def getChannelId(channel_name):
    request = youtube.channels().list(
        part='snippet, contentDetails, statistics',
        forUsername=channel_name
    )
    response = request.execute()
    try:
        channel = response['items']
        for info in channel:
            channel_id = info['id']
            return channel_id
    except Exception as err:
        return False


def searchVideosIdByIdChannel(channel_id, published_after, published_before, page_token=None, max_results=50):
    request = youtube.search().list(
        part='id',
        type='video',
        channelId=channel_id,
        order='date',
        publishedAfter=published_after,
        publishedBefore=published_before,
        maxResults=max_results,
        pageToken=page_token
    )
    response = request.execute()
    return response


def getVideosStatistic(list_of_id_videos):  # takes list with video ID`s
    start_id = 0
    stop_id = 50
    result = []
    for video in range(ceil(len(list_of_id_videos) / 50)):
        part_ids = list_of_id_videos[start_id:stop_id]
        part_ids = ','.join(part_ids)
        request = youtube.videos().list(
            part='snippet,statistics',
            id=part_ids,
        )
        result.append(request.execute())
        start_id += 50
        stop_id += 50
    return result
