import unittest

from ai_news_writer import rss_news_feed


class RSSNewsFeedsUnitTests(unittest.TestCase):
    def test_add_rss_news_feed(self):
        obj_under_test = rss_news_feed.RSSNewsFeed()
        obj_under_test.add_item('http://www.mynewsfeed.com', 'My News Feed', 'Test Category')
        self.assertTrue(obj_under_test.news_feeds[0]['url'] == 'http://www.mynewsfeed.com')
        print(obj_under_test.news_feeds)

    def test_update_rss_news_feed(self):
        obj_under_test = rss_news_feed.RSSNewsFeed()
        obj_under_test.add_item('http://www.mynewsfeed.com', 'My News Feed', 'Test Category')
        obj_under_test.update_item(key='http://www.mynewsfeed.com', url='http://www.mynewsfeed2.com')
        self.assertTrue(obj_under_test.news_feeds[0]['url'] != 'http://www.mynewsfeed.com')
        self.assertTrue(obj_under_test.news_feeds[0]['url'] == 'http://www.mynewsfeed2.com')
        print(obj_under_test.news_feeds)

    def test_delete_rss_news_feed(self):
        obj_under_test = rss_news_feed.RSSNewsFeed()
        obj_under_test.add_item('http://www.mynewsfeed.com', 'My News Feed', 'Test Category')
        self.assertTrue(obj_under_test.news_feeds[0]['url'] == 'http://www.mynewsfeed.com')
        obj_under_test.remove_item('http://www.mynewsfeed.com')
        self.assertTrue(len(obj_under_test.news_feeds) == 0)
        print(obj_under_test.news_feeds)

    def test_get_rss_news_feed_collection(self):
        obj_under_test = rss_news_feed.RSSNewsFeed()
        obj_under_test.add_item('http://www.mynewsfeed.com', 'My News Feed', 'Test Category')
        obj_under_test.add_item('http://www.notmynewsfeed.com', 'Not My News Feed', 'Test Category')
        obj_under_test.add_item('http://www.anothernewsfeed.com', 'Another News Feed', 'Test Category')

        expected_item = obj_under_test.news_feeds[1]
        actual_item = obj_under_test.get_item('http://www.notmynewsfeed.com')

        self.assertEqual(expected_item, actual_item)


if __name__ == '__main__':
    unittest.main()
