#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ai_news_writer` package."""

import pytest

from ai_news_writer import ai_news_writer


@pytest.fixture
def ai_news_feeds():
    ai_feeds = ai_news_writer.ai_news_feeds
    return ai_feeds


@pytest.fixture
def parse_feed():
    feed = ai_news_writer.ai_news_feeds[0]
    return ai_news_writer.parse_feed(feed['name'], feed['url'])


def test_content(ai_news_feeds):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert len(ai_news_feeds) > 0


def test_feed_parse(parse_feed):
    print(parse_feed)
    assert parse_feed is None
