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

def get_page(origin, start, end):

    _dr.get("https://twitter.com/" + origin)
    time.sleep(2)
    t_scrape(origin, start, end)

def get_count(origin):

    _dr.get("https://twitter.com/" + origin)
    time.sleep(2)
    _data_count = _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span[3]')
    _count = _data_count.get_attribute('data-count')
    print('This profile has {} items that can be retrieved.'.format(int(_count)))

def t_scrape(origin, start, end):

    try:

        [_get_id, _get_timestamp, _get_reply, _get_retweet, _get_favorite] = [
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[1]/button/span' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[2]/button/span' % start),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[3]/button/span' % start)
            ]

        [_id, _timestamp0, _reply, _retweet, _favorite] = [
            _get_id.get_attribute('data-tweet-id'),
            _get_timestamp.get_attribute('data-time'),
            _get_reply.get_attribute('data-tweet-stat-count'),
            _get_retweet.get_attribute('data-tweet-stat-count'),
            _get_favorite.get_attribute('data-tweet-stat-count')
            ]

        [_fullname, _username, _timestamp, _tweet] = [
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[1]/strong' % start).text,
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[2]/b' % start).text,
            datetime.datetime.strptime(time.ctime(int(_timestamp0)), '%a %b %d %H:%M:%S %Y'),
            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[2]/p' % start).text
            ]

        _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

        _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
        _session.add(_record)
        _session.commit()
        print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
        time.sleep(1.25)

    except:

        try:

            [_get_id, _get_timestamp, _get_reply, _get_retweet, _get_favorite] = [
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[1]/button/span' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[2]/button/span' % start),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[3]/button/span' % start)
                ]

            [_id, _timestamp0, _reply, _retweet, _favorite] = [
                _get_id.get_attribute('data-tweet-id'),
                _get_timestamp.get_attribute('data-time'),
                _get_reply.get_attribute('data-tweet-stat-count'),
                _get_retweet.get_attribute('data-tweet-stat-count'),
                _get_favorite.get_attribute('data-tweet-stat-count')
                ]

            [_fullname, _username, _timestamp, _tweet] = [
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[1]/strong' % start).text,
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[2]/b' % start).text,
                datetime.datetime.strptime(time.ctime(int(_timestamp0)), '%a %b %d %H:%M:%S %Y'),
                _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/p' % start).text]

            _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

            _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
            _session.add(_record)
            _session.commit()
            print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
            time.sleep(1.25)

        except:

            try:

                [_get_id, _get_timestamp, _get_reply, _get_retweet, _get_favorite] = [
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[1]/button/span' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[2]/button/span' % start),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/div[2]/div[3]/button/span' % start)
                    ]

                [_id, _timestamp0, _reply, _retweet, _favorite] = [
                    _get_id.get_attribute('data-tweet-id'),
                    _get_timestamp.get_attribute('data-time'),
                    _get_reply.get_attribute('data-tweet-stat-count'),
                    _get_retweet.get_attribute('data-tweet-stat-count'),
                    _get_favorite.get_attribute('data-tweet-stat-count')
                    ]

                [_fullname, _username, _timestamp, _tweet] = [
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[1]/strong' % start).text,
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[2]/b' % start).text,
                    datetime.datetime.strptime(time.ctime(int(_timestamp0)), '%a %b %d %H:%M:%S %Y'),
                    _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[3]/p' % start).text]

                _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

                _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
                _session.add(_record)
                _session.commit()
                print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
                time.sleep(1.25)

            except:

                try:

                    [_get_id, _get_timestamp, _get_reply, _get_retweet, _get_favorite] = [
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[1]/button/span' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[2]/button/span' % start),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[4]/div[2]/div[3]/button/span' % start)
                        ]

                    [_id, _timestamp0, _reply, _retweet, _favorite] = [
                        _get_id.get_attribute('data-tweet-id'),
                        _get_timestamp.get_attribute('data-time'),
                        _get_reply.get_attribute('data-tweet-stat-count'),
                        _get_retweet.get_attribute('data-tweet-stat-count'),
                        _get_favorite.get_attribute('data-tweet-stat-count')
                        ]

                    [_fullname, _username, _timestamp, _tweet] = [
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[1]/strong' % start).text,
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[2]/b' % start).text,
                        datetime.datetime.strptime(time.ctime(int(_timestamp0)), '%a %b %d %H:%M:%S %Y'),
                        _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[2]/p' % start).text
                        ]

                    _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

                    _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
                    _session.add(_record)
                    _session.commit()
                    print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
                    time.sleep(1.25)

                except:

                    try:

                        [_get_id, _get_timestamp, _get_reply, _get_retweet, _get_favorite] = [
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start),
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/small/a/span' % start),
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[2]/div[1]/button/span' % start),
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[2]/div[2]/button/span' % start),
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[5]/div[2]/div[3]/button/span' % start)
                            ]

                        [_id, _timestamp0, _reply, _retweet, _favorite] = [
                            _get_id.get_attribute('data-tweet-id'),
                            _get_timestamp.get_attribute('data-time'),
                            _get_reply.get_attribute('data-tweet-stat-count'),
                            _get_retweet.get_attribute('data-tweet-stat-count'),
                            _get_favorite.get_attribute('data-tweet-stat-count')
                            ]

                        [_fullname, _username, _timestamp, _tweet] = [
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[1]/strong' % start).text,
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[1]/a/span[2]/b' % start).text,
                            datetime.datetime.strptime(time.ctime(int(_timestamp0)), '%a %b %d %H:%M:%S %Y'),
                            _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]/div[2]/div[2]/p' % start).text
                            ]

                        _dr.execute_script('arguments[0].scrollIntoView();', _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start))

                        _record = t_db(_id, origin, _fullname, _username, _timestamp, _tweet, _reply, _retweet, _favorite)
                        _session.add(_record)
                        _session.commit()
                        print('Tweet ID {} entered. {} of {}.'.format(int(_id), start, end))
                        time.sleep(1.25)

                    except:

                        _get_id = _dr.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[2]/ol[1]/li[%d]/div[1]' % start)
                        _id = _get_id.get_attribute('data-tweet-id')
                        pass
                        print('Error processing Tweet ID {}. {} of {}.'.format(int(_id), start, end))

    if start < end:

        t_scrape(origin, start + 1, end)

    else:

        _dr.close()
        _dr.quit()
