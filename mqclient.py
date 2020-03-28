"""
Sample reworked from https://www.ibm.com/developerworks/websphere/library/techarticles/0708_salkosuo/0708_salkosuo.html
"""

import pymqi
from loguru import logger


def main():
    try:
        queue_manager_name = "QM1"
        queue_name = "DEV.QUEUE.1"
        queue_manager = pymqi.QueueManager(queue_manager_name)
        queue = pymqi.Queue(queue_manager, queue_name)
        queue.put("Hello from Python !")
    except Exception as exception:
        logger.exception(exception)


if __name__ == "__main__":
    main()
