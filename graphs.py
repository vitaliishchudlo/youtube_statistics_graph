import datetime

import matplotlib.pyplot as plt


def show_statistic_graph(data, choice, channel_name, channel_id):
    date_now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    date_end = date_now.replace(day=1) - datetime.timedelta(days=1)
    date_from = datetime.datetime.strftime(date_end.replace(day=1), '%d-%m-%Y')
    date_end = datetime.datetime.strftime(date_end, '%d-%m-%Y')
    plt.title(
        f'TOP 10 videos on {choice[:-5] + "s"} in the period from {date_from} to {date_end}\n'
        f'YouTube channel name: {channel_name}')
    plt.xlabel('TOP places')
    plt.ylabel(f'Number of {choice[:-5] + "s"}')
    # змінити наступні значення типу str на тип int
    for dic in data:
        dic['viewCount'] = int(dic['viewCount'])
        dic['likeCount'] = int(dic['likeCount'])
        dic['dislikeCount'] = int(dic['dislikeCount'])
        dic['commentCount'] = int(dic['commentCount'])

    # Сортування словників в списку, за певним значенням(коменти, лайки, діз)
    def get_data(x):
        return x[f'{choice}']

    result = sorted(data, key=get_data, reverse=True)
    y_count = []
    for y in result[:10]:
        item = y[f'{choice}']
        y_count.append(item)
    legend_count = []
    for l in result[:10]:
        element = datetime.datetime.strftime(
            datetime.datetime.strptime(l['publishedAt'].replace('Z', '').replace('T', ' '), '%Y-%m-%d %H:%M:%S'),
            '%d-%m-%Y')
        legend_count.append(f'{element} | {l["title"]}')
    labels_top = ['Top10', 'Top9', 'Top8', 'Top7', 'Top6', 'Top5', 'Top4', 'Top3', 'Top2', 'Top1']
    y_count.reverse()
    for graph in range(len(result[:10])):
        plt.bar(labels_top.pop(), y_count.pop())
    plt.gca().ticklabel_format(axis='y', style='plain')
    plt.legend(legend_count)
    plt.grid()
    plt.show()
