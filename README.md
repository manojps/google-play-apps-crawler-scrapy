# Google Play Crawler Using Scrapy; 1.1M+ Apps Crawled

The aim of this project was to build a database of all apps in Google Play. The project was tested on Google Play U.S. So far, I've **crawled 1,118,620 apps on Google Play (U.S. app store)**.

The data points collected are as follows.

1. app_id: App’s ID on Google Play 
2. item_name: Display name of app
3. updated: Date of last update
4. author: Name of publisher
5. filesize: File size of app
6. downloads: Download numbers for app
7. version: Version number of app
8. compatibility: Android version compatibility of app
9. content_rating: Maturity rating of content
10. author_link: Publisher website link and/or email address
11. genre: Category under which app is published
12. price: Price of app
13. rating_value: User rating value
14. review_number : Number of user reviews
15. description: App description
16. iap: In-app purchase available or not
17. developer_badge: Google Developer badge (if any)
18. physical_address: Contact information of publisher
19. video_url: Video preview URL
20. developer_id: Publisher portfolio link in Google Play

You can find more about the dataset at https://manojsaha.com/2015/12/24/google-play-apps-dataset/

I have used Scrapy 0.24.5 to crawl Google Play and PostgreSQL to store the data.

After the first iteration was done, I also ran some quick analysis on the data. You can read about my finding at 
https://manojsaha.com/2015/12/24/10-google-play-stats/


