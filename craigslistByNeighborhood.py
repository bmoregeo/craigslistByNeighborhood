import requests
from models import CraigslistPosts

if __name__ == '__main__':
    cp = CraigslistPosts('seattle', 1800, 2, True)
    posts = cp.get()
    print len(posts)