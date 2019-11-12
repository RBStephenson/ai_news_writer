class RSSNewsFeed(object):
    def __init__(self):
        self.news_feeds = []

    def add_item(self, news_feed, feed_name, category):
        self.news_feeds.append({"url": news_feed, "name": feed_name, "category": category})

    def remove_item(self, url):
        # I'm not sure I like this method or not, which makes me think I need to
        # change the storage method too. I know that I want to eventually store
        # this in a database, so I might investigate that. Originally, I wanted
        # to use a pandas DataFrame so I could pass that to SQLAlchemy and
        # handle everything that way. I will settle for this right now, just to
        # keep it as simple as possible.
        self.news_feeds = [x for x in self.news_feeds if x['url'] != url]

    def update_item(self, key, url=None, name=None, category=None):
        # This method is a real kludge and I don't like it at all. I know that I could be doing something
        # much more efficient Python-wise, however, I don't know what that is right now. I also realize that
        # I still have a difficult time grasping list comprehensions, how they work and what they return.
        # I had originally had a list comprehension to return the `org_item` but it was not returning the
        # item I expected. I found the below `for` loop returns what I wanted so I could perform the update.
        org_item = None

        for item in iter(self.news_feeds):
            if item['url'] == key:
                org_item = item
                break

        self.remove_item(key)

        new_item = {"url": url, "name": name, "category": category}
        if new_item['url'] is None:
            new_item['url'] = org_item['url']

        if new_item['name'] is None:
            new_item['name'] = org_item['name']

        if new_item['category'] is None:
            new_item['category'] = org_item['category']

        self.news_feeds.append(new_item)

    def get_item(self, key):
        return [item for item in self.news_feeds if item['url'] == key][0]
