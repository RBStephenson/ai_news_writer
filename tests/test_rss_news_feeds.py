import unittest

from ai_news_writer import rss_news_feed


class RSSNewsFeedsUnitTests(unittest.TestCase):
    def test_add_rss_news_feed(self):
        obj_under_test = rss_news_feed.RSSNewsFeed()
        obj_under_test.add_item('http://www.mynewsfeed.com', 'My News Feed', 'Test Category')
        self.assertTrue(obj_under_test.news_feeds[0]['url'] == 'http://www.mynewsfeed.com')

    def test_update_rss_news_feed(self):
        pass

    def test_delete_rss_news_feed(self):
        pass

    def test_get_rss_news_feed_collection(self):
        pass


if __name__ == '__main__':
    unittest.main()
