import logging


base_url = "https://jsonplaceholder.typicode.com/"


def get_logger():
    """
    logger method for logging all the errors occurred in any of test suites, posts, users or comments
    """
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='script_logger.log', format=LOG_FORMAT, level=logging.ERROR, force=True)
    log = logging.getLogger()
    return log