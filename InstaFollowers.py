#Determines which accounts you are following that are not following you back
#and allows you to unfollow them right from the Python Terminal

from Login import login

login = login()

API = login[1]
user_id = login[0]

API.getUsernameInfo(user_id)
API.LastJson
following = []
followers = []
next_max_id = True
while next_max_id:
    if next_max_id == True: next_max_id=''
    _ = API.getUserFollowings(user_id,maxid=next_max_id)
    following.extend(API.LastJson.get('users', []))
    _ = API.getUserFollowers(user_id,maxid=next_max_id)
    followers.extend(API.LastJson.get('users',[]))
    next_max_id = API.LastJson.get('next_max_id', '')

users_following = []
for user in following:
    user_info = [user['username'],user['pk']]
    users_following.append(user_info)

users_followers = []
for user in followers:
    user_info = [user['username'],user['pk']]
    users_followers.append(user_info)

not_follow_back = []
for user in users_following:
    if user not in users_followers:
        not_follow_back.append(user)
print('Users not following you back:')
for user in not_follow_back:
    print(user[0])

user_unfollow = ""
while user_unfollow != "No":
    user_unfollow = str(input("\nUnfollow a user who doesn't follow you? Enter username or type 'No' to stop: "))
    for user in not_follow_back:
        if user_unfollow == user[0]:
            API.unfollow(user[1])



