import  tweepy as tw
import  os.path
import  numpy
from    numpy  import genfromtxt
import  sys

class TwitterAPI():
    def __init__(self):
        self.consumer_key           = ''
        self.consumer_secret        = ''
        self.access_token           = ''
        self.access_token_secret    = ''

        self.auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tw.API(self.auth)

    # Fetch me
    def me(self):
        return self.api.me().id

    # Fetch every followers from a user
    def get_followers(self, user):
        return self.api.followers_ids(user)

    # Follow a user
    def follow(self, user):
        return self.api.create_friendship(user)

    # Unfollow a user
    def unfollow(self, user):
        return self.api.destroy_friendship(user)

if __name__ == '__main__':
    t = TwitterAPI()

    # It's you
    me = t.me()

    if len(sys.argv) > 1:

        # The user you want to fetch every followers
        user = sys.argv[1]
        file = user + '_followers_ids'

        # Unfollow if necessay
        if os.path.exists(file):
            followers = genfromtxt(file, dtype=None, delimiter=',')
            for n in followers:
                t.unfollow(n)
            os.remove(file)
            sys.exit('You\'ve unfollowed every followers of '+ user)

        # Every followers...
        followers = t.get_followers(user)
        numpy.savetxt(file, followers, fmt='%s', delimiter=',')

        # Follow every users if it's not you
        for n in followers:
            if n != me:
                t.follow(n)
        print('You are now following every followers of '+ user)
    else:
        print('Provide a user please')
