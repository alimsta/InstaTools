# Creates a matplotlib graph of your account's likes per post over time
# Also returns list of posts sorted by number of likes

import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from pandas import DataFrame

from Login import login

login = login()

API = login[1]
user_id = login[0]

user_media = API.getTotalUserFeed(user_id)

likesnum = []
image_date = []
image_info = []
for image in user_media:
    likesnum.append(image['like_count'])
    image_date.append(mdates.date2num
                      (dt.datetime.fromtimestamp(image['device_timestamp'])))
    image_info.append([image['caption']['text'],
                       dt.datetime.fromtimestamp(image['device_timestamp']).strftime('%m-%d-%Y'),
                       image['like_count']])

likesnum.reverse() #switches order from (most recent to least) to (least recent to most)
image_date.reverse()

image_info.sort(key=lambda x: x[2], reverse=True) #sort list by number of likes, descending order

print(DataFrame(image_info))

with plt.style.context(('dark_background')):
    plt.plot(image_date,likesnum)
    plt.ylabel("Number of Likes")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.xlabel('Date')

    plt.title('Trend in Likes/Post')
    plt.show()

