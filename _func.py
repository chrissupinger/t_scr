import datetime, time, sys

from _db import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.setrecursionlimit(100000)

_db = create_engine('sqlite:///_db.db', echo = False)
_Session = sessionmaker(bind = _db)
_session = _Session()

# _dr = webdriver.Firefox()

_opt = webdriver.ChromeOptions()
_opt.add_argument('headless')
_dr = webdriver.Chrome(chrome_options = _opt)

def get_count(origin):

    _dr.get("https://twitter.com/" + origin)
    time.sleep(2)
    _data_count = _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span[3]')
    _count = _data_count.get_attribute('data-count')
    print('This profile has {} items that can be retrieved.'.format(int(_count)))

def get_page(origin, start, end):

    _dr.get("https://twitter.com/" + origin)
    time.sleep(2)
    t_scrape(origin, start, end)

def t_scrape(origin, start, end):

    _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

    [_get_content, _get_timestamp, _get_tweet] = [
        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]' % start)]

    _get_timestamp = _get_timestamp.get_attribute('data-time')

    try:
        [_get_reply, _get_retweet, _get_favorite] = [
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[1]/span[1]/span' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[1]/span[2]/span' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[1]/span[3]/span' % start)
        ]
    except:
        try:
            [_get_reply, _get_retweet, _get_favorite] = [
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[1]/span[1]/span' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[1]/span[2]/span' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[1]/span[3]/span' % start)
            ]
        except:
            try:
                [_get_reply, _get_retweet, _get_favorite] = [
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[1]/span[1]/span' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[1]/span[2]/span' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[1]/span[3]/span' % start)
                ]
            except:
                try:
                    [_get_reply, _get_retweet, _get_favorite] = [
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[6]/div[1]/span[1]/span' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[6]/div[1]/span[2]/span' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[6]/div[1]/span[3]/span' % start)
                    ]
                except:
                    print('Error processing Tweet.')                    
                    _dr.close()
                    _dr.quit()
                    quit()

    [_id, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite] = [
        _get_content.get_attribute('data-item-id'),
        _get_content.get_attribute('data-name'),
        _get_content.get_attribute('data-screen-name'),
        datetime.datetime.strptime(time.ctime(int(_get_timestamp)), '%a %b %d %H:%M:%S %Y'),
        _get_tweet.find_element_by_class_name('js-tweet-text-container').text,
        _get_reply.get_attribute('data-tweet-stat-count'),
        _get_retweet.get_attribute('data-tweet-stat-count'),
        _get_favorite.get_attribute('data-tweet-stat-count')
    ]


    _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
    _session.add(_record)
    _session.commit()
    print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
    time.sleep(1.25)

    if start < end:

        t_scrape(origin, start + 1, end)

    else:

        _dr.close()
        _dr.quit()
