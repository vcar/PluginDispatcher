from flask import Flask
from werkzeug.serving import run_simple

"""
    DEFAULT APP,
    in the request path in not : plugins/plugin_folder
    then return the default app which is vCar dashboard
    plugins are accecible only via 'plugins' prefix to avoid confusion
"""


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return '<h1>APP : YOONA</h1><p>Default Application</p>'


if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
