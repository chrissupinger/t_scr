# t_scr: A Twitter Scraping Solution

## Overview:
Simple program to recursively scrape public profiles on Twitter.

## Purpose:
Recently, it's become increasingly difficult to gain access to development APIs for social media platforms.  This program was quickly created to data mine corpora for the purpose of a computational linguistics project; additionally, it avoids the need for an account or access to a development API.

## Dependencies:
* Python:
  * Selenium
  * SQLAlchemy
* Other:
  * ChromeDriver and/or geckodriver

## Known Issues:
* 09.17.18 - Selenium: loss of element; observed between data captures in the range of 600 to 900
