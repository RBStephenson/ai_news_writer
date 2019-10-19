# -*- coding: utf-8 -*-

"""Main module."""

ai_news_feeds = [
    {"name": "AI Trends", "url": "https://www.aitrends.com/feed/"},
    {"name": "Science Daily", "url": "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml"},
    {"name": "MIT News - Artificial Intelligence", "url": "http://news.mit.edu/rss/topic/artificial-intelligence2"},
    {"name": "r/artificial", "url": "https://www.reddit.com/r/artificial/.rss"},
    {"name": "Chatbots Magazine - Medium", "url": "https://chatbotsmagazine.com/feed"},
    {"name": "Towards Data Science - Medium", "url": "https://towardsdatascience.com/feed"},
    {"name": "Chatbots Life - Medium", "url": "https://chatbotslife.com/feed"},
    {"name": "AWS Machine Learning Blog", "url": "https://aws.amazon.com/blogs/machine-learning/feed/"},
    {"name": "Artificial Intelligence - IBM Developer",
     "url": "https://developer.ibm.com/patterns/category/artificial-intelligence/feed/"},
    {"name": "Lex Fridman - Artificial Intelligence (AI)", "url": "https://lexfridman.com/category/ai/feed/"},
    {"name": "r/singularity", "url": "https://www.reddit.com/r/singularity/.rss?format=xml"},
    {"name": "Archie.AI - Medium", "url": "https://medium.com/feed/archieai"},
    {"name": "The Official NVIDIA Blog", "url": "http://feeds.feedburner.com/nvidiablog"},
    {"name": "OpenAI Blog", "url": "https://openai.com/blog/rss/"},
    {"name": "VentureBeat", "url": "http://feeds.feedburner.com/venturebeat/SZYF?format=xml"},
]

import feedparser


def parse_feed(name, url):
    output = feedparser.parse(url_file_stream_or_string=url)
    print(output)
