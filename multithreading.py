"""In this task we will work with multithreading.

To solve this task we need:
1. Lock function, which implement incrementation
"""

# from incr import incrementation
# print(incrementation(5, 1_000_000))
# Second solution, which use c++ module(atomic vars + multithreading).

from threading import Thread, Lock
from loguru import logger

# Removing basic logging handler, which is used for debugging.
# Users don't need to know what's going on in the program.
logger.remove(0)

logger.add('logs.log', level='INFO',
           format="{time} {level} {message}",
           rotation='1 MB', compression='zip')


@logger.catch()
def locker(func):
    """Decorator, that implement threading.Lock

    :param func: func, that need to be locked
    :return: wrapped function
    """
    lock = Lock()

    def wrapper(arg):
        with lock:
            func(arg)

    return wrapper


def main():
    a = 0

    @locker
    @logger.catch()
    def function(arg):
        """Multithreading incrementation

        :param arg: number of incrementation
        :return: None
        """

        nonlocal a

        for _ in range(arg):
            a += 1

    threads = []
    for _ in range(5):
        thread = Thread(target=function, args=(1_000_000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # ???


if __name__ == "__main__":
    main()
