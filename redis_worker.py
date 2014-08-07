from redis import Redis

from config import REDIS_CRAWLER_KEY, REDIS_RECENT_SEARCHES, MAX_RECENT_SEARCH_ITEMS
from main import crawler_machine

import time

redis = Redis()

def work():
    while 1:
        msg = redis.spop(REDIS_CRAWLER_KEY)
        if msg:
            crawler_machine(msg)
        else:
            print "waiting for command!"
        time.sleep(10)

def recent_searches(kw=None, fetch_only=False):
    if kw:
        redis.lpush(REDIS_RECENT_SEARCHES,kw)
    if fetch_only:
        return redis.lrange(REDIS_RECENT_SEARCHES, 0, MAX_RECENT_SEARCH_ITEMS)

if __name__ == '__main__':
    work()
