#Simplified Login function

from Dependencies.InstagramAPI import InstagramAPI

def login():
    def login_account():
        username = ''#str(input("Enter username: "))
        pwd = ''#str(input("Enter password: "))
        #Can use this link to find UserID: https://smashballoon.com/instagram-feed/find-instagram-user-id/
        user_id = #int(input("Enter User ID: "))
        API = InstagramAPI(username,pwd)
        return [API.login(force=False), user_id, API]

    login_success = login_account()
    cont = ''
    while login_success[0] == None and cont != 'no':
        cont = str(input("Incorrect user info. Type 'yes' to re-enter info or type 'no' to exit: "))
        if cont == 'yes':
            login_success = login_account()
    return [login_success[1],login_success[2]]
