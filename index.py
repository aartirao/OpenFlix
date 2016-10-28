from bottle import Bottle, run, template, static_file, get, post, request, response, abort

from ffvideo import VideoStream
import ConfigParser
import subprocess
import glob

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
    files = glob.glob("index/static/images/thumbnails/*.jpeg")
    
    for i in range(0, len(files)):
        files[i] = files[i].replace('index/','')
    return template('index/index.html', thumbs=files)

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
    #create thumbnail
    thumbnail = VideoStream(path+'/'+str(upload.filename)).get_frame_at_sec(3).image() 
    thumbnail.save('./index/static/images/thumbnails/'+str(upload.filename).replace('.flv', '')+'.jpeg')
    #run transcode module
    subprocess.call('cd '+path +' && '+ './transcode.sh ' + str(upload.filename) + ' ' + str(upload.filename).replace('.flv', ''), shell=True)
    return 'OK'


run(app, host=config.get('database','host'), port=config.get('database','port'), debug=True)
