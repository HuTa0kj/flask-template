from app import create_app, config

app, celery = create_app(config.DevConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
