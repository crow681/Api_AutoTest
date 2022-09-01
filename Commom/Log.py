# coding:utf-8
'''
简单配置日志
'''
import logging
import os

from time import strftime, localtime

class Mylogging:
    #  创建日志文件
    def __init__(self):
        date_fmt = '%Y-%m-%d %H:%M:%S '  # 格式化时间
        log_name = strftime('%Y%m%d', localtime())
        log_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + f'/Log/{log_name}.log'

        logging.basicConfig(
            format='%(asctime)s-%(levelname)s-%(message)s',
            datefmt=date_fmt,
            filename=f'{log_file}',
            encoding='utf-8',
            level=logging.DEBUG,

        )

    @staticmethod
    def debug(msg):
        logger = logging.getLogger(__name__)
        debug_msg = logger.debug(msg)
        return debug_msg
    @staticmethod
    def err(msg):
        logger = logging.getLogger(__name__)
        debug_msg = logger.error(msg)
        return debug_msg

    @staticmethod
    def warning(msg):
        logger = logging.getLogger(__name__)
        debug_msg = logger.warning(msg)
        return debug_msg

if __name__ == '__main__':
    mylog = Mylogging()
    mylog.debug('提示信息')
    mylog.err('错误信息')





















