from bottle import Bottle, run, template, static_file, get, post, request, response, abort


import ConfigParser
import subprocess

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

# Route for uploads page
@app.route('/uploads',method="GET")
def index():
        return template('index/upload.html')

#Route to save uploaded file
@app.route('/upload', method='POST')
def video_upload():
    path = '/usr/local/nginx/Videos/vod'
    category   = request.forms.get('category')
    upload     = request.files.get('upload')

    upload.save(path) # appends upload.filename automatically
    print 'cd '+path +' && '+ './transcode.sh ' + str(upload.filename) + ' ' + str(upload.filename).replace('.flv', '')
    #subprocess.call(['cd '+path +' && '+ './transcode.sh ' + str(upload.filename) + ' ' + str(upload.filename).replace('.flv','')])
    subprocess.call('cd '+path +' && '+ './transcode.sh ' + str(upload.filename) + ' ' + str(upload.filename).replace('.flv', ''), shell=True)
    return 'OK'


run(app, host=config.get('database','host'), port=config.get('database','port'), debug=True)
