This project provides cloud based video-on-demand streaming

Server Configuration uses NGINX RTMP Module

Front End - 
* Python Bottle as the server
* Dash.js as the video player

To Run -

1. Install nginx with nginx-rtmp and ffmpeg using `sh nginx-install.sh`
2. Copy the nginx configuration to /usr/local/nginx/conf
3. Copy the contents of sample-videos to the folder - /usr/local/nginx/Videos/vod
4. Install python bottle by `pip install bottle`
5. Run `python index.py`