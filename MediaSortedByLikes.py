#Sorts instagram page's media by number of likes

from Login import login
from operator import itemgetter

login = login()
API = login[1]

user_name = ''
API.searchUsername(user_name)
username_id = API.LastJson["user"]["pk"]

media_list = API.getTotalUserFeed(username_id, minTimestamp = None)

custom_list = []

for item in media_list:
    custom_list.append([item['like_count'],item['id'], item['caption']])

sorted_list = sorted(custom_list, key=itemgetter(0), reverse=True)

for item in sorted_list:
    print(item)