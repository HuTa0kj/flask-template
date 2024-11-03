from app import create_app, config
import logging

app, celery = create_app(config.DevConfig)

if __name__ == '__main__':
    logging.info("启动成功")
    app.run(host='0.0.0.0', port=5000)
