# PluginDispatcher
Flask PluginDispatcher load plugins dynamically

This is a demonstration application to show how we can run multiple flask application
within the same interpreter.

Here we suppose we have a main application `yoona.py` and multiple plugins in the `plugins` folder

The PluginDispatcher will look at each request if it maches the path `/plugins/plugin_name`
and look for the plugin in the plugins folder, if it's there it will load it.

### Installation 

`git clone https://github.com/vcar/PluginDispatcher.git`

`pip install -r requirements.txt`

`python run.py `

You can create new plugins and they will load automatically.