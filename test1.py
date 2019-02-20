from bs4 import BeautifulSoup
from excel_create import *
from authh import *
from userr_info import *
from sorting_algo import *
import time
data = api.rate_limit_status()


def loll(user_id,i):
    total_id_1=[]
    user_info(user_id,i)
    total_id=follower_following_id(user_id)
    total_id_1=total_id_1+total_id
    total_id_1=remove_duplicate(total_id_1)
i=1
user=api.get_user('SohelMomin19')
loll(user.id,i)
i=i+1

user=api.get_user('XiaomiIndia')
loll(user.id,i)
i=i+1
user=api.get_user('Apple')
loll(user.id,i)
i=i+1
user=api.get_user('NanduMayur')
loll(user.id,i)
i=i+1
user=api.get_user('arstechnica')
loll(user.id,i)
i=i+1
user=api.get_user('HyundaiIndia')
loll(user.id,i)
i=i+1
user=api.get_user('cricbuzz')
loll(user.id,i)
i=i+1

##user = api.get_user(user_id)
##print(user)



