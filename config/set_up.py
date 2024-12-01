import logging


base_url = "https://jsonplaceholder.typicode.com/"


def get_logger():
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='script_logger.log', format=LOG_FORMAT, level=logging.ERROR, force=True)
    log = logging.getLogger()
    return log