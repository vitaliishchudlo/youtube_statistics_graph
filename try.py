import matplotlib.pyplot as plt

# data_list = [
#     {
#         "title": "Украина — Англия. Обзор матча / Прыгнуть выше головы не смогли",
#         "viewsCount": "132870",
#     },
#     {
#         "title": "Львів - шахтар. Виїздна серія",
#         "viewsCount": "41242",
#     },
#     {
#         "title": "Залужани - Барселона. Рік два. Студія після матчу",
#         "viewsCount": "341516",
#     }
# ]

# x = [
#     'Львів - шахтар. Виїздна серія',
#     'Украина — Англия. Обзор матча / Прыгнуть выше головы не смогли',
#     'Залужани - Барселона. Рік два. Студія після матчу'
# ]
# y = [1323, 5142, 2681]


plt.title("ТОП 10 відео по переглядам (в період 1-31липня)", fontsize=14, fontweight='bold', color='red')
plt.xlabel('X labels')
plt.ylabel('Y labels')

label_x = 'Львів - шахтар. Виїздна серія'
label_x1 = 'Залужани - Барселона. Рік два. Студія після матчу'
label_x2 = 'Львів - шахтар. Виїздна серія. Студія після матчу.'
label_x3 = 'Украина — Англия. Обзор матча / Прыгнуть выше головы не смогли'
label_x4 = 'Верес - Минай. Матч за шесть очков. Студия'
label_x5 = 'Ингулец – Динамо. Дать бой чемпиону. Студия после матча'
label_x6 = 'Мариуполь - Черноморец. «Морское дерби». Студия'
label_x7 = 'Боруссия Д – Айнтрахт. Обзор матча / Дубль и три ассиста Холанда'
label_x8 = 'Десна - Днепр-1. Продолжить победную серию. Студия после матча'
label_x9 = 'Колос - Рух. Реабилитация за еврокубки. Студия'

x = 'Top 1'
x1 = 'Top 2'
x2 = 'Top 3'
x3 = 'Top 4'
x4 = 'Top 5'
x5 = 'Top 6'
x6 = 'Top 7'
x7 = 'Top 8'
x8 = 'Top 9'
x9 = 'Top 10'

y = 18513
y1 = 17000
y2 = 16000
y3 = 15314
y4 = 12515
y5 = 12500
y6 = 10331
y7 = 7681
y8 = 5350
y9 = 4999
# 'indigo', 'purple', 'darkder', 'peru', 'navy', 'lime


plt.bar(x, y, color='red')
plt.bar(x1, y1, color='blue')
plt.bar(x2, y2, color='orange')
plt.bar(x3, y3, color='yellow')
plt.bar(x4, y4, color='darkred')
plt.bar(x5, y5, color='black')
plt.bar(x6, y6, color='magenta')
plt.bar(x7, y7, color='cyan')
plt.bar(x8, y8, color='black')
plt.bar(x9, y9, color='green')

plt.legend([label_x, label_x1, label_x2, label_x3, label_x4, label_x5, label_x6, label_x7, label_x8, label_x9])
# plt.grid()
# plt.show()


data_list = [
    {
        "title": "пятый",
        "viewsCount": "102",
        "likesCount": "10",
    },
    {
        "title": "третий",
        "viewsCount": "733",
        "likesCount": "50",
    },
    {
        "title": "первый",
        "viewsCount": "1000",
        "likesCount": "20",
    },
    {
        "title": "четвертый",
        "viewsCount": "345",
        "likesCount": "30",
    },
    {
        "title": "второй",
        "viewsCount": "951",
        "likesCount": "1",
    }
]

for dic in data_list:
    dic['viewsCount'] = int(dic['viewsCount'])
    dic['likesCount'] = int(dic['likesCount'])





def get_data(x):
    return x['viewsCount']

result = sorted(data_list, key=get_data, reverse=True)

#more_viewed = sorted(data_list, key=itemgetter('viewsCount'))
import ipdb;ipdb.set_trace()
