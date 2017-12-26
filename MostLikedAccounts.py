# Analyzes all the media you've liked
# and returns the accounts whose media you've liked the most

from collections import Counter

from Login import login

login = login()

API = login[1]
user_id = login[0]
API.LastJson

usernames = []
for pic in API.getTotalLikedMedia(scan_rate=1):
    usernames.append(pic['user']['username'])

numlikes = Counter(usernames).most_common()
for user in numlikes:
    print(user[0]+": "+str(user[1]))