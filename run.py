from flask import Flask
import pkgutil
import importlib
from werkzeug.serving import run_simple

import plugins
from plugindispatcher import PluginDispatcher
from yoona import app as default_app


def create_plugin(plugin_name):
    """
        Import the plugin from its local path, then create an instance
        of the plugin using create_app() and return it
        Return <Flask : plugin>
    """
    plugin = importlib.import_module('plugins.'+plugin_name)
    return plugin.create_app()


def get_plugins():
    """
        Get the list of valid plugins in the plugin folder (not used)
    """
    for importer, plugin_name, is_pakage in pkgutil.iter_modules(plugins.__path__):
        if plugin_name is not None and is_pakage:
            return create_plugin(plugin_name)


def get_plugin(plugin_name):
    """
        create an instance of a plugin given its name,
        return the plugin instance, otherwise return None
    """
    if plugin_name is not None:
        return create_plugin(plugin_name)
    else:
        return None


application = PluginDispatcher(default_app, get_plugin)


if __name__ == '__main__':
    run_simple('localhost', 5000, application, use_reloader=True,
               use_debugger=True, use_evalex=True)
