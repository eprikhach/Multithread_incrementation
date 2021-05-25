"""In this task we will work with multithreading.

To solve this task we need:
1. Lock function, which implement incrementation
"""

from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock
from loguru import logger

# Removing basic logging handler, which is used for debugging.
# Users don't need to know what's going on in the program.
logger.remove(0)

logger.add('logs.log', level='INFO',
           format="{time} {level} {message}",
           rotation='1 MB', compression='zip')


from incr import incrementation
print(incrementation(5, 1_000_000))
# Second solution, which use c++ module(atomic vars + multithreading).


class Counter:

    def __init__(self):
        self.a = 0


@logger.catch()
def function(arg: int, counter: Counter, lock: Lock):
    """Multithreading incrementation

    :param lock: lock object
    :param counter:
    :param arg: number of incrementation
    :return: None
    """

    for _ in range(arg):
        lock.acquire()
        counter.a += 1
        lock.release()


def main():
    lock = Lock()
    counter = Counter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(function(1000000, counter, lock, ))

    print("----------------------", counter.a)  # ???


if __name__ == "__main__":
    main()
