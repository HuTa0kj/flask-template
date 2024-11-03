import os
import yaml


def read_config():
    """
    读取配置文件
    :return: 配置文件内容
    """
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'config.yaml')
    with open(file_path, 'r', encoding='utf-8') as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)
        return configs
