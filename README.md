# t_scr: A Twitter Scraping Solution

## Purpose
Recently, it's become increasingly difficult to gain access to development APIs for social media platforms.  This program was quickly created to data mine corpora for the purpose of a computational linguistics project; additionally, it avoids the need for an account or access to a development API.  It's solely concerned with publicly available text data.

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
* 09.18.18 - *\_func.py*: slightly modified to handle more variations in Twitter page structures
* 09.17.18 - *\_func.py*: added greater flexibility for scanning variations in Twitter page structures; also added the ability to capture the number of replies, retweets and favorites

## Known/Working Issues
* [ ] 09.17.18 - Selenium: loss of reference element observed between data captures in the range of 400 to 900; due to dynamic page structures
* [ ] 09.17.18 - ChromeDriver: process persistence following program exception
* [ ] 09.17.18 - fake-useragent: incorporate functionality
* [ ] 09.17.18 - *\_func.py*: code redundancy
