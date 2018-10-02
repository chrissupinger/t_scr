# t_scr: A Twitter Scraping Solution

## Purpose
Recently, it's become increasingly difficult to gain access to development APIs for social media platforms.  This program was quickly created to data mine corpora for the purpose of a computational linguistics project; additionally, it avoids the need for an account or access to a development API.  It's solely concerned with publicly available text data.

## Function
This program specifically targets public profiles and doesn't require a Twitter account to operate.  It's particularly concerned with the following: tweet ID, username, full name, timestamp and tweet.  Additionaly, it captures numerical data associated with each tweet that includes: the number of replies, retweets and how many times it has been favorited.

## Dependencies
* Python:
  * [Selenium](https://selenium-python.readthedocs.io)
  * [SQLAlchemy](http://www.sqlalchemy.org)
* Other:
  * [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and/or [geckodriver](https://github.com/mozilla/geckodriver/releases)
* Suggested:
  * [fake-useragent](https://github.com/hellysmile/fake-useragent)
  * [VPN](https://www.cnet.com/best-vpn-services-directory/)

## Notes
* ChromeDriver is great for running headless environments

## Updates
* 10.02.18 - *\_func.py*: modified to moderately condense structure
* 09.19.18 - *\_func.py*: modified to eliminate some code redundancy; additional modifications needed
* 09.18.18 - *\_func.py*: slightly modified to handle more variations in Twitter page structures
* 09.17.18 - *\_func.py*: added greater flexibility for scanning variations in Twitter page structures; also added the ability to capture the number of replies, retweets and favorites

## Known/Working Issues
* [ ] 09.22.18 - Selenium: loss of reference element observed between data captures in the range of ~~400~~ 800 to 900; due to dynamic page structures
* [ ] 09.18.18 - *\_prog.py*: linearize program initiation and set boundaries to avoid anomalies
* [ ] 09.17.18 - ChromeDriver: process persistence following program exception
* [ ] 09.17.18 - fake-useragent: incorporate functionality
* [ ] 09.17.18 - *\_func.py*: code redundancy
