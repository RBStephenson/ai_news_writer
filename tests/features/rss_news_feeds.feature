# Created by brent at 11/1/2019

# This python module is going to be used in a Natural Language Processing application. Right now, I am planning
# on creating a Django front end for this application. The Django front-end will allow us to manage and maintain
# the RSS Feed collection we use to build our scripts and summaries as well as keep an archive all of the stories,
# articles, generated summaries, and scripts.

# This first set of tests is specifically for creating and maintaining our RSS feed collection. My idea is that
# I will use BDD (pytest-bdd) for development and feature design (see below tests). I am also following along
# With the pytest practices defined in https://www.obeythetestinggoat.com/ (great resource and I highly recommend it).

# As a content creator, I want to be able to find RSS News Feeds that are specifically about AI (and all related
# disciplines.

# Once I have found an RSS feed, I want to be able to add that to a collection of RSS feeds so that I can scrape
# articles from the feed.

# I will need to be able to store the RSS Feed's name, URL, and it's category (AI, Computer, Tech, etc).

# After adding an RSS Feed to the application, I will need to be able to edit the name, url and category and save
# those changes

# After adding an RSS Feed to the application, I may need to delete or remove the RSS Feed from the application's
# collection

# After adding an RSS Feed to the application, I may need to disable the feed without deleting it.

@rss @news_feeds
Feature: RSS News Feed List
    As a content creator,
    I want to be able to create a collection of RSS News Feeds
    So I can use them as source material for content generation

    Scenario:
        Given I am a content creator
        And I have an RSS news feed
        When I execute the save command
        Then I should not get an error
        And I should see the RSS news feed added to the RSS News Feed List

    Scenario:
        Given I am a content creator
        And I want to remove an RSS news feed
        When I select an RSS news feed
        And exceute the delete command
        Then I should not get an error
        And the RSS news feed should be removed from the RSS News Feed List

    Scenario:
        Given I am a content creator
        And I want to change information for an RSS News Feed
        When I select the RSS News feed from the list
        And supply updated information
        When I execute the update command
        Then I should not get an error
        And I should see the changes in the RSS News Feed List


