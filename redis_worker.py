from redis import Redis

from config import REDIS_CRAWLER_KEY
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

if __name__ == '__main__':
    work()