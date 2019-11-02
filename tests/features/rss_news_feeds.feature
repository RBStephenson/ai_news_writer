# Created by brent at 11/1/2019
Feature: RSS News Feeds Collection
    As a content creator and an NLP enthusiast,
    I want to be able to collect RSS news feeds about a specific topic/category
    and save those to a collection/database
    so that I can gather timely and relevant news on a given topic

    Scenario Outline: Add RSS Feed URL
        Given I have entered a <url>
        And I have entered a <feed_name>
        And I have entered a <category>
        When I click on the save button
        Then the RSS news feed is added to the collection
        Examples:
            | feed_name     | url                                                                         | category |
            | AI Trends     | https://www.aitrends.com/feed/                                              | AI       |
            | Science Daily | https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml | AI       |

    Scenario Outline: Update an RSS Feed
        Given I have an existing RSS Feed <feed_name>
        And I have an existing <url>
        And I have an existing <category>
        When I change existing data
        And I click on the edit button
        Then I should be able to update the <feed_name>
        And I should be able to update the <url>
        And I should be able to update the <category>
        Examples:
            | feed_name     | url                                                                         | category |
            | AI Trends     | https://www.aitrends.com/feed/                                              | AI       |
            | Science Daily | https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml | AI       |

    Scenario Outline: Remove an RSS Feed from the Collection
        Given I have a collection of RSS Feeds
        And I want to remove a feed from the collection
        When I select the feed
        And Click on the delete button
        Then the RSS Feed <feed_name>
        And the RSS Feed <url>
        And the RSS Feed <category> should be removed from the collection
        Examples:
            | feed_name     | url                                                                         | category |
            | AI Trends     | https://www.aitrends.com/feed/                                              | AI       |
            | Science Daily | https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml | AI       |
