from instapy import InstaPy #pip install instapy
insta_username = "thisisinstatestaccount"
insta_password = "thisisinstatestaccount"

session = InstaPy(username = insta_username, password = insta_password)


session.login()

session.like_by_users(["viitpune"], amount =1)
session.follow_by_list(["viitpune"], times =1)

session.end()