import logging
import os


def get_logger(log_file_name='sample.log'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s: %(message)s')
    if os.path.isdir('tmp'):
        pass
    else:
        try:
            os.mkdir('tmp')
        except OSError:
            print('Creation of the directory tmp dir failed')
        else:
            print('Successfully created the directory tmp')
    file_handler = logging.FileHandler('tmp/{}'.format(log_file_name), mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
