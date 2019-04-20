import logging


def get_logger(log_file_name='sample.log'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s: %(message)s')
    file_handler = logging.FileHandler('tmp/{}'.format(log_file_name), mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
