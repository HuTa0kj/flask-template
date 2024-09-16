from app.extensions import db

"""
编写数据库连接
"""


class UserTable(db.Model):
    __tablename__ = "user"
    # 主键、自增长
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
