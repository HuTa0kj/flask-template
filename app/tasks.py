import time
import logging

from datetime import datetime
from app.extensions import celery


@celery.task
def log_access_time(user_id):
    start_time = datetime.now()
    logging.info(f"用户 {user_id} 访问时间: {start_time}")

    # 模拟长时间任务，延迟30秒
    time.sleep(30)

    end_time = datetime.now()
    logging.info(f"用户 {user_id} 结束时间: {end_time}")
    return start_time, end_time


@celery.task
def log_access_schedule_time():
    start_time = datetime.now()
    logging.info(f"访问时间: {start_time}")

    # 模拟长时间任务，延迟30秒
    time.sleep(30)

    end_time = datetime.now()
    logging.info(f"结束时间: {end_time}")
    return start_time, end_time
