import os
import logging

from app.read_config import read_config


class Logger:
    # 类属性，用于存储是否开启DEBUG模式
    debug_mode = read_config()["SET"]["DEBUG"]
    log_format = "[pid: %(process)d] [%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d %(funcName)s] - %(message)s"

    # 类初始化时配置日志系统
    def __init__(self):
        # 创建一个日志记录器
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG if self.debug_mode else logging.INFO)

        # # 确保日志目录存在
        log_directory = './log'
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # 写入日志文件
        log_file = os.path.join(log_directory, f'app.log')
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(logging.DEBUG if self.debug_mode else logging.INFO)
        file_handler.setFormatter(logging.Formatter(self.log_format))
        self.logger.addHandler(file_handler)

        # 日志输出到终端
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)  # 只输出INFO级别以上的日志到终端
        stream_handler.setFormatter(logging.Formatter(self.log_format))
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger


# 创建全局的日志记录器实例
logger = Logger().get_logger()
