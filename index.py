from bottle import Bottle, run, template, static_file, get, post, request, response, abort


import ConfigParser

config = ConfigParser.ConfigParser()
config.read('db.cfg')

app = Bottle()

# Static Routes
@app.route('/static/<path:path>')
def stylesheets(path):
    return static_file(path, root='index/static')

# Route for posts page
@app.route('/home')
@app.route('/home/')
def index(): 
	return template('index/index.html')


run(app, host=config.get('database','host'), port=config.get('database','port'), debug=True)