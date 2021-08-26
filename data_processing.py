from datetime import datetime, timedelta

from youtubeAPI import searchVideosIdByIdChannel


def extract_id_videos(text_for_extract):
    result = []
    for video in text_for_extract['items']:
        result.append(video['id']['videoId'])
    return result


def get_list_id_videos(channel_id):
    date_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    date_end = date_now.replace(day=1) - timedelta(days=1)
    date_from = date_end.replace(day=1)
    # Adding the standard in time that requires YoutubeAPI
    date_from = date_from.isoformat('T') + 'Z'
    date_end = date_end.isoformat('T') + 'Z'
    response = searchVideosIdByIdChannel(channel_id, date_from, date_end)
    list_with_all_id_videos = []
    try:
        while response['nextPageToken']:
            list_with_part_id_videos = extract_id_videos(response)
            list_with_all_id_videos += list_with_part_id_videos
            response = searchVideosIdByIdChannel(channel_id, date_from, date_end, page_token=response['nextPageToken'])
    except Exception:
        list_with_part_id_videos = extract_id_videos(response)
        list_with_all_id_videos += list_with_part_id_videos
    return list_with_all_id_videos
