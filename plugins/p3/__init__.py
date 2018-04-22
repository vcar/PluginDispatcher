from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<h1>Plugin : 03</h1>'

    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>P2 : 404</h1>", 404

    return app
