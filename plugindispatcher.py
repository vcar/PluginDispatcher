import re
from threading import Lock
from werkzeug.wsgi import pop_path_info, peek_path_info


class PluginDispatcher(object):
    """
    The Plugin dispatcher takes the request object, looks for the correct
    Flask instace to dispatche the request to, in case of no plugin found
    the request is redirected to the default app. 
    """

    def __init__(self, default_app, create_app):
        self.default_app = default_app
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, plugin_path):
        with self.lock:
            plugin_name, plugin_prefix = self.get_plugin_name(plugin_path)
            app = self.instances.get(plugin_name)
            if app is None:
                app = self.create_app(plugin_name)
                if app is not None:
                    self.instances[plugin_name] = app

            return app, plugin_prefix

    def __call__(self, environ, start_response):
        # path_info = peek_path_info(environ)
        app, prefix = self.get_application(environ['PATH_INFO'])
        if app is not None:
            if environ['PATH_INFO'].startswith(prefix):
                environ['PATH_INFO'] = environ['PATH_INFO'][len(prefix):]
                environ['SCRIPT_NAME'] = prefix
            # pop_path_info(environ)
        else:
            app = self.default_app

        return app(environ, start_response)

    def get_plugin_name(self, path):
        try:
            path_list = path.split('/')
            if path_list[1] != 'plugins' or path_list[2] == '':
                return None, None
            else:
                name = re.sub('[^A-Za-z0-9-_]', '', path_list[2])
                prefix = '/'.join(['/plugins', name])
                return name, prefix
        except Exception:
            return None, None
