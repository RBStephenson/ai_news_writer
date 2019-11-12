class RSSNewsFeed(object):
    def __init__(self):
        self.news_feeds = []

    def add_item(self, news_feed, feed_name, category):
        self.news_feeds.append({"url": news_feed, "name": feed_name, "category": category})
