import os

import requests

from data_processing import get_list_id_videos, get_formatted_data
from graphs import show_statistic_graph
from youtubeAPI import getChannelId, getVideosStatistic, getChannelNameByChannelId


def app(channel_name, channel_id):
    list_of_videos_id = get_list_id_videos(channel_id)
    list_of_videos_statistic = getVideosStatistic(list_of_videos_id)
    formatted_data_for_graphs = get_formatted_data(list_of_videos_statistic)

    def menu_graphs():
        try:
            menu_choice = int(input('\n1 - Views\n2 - Likes\n3 - Comments\n4 - Exit\n> '))

            if menu_choice == 1:
                menu_choice = 'viewCount'
                show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
                menu_graphs()
            elif menu_choice == 2:
                menu_choice = 'likeCount'
                show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
                menu_graphs()
            elif menu_choice == 3:
                menu_choice = 'commentCount'
                show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
                menu_graphs()
            elif menu_choice == 4 or menu_choice == 'exit' or menu_choice == 'Exit':
                os.system('exit')
            else:
                print('Try to enter the correct value\n\n\n')
        except Exception:
            menu_graphs()
    menu_graphs()


def get_user_input():
    user_input = input(
        '\nEnter the ID or NAME or LINK on your YouTube channel from which you want to visualize statistics.\n'
        'You can press "Enter" to apply the default YouTube channel - DudeGang\n> ')
    if len(user_input) == 0:
        user_input = 'https://www.youtube.com/channel/UC6NmCNbRV8pwEwpcsUNpWhw'
    return user_input


def get_channel_id_from_channel_page(channel_link):
    try:
        response = requests.get(channel_link).text
        link_start = response.find('href="https://www.youtube.com/channel/')
        channel_url = response[link_start:link_start + 100].split('"')[1]
        channel_id = channel_url.split('/')[-1]
        return channel_id
    except Exception:
        return False


def process_user_input(user_input):
    if 'https://www.youtube.com/channel/' in user_input:
        channel_id = user_input.split('/')[-1]
        return channel_id

    if 'https://www.youtube.com/c/' in user_input:
        channel_id = get_channel_id_from_channel_page(user_input)
        if channel_id: return channel_id


    if 'https://www.youtube.com/' in user_input:
        channel_id = get_channel_id_from_channel_page(user_input)
        if channel_id: return channel_id

    channel_id = getChannelId(user_input)
    if channel_id: return channel_id

    channel_id = getChannelId(user_input, id=True)
    if channel_id: return channel_id

    target_link = 'https://www.youtube.com/c/' + user_input
    channel_id = get_channel_id_from_channel_page(target_link)
    if channel_id: return channel_id

    return False


def start():
    user_input = get_user_input()
    channel_id = process_user_input(user_input)
    if not channel_id:
        print('Error. Can`t find this youtube channel.\n')
        start()
    channel_name = getChannelNameByChannelId(channel_id)
    if not channel_name:
        channel_name = 'Error404'
    app(channel_name, channel_id)


if __name__ == '__main__':
    start()
