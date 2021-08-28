import datetime

import matplotlib.pyplot as plt


# , fontsize=14, fontweight='bold', color='red'

def show_statistic_graph(data, choice):
    if choice == 1:
        choice = 'viewCount'
    elif choice == 2:
        choice = 'likeCount'
    else:
        choice = 'commentCount'

    plt.title(f'TOP 10 videos by {choice}')
    plt.xlabel('TOP places')
    plt.ylabel(f'Number')

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
    plt.legend(legend_count)
    plt.grid()
    plt.show()
