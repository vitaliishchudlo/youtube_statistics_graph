from datetime import datetime, timedelta

from youtubeAPI import searchVideosIdByChannelId


def get_list_id_videos(channel_id):
    date_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    date_end = date_now.replace(day=1) - timedelta(days=1)
    date_from = date_end.replace(day=1)
    # Adding the standard in time that requires YoutubeAPI
    date_from = date_from.isoformat('T') + 'Z'
    date_end = date_end.replace(hour=23, minute=59, second=59).isoformat('T') + 'Z'
    response = searchVideosIdByChannelId(channel_id, date_from, date_end)
    list_with_all_id_videos = []

    def extract_id_videos(text_for_extract):
        for video in text_for_extract['items']:
            list_with_all_id_videos.append(video['id']['videoId'])

    try:
        while response['nextPageToken']:
            extract_id_videos(response)
            response = searchVideosIdByChannelId(channel_id, date_from, date_end, page_token=response['nextPageToken'])
    except Exception:
        extract_id_videos(response)
    return list_with_all_id_videos


def get_formatted_data(unFormattedData):
    result = []
    for x in unFormattedData:
        for video in x['items']:
            videos_result = {}
            videos_result['title'] = video['snippet']['title']
            videos_result['publishedAt'] = video['snippet']['publishedAt']
            videos_result['viewCount'] = video['statistics']['viewCount']
            videos_result['likeCount'] = video['statistics']['likeCount']
            #videos_result['dislikeCount'] = video['statistics']['dislikeCount']
            videos_result['commentCount'] = video['statistics']['commentCount']
            videos_result['link'] = f'https://www.youtube.com/watch?v={video["id"]}'
            result.append(videos_result)
    return result
