import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def timer(func):
    """
    This decorator is a timer used to observe the time taken to execute a function
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        logger.info(f"Time taken to execute {func.__name__} - {time.time() - start}s")
        return res

    return wrapper


@timer
def tester():
    for i in range(5000000):
        pass


if __name__ == "__main__":
    tester()
