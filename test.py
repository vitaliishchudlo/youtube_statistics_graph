import datetime
import json
from math import ceil

from googleapiclient.discovery import build

channel_name = 'FootballTVUA'
channel_id = 'UCI0t9OsDta3rJwjN_GG3_Aw'
channel_link = f'https://www.youtube.com/user/{channel_name}'
# ensure_ascii=False
# api_key = 'AIzaSyCizgl_YfmTf75RIFvFS600FXZ1Aa6KxZI'
api_key = 'AIzaSyBNRpDvWwDK6qbBw4hwakmZW5GHtMHupPc'

youtube = build('youtube', 'v3', developerKey=api_key)

videosId = []


def getVideoList(maxresults=50, pagetoken=None):
    needed_date = (datetime.datetime.now() - datetime.timedelta(days=100)).isoformat('T') + 'Z'
    request = youtube.search().list(
        part='id',
        type='video',
        channelId=channel_id,
        publishedAfter=needed_date,
        order='date',
        maxResults=maxresults,
        pageToken=pagetoken  # pageToken='CAoQAA'
    )
    response = request.execute()  # json.loads(request.execute())
    return response


def getVideoIds(request):
    for video in request['items']:
        videosId.append(video['id']['videoId'])


def getVideosStatistic(full_video_ids):  # takes list with video ID`s
    start_id = 0
    stop_id = 50
    result = []

    for step in range(ceil(len(full_video_ids) / 50)):
        part_ids = full_video_ids[start_id:stop_id]
        part_ids = ','.join(part_ids)
        request = youtube.videos().list(
            part='statistics, snippet, contentDetails',
            id=part_ids,
        )
        result.append(request.execute())
        start_id += 50
        stop_id += 50
    return result


def start():
    all_videos = getVideoList()
    try:
        while all_videos['nextPageToken']:
            getVideoIds(all_videos)
            all_videos = getVideoList(pagetoken=all_videos['nextPageToken'])
    except Exception:
        getVideoIds(all_videos)


start()
statistic = getVideosStatistic(videosId)
statistic_json = json.dumps(statistic, ensure_ascii=False)

with open('test.txt', 'w') as file:
    file.write(statistic_json)


def show_result(text):
    result = []
    for x in text:
        for item in x['items']:
            video = {}
            video['title'] = item['snippet']['title']
            video['publishedAt'] = item["snippet"]["publishedAt"]
            video['viewsCount'] = item['statistics']['viewCount']
            video['likesCount'] = item['statistics']['likeCount']
            video['dislikesCount'] = item['statistics']['dislikeCount']
            video['link'] = f'https://www.youtube.com/watch?v={item["id"]}'
            result.append(video)
    return result


list_with_statistic = show_result(statistic)
with open('test.txt', 'w') as file:
    file.write(json.dumps(list_with_statistic, ensure_ascii=False))

import ipdb; ipdb.set_trace()