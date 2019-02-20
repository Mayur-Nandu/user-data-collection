from excel_create import *
from authh import *

def user_info(user_id,i):
    user = api.get_user(user_id)
    user_sheet.write(i,0,user.id)
    user_sheet.write(i,1,user.screen_name)
    user_sheet.write(i,2,user.friends_count)
    user_sheet.write(i,3,user.followers_count)
    user_sheet.write(i,4,user.favourites_count)
    user_sheet.write(i,5,user.statuses_count) #No. of tweets
##    user_sheet.write(i,6,user.retweet_count)
    user_sheet.write(i,6,user.created_at)#age of twitter account
    '''
    #string manipulation 
    age_of_acc_s=str(age_of_acc)
    date = datetime.datetime.strptime(age_of_acc_s,"%Y-%m-%d %S:%M:%H")
    print(date.year,date.month,date.day)
    print(type(date.year)
    '''
    user_sheet.write(i,7,user.location)
    user_sheet.write(i,8,user.description)
    user_sheet.write(i,9,user.verified) #user verified or not
    user_sheet.write(i,10,user.protected)
    wb.save('user_db2.xls')
    
def follower_following_id(user_id):
    user = api.get_user(user_id)
    ids=[]
    #no of friends/following
    for page in tweepy.Cursor(api.friends_ids, screen_name=user.screen_name).pages():
        ids.extend(page)
    idss=[]
    #no of follower
    for page in tweepy.Cursor(api.followers_ids, screen_name=user.screen_name).pages():
        idss.extend(page)
    total_id = ids + idss
    total_id.sort()
    return total_id
        
