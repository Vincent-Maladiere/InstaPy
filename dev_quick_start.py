import numpy as np
import pandas as pd

from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(
    username='young_mamen', 
    password='871011tnecniv')


with smart_run(session):

    # profil lists, keywords, hashtags
    # TODO
    usernames = session.seed_users(n_users=3)

    # watch story of users (liking is not dev yet)
    # TODO: add like
    #session.set_do_story(enabled=True, percentage=70, simulate=False)

    # enable following
    session.set_do_follow(enabled=True, percentage=100, times=1)
    session.set_follow_skip_users(
        skip_non_business=True
    )

    # define specifics follow rules
    # TODO: add post frequency
    #session.set_relationship_bounds(
    #    enabled=True,
    #    max_followers=2500,
    #    delimit_by_numbers=True,
    #)

    # reduce sleep to improve speed
    session.set_sleep_reduce(30)

    # like last 4 pics of usernames
    session.set_do_like(enabled=True, percentage=100)
    #session.interact_by_users(usernames, amount=4, randomize=False)
    
    # like comments of usernames
    gaussian_max_comment = int(np.random.normal(50, 5))
    session.interact_by_comments(
        usernames,
        posts_amount=2,
        comments_per_post=gaussian_max_comment,
        interact=False,
        reply=False
    )

    # get people who commented
    session.extract_commenters(usernames, photos_amount=4, daysold=365)
    #session.follow_commenters(usernames, amount=20, daysold=365, max_pic = 100, sleep_delay=600, interact=False)

    # get people who likes? 
    # interact with likers of these usernames' posts
    # TO DEBUG?(stale)
    #user_liked_list = session.extract_likers(usernames, photos_amount=4, likes_per_post=50)

    # send dm to profils that have max 100 followers and post at least every other day 


#################################
########### TODO ################

# 6. Add telegram connecter
# 7. Add DMs w/ le bébé and a story likers


################################
########### END OF TODO ########



"""
GOAL:

(Once post online, bot generate interaction.)
    -> Only one session, if a bot run on a profile, the profile must not be visited.

Action
- profil lists, keywords, hashtags
    => generate a huge csv file
- visit profils
    - drop a fire or heart emoji on last story
    - like 5 last pictures
    - like comments on last post (max 50 comments on a given post, random is best)
    - visit commenters profil
        - like last 5 pics
    - visit likers profil
        - like last 5 pics
    - follow profils that have max 2500 followers and post at least every other day
- get list of all people interactions
- send dm to profils that have max 100 followers and post at least every other day 
- in a specified group chat, send a random sticker at given times
- report interacted profils that have a url in bio


"""