from InstagramAPI import InstagramAPI
import time

#login info.
username="" #type your username here
password="" #type the password here
InstagramAPI = InstagramAPI(username,password)
InstagramAPI.login()

#base case to pull data of the user
InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
#print(result)

#get user ID
InstagramAPI.getProfileData()
user_id = InstagramAPI.LastJson['user']['pk']
print(user_id)



InstagramAPI.getUserFollowings(user_id)
print (len(InstagramAPI.LastJson['users']))
following=InstagramAPI.LastJson['users']
following_list=[]
for x in following:
    #print(x['username'])
    following_list.append(x['username'])


"""
#getting followers[version 1.0] - this doesnt print people after the "+" button when viewing followers in your insta app
InstagramAPI.getUserFollowers(user_id)
print (len(InstagramAPI.LastJson['users']))
followers_list=InstagramAPI.LastJson['users']
for x in followers_list:
    print(x['username'])
"""

followers = []
followers_list = []
next_max_id = True
while next_max_id:
    print(next_max_id)
    # first iteration hack
    if next_max_id == True: next_max_id = ''
    _ = InstagramAPI.getUserFollowers(user_id, maxid=next_max_id)
    followers.extend(InstagramAPI.LastJson.get('users', []))
    next_max_id = InstagramAPI.LastJson.get('next_max_id', '')
    time.sleep(1)

for x in  followers:
    #print(x['username'])
    followers_list.append(x['username'])



#now for the main selfish move, compare the two lists and get the followers who unfollowed you when you so dearly
#followed them. Don't show 'em love they don't need.

difference = list(set(followers_list) - set(following_list)) #switch places here to get the difference in the list you're looking for.
for x in difference:
    print(x)