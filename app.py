from config import API_KEY

def start():
    channel_name = input('Enter the name of the channel from which you want to get information\n'
                   'Or PRESS ENTER to choose the default - FootballTVUA\n> ')
    if len(channel_name) == 0:
        choice = 'FootballTVUA'
    print(API_KEY)





if __name__ == '__main__':
    start()