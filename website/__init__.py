from flask import Flask


def create_app():
    # __name__ là một biến đặc biệt trong Python, nó được truyền vào để Flask biết vị trí của ứng dụng.
    app = Flask(__name__)
    # 'SECRET_KEY' được sử dụng bởi Flask và các extension của nó để bảo mật (ví dụ: tạo chữ ký cho cookies phiên (session cookies)).
    app.config['SECRET_KEY'] = 'nothingissecret'

    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')


    return app