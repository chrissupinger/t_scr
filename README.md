# t_scr: A Twitter Scraping Solution

## Purpose
Recently, it's become increasingly difficult to gain access to development APIs for social media platforms.  This program was quickly created to data mine corpora for the purpose of a computational linguistics project; additionally, it avoids the need for an account or access to a development API.  It's solely concerned with text data.

## Dependencies
* Python:
  * [Selenium](https://selenium-python.readthedocs.io)
  * [SQLAlchemy](http://www.sqlalchemy.org)
* Other:
  * [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and/or [geckodriver](https://github.com/mozilla/geckodriver/releases)
* Suggested:
  * [fake-useragent](https://github.com/hellysmile/fake-useragent)
  * VPN

## Notes
* ChromeDriver is great for running headless environments

## Working
* [ ] Looking to further tune the program to run in conjuction with fake-useragent

## Known Issues
* 09.17.18 - Selenium: loss of element; observed between data captures in the range of 600 to 900
