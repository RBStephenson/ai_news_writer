from pytest_bdd import given, when, then, scenarios

scenarios("../features/rss_news_feeds.feature")


@given("I have entered a <url>")
def step_impl(url):
    raise NotImplementedError(u'STEP: Given I have entered a <url>')


@when("I click on the save button")
def step_impl():
    raise NotImplementedError(u'STEP: When I click on the save button')


@then("the RSS news feed is added to the collection")
def step_impl():
    raise NotImplementedError(u'STEP: Then the RSS news feed is added to the collection')


@given("I have an existing RSS Feed <feed_name>")
def step_impl(feed_name):
    raise NotImplementedError(u'STEP: Given I have an existing RSS Feed <feed_name>')


@given("I have an existing <url>")
def step_impl(url):
    raise NotImplementedError(u'STEP: And I have an existing <url>')


@when("I change existing data")
def step_impl():
    raise NotImplementedError(u'STEP: When I change existing data')


@given("I click on the edit button")
def step_impl():
    raise NotImplementedError(u'STEP: And I click on the edit button')


@then("I should be able to update the <feed_name>")
def step_impl(feed_name):
    raise NotImplementedError(u'STEP: Then I should be able to update the <feed_name>')


@given("I have a collection of RSS Feeds")
def step_impl():
    raise NotImplementedError(u'STEP: Given I have a collection of RSS Feeds')


@given("I want to remove a feed from the collection")
def step_impl():
    raise NotImplementedError(u'STEP: And I want to remove a feed from the collection')


@when("I select the feed")
def step_impl():
    raise NotImplementedError(u'STEP: When I select the feed')


@given("Click on the delete button")
def step_impl():
    raise NotImplementedError(u'STEP: And Click on the delete button')


@then("the RSS Feed <feed_name>")
def step_impl(feed_name):
    raise NotImplementedError(u'STEP: Then the RSS Feed <feed_name>')
