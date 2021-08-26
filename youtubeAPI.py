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


#
# def getAllVideosByPeriod():
#    request = youtube.search().list(
#        part='id',
#        type='video',
#        channelId=channel_id,
#        publishedAfter=needed_date,
#        order='date',
#        maxResults=maxresults,
#        pageToken=pagetoken  # pageToken='CAoQAA'
#    )
