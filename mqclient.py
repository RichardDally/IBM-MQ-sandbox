"""
Sample reworked from https://www.ibm.com/developerworks/websphere/library/techarticles/0708_salkosuo/0708_salkosuo.html
"""

import pymqi
from loguru import logger


class MQManager:
    def __init__(self):
        self.queue_manager = config.queue_manager
        self.channel = config.channel
        self.port = config.port
        self.host = config.host
        self.conn_info = config.conn_info
        self.queue_request_name = config.queue_request_name
        self.queue_response_name = config.queue_response_name

        cd = pymqi.CD()
        cd.ChannelName = self.channel
        cd.ConnectionName = self.conn_info
        cd.ChannelType = pymqi.CMQC.MQCHT_CLNTCONN
        cd.TransportType = pymqi.CMQC.MQXPT_TCP

        self.qmgr = pymqi.QueueManager(None)
        self.qmgr.connect_with_options(self.queue_manager, opts=pymqi.CMQC.MQCNO_HANDLE_SHARE_NO_BLOCK, cd=cd)


def create_queue_manager():
    queue_manager = pymqi.QueueManager(None)
    return queue_manager


def main():
    queue_manager_name = "QM1"
    queue_name = "DEV.QUEUE.1"
    queue_manager = create_queue_manager()
    queue = pymqi.Queue(queue_manager, queue_name)
    queue.put("Hello from Python !")


if __name__ == "__main__":
    main()
