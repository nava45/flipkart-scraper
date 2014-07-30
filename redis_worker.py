from redis import Redis

from config import REDIS_CRAWLER_KEY
from main import crawler_machine

redis = Redis()

def work():
    while 1:
        msg = redis.spop(REDIS_CRAWLER_KEY)
        crawler_machine(msg)

if __name__ == '__main__':
    work()