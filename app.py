from youtubeAPI import getChannelId, searchVideosIdByIdChannel
from data_processing import get_list_id_videos

def get_youtube_channel_name():
    channel_name = input('Enter the name of the Youtube channel from which you want to get info.\n'
                         'Or PRESS ENTER to choose the default - "FootballTVUA"\n> ')
    if len(channel_name) == 0:
        channel_name = 'FootballTVUA'
    return channel_name


def app(channel_name, channel_id):
    list_of_id_videos = get_list_id_videos(channel_id)




def start():
    channel_name = get_youtube_channel_name()
    channel_id = getChannelId(channel_name)
    if not channel_id:
        print('Error. Can`t find this youtube channel.\n')
        start()
    else:
        app(channel_name, channel_id)


if __name__ == '__main__':
    start()
