# Google Play Crawler Using Scrapy; 1.1M+ Apps Crawled

The aim of this project was to build a database of all apps in Google Play. The project was tested on Google Play U.S. So far, I've crawled 1,118,620 apps on Google Play (U.S. app store).

The data points collected are as follows.

app_id: App’s ID on Google Play
item_name: Display name of app
updated: Date of last update
author: Name of publisher
filesize: File size of app
downloads: Download numbers for app
version: Version number of app
compatibility: Android version compatibility of app
content_rating: Maturity rating of content
author_link: Publisher website link and/or email address
genre: Category under which app is published
price: Price of app
rating_value: User rating value
review_number : Number of user reviews
description: App description
iap: In-app purchase available or not
developer_badge: Google Developer badge (if any)
physical_address: Contact information of publisher
video_url: Video preview URL
developer_id: Publisher portfolio link in Google Play

You can find more about the dataset at http://alo.ventures/google-play-apps-data-and-reviews-dataset/

I have used Scrapy 0.24.5 to crawl Google Play and PostgreSQL to store the data.

After the first iteration was done, I also ran some quick analysis on the data. You can read about my finding at 
http://alo.ventures/10-google-play-stats-you-should-know/


