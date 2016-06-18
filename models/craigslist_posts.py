import requests
from post import Post


class CraigslistPosts(object):
    def __init__(self, city, max_price, bedrooms, dogs=False):
        self.city = city
        self.max_price = max_price
        self.bedrooms = bedrooms
        self.dogs = dogs

    @property
    def url(self):
        return 'http://{}.craigslist.org/jsonsearch/apa/?max_price={}&bedrooms={}&pets_dog={}'.format(self.city,
                                                                                                      self.max_price,
                                                                                                      self.bedrooms,
                                                                                                      int(self.dogs))

    def get(self):
        response = requests.get(self.url)
        data = response.json()

        posts = []
        i = 0

        for record in data[0]:
            if 'GeoCluster' in record.keys():
                cluster_response = requests.get('http://{}.craigslist.org{}'.format(self.city, record['url']))

                for post in cluster_response.json()[0]:
                    posts.append(Post(post['PostingID'],
                                  post['PostingTitle'],
                                  post['Ask'],
                                  post['Bedrooms'],
                                  post['PostingURL'],
                                  post['Longitude'],
                                  post['Latitude'],
                                  post['PostedDate']
                                  ))

                    i+=1
                    print i
            else:
                posts.append(Post(record['PostingID'],
                                  record['PostingTitle'],
                                  record['Ask'],
                                  record['Bedrooms'],
                                  record['PostingURL'],
                                  record['Longitude'],
                                  record['Latitude'],
                                  record['PostedDate']
                                  ))
                i+=1
                print i
        return posts
