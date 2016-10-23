This project provides cloud based video-on-demand streaming

Server Configuration uses NGINX RTMP Module

Front End - 
* Python Bottle as the server
* Dash.js as the video player

To Run -

1. Install nginx with nginx-rtmp and ffmpeg using `sh nginx-install.sh`
2. Copy the nginx configuration to /usr/local/nginx/conf
3. Copy the contents of sample-videos to the folder - /usr/local/nginx/Videos/vod
4. Copy transcode script transcode.sh to /usr/local/nginx/Videos/vod 
5. Install python bottle by `pip install bottle`
6. Run `python index.py`

To Install MP4Box
https://gpac.wp.mines-telecom.fr/2015/07/29/gpac-build-mp4box-only-all-platforms/

Steps:
1. sudo apt-get install x264
2. sudo apt-get install gpac