# 使用官方Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

ENV TZ=Asia/Shanghai

# 将 requirements.txt 复制到容器内
COPY requirements.txt /tmp/requirements.txt

# 安装 requirements.txt 中指定的任何所需包
RUN apt-get update && pip install --no-cache-dir -r /tmp/requirements.txt

# 在容器启动时运行 app.py
CMD ["python", "run.py"]
