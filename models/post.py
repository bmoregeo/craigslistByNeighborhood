class Post(object):
    def __init__(self, post_id, title, asking_price, bedrooms, url, lon, lat, date):
        self.id = post_id
        self.url = url
        self.lon = lon
        self.lat = lat
        self.date = date
        self.asking_price = asking_price
        self.title = title
        self.bedrooms = bedrooms

    @property
    def coordinate(self):
        return self.lon, self.lat

