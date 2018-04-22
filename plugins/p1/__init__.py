from flask import Flask


def create_app():
    """
    create_app called by the dispatcher in case a requet is made to
    this plugin if the app already existe it will use it otherwise
    it will be created using this method 
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<h1>Plugin : 01</h1>'

    @app.route('/saya')
    def saya():
        return '<h1>Plugin : SAYA</h1>'

    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>P1 : 404</h1>", 404

    return app
