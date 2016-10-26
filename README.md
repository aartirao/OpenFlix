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
3. sudo apt-get install ffmpeg

Nginx-GeoIp module:
sudo add-apt-repository ppa:maxmind/ppa
sudo apt-get update
sudo apt-get install libmaxminddb0 libmaxminddb-dev mmdb-bin
go to video_streaming_server/nginx/
git clone https://github.com/leev/ngx_http_geoip2_module.git
TAKE BACKUP OF NGINX CONF
cd nginx-1.8.1/
sudo apt-get install libgeoip-dev
./configure --with-http_ssl_module --with-http_stub_status_module --with-http_geoip_module --add-module=../nginx-rtmp-module-master
sudo make
sudo make install
replace NGINX.conf with the backup
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz
gzip -d GeoLite2-City.mmdb.gz
gzip -d GeoLite2-Country.mmdb.gz
One method is to use the unzipped files.
Make config changes as mentioned here - https://gist.github.com/kmjones1979/fcabb4731bbf85b9c50189e90d76b1c1



Another method:
wget https://raw.githubusercontent.com/phusion/nginx/master/contrib/geo2nginx.pl
chmod 755 geo2nginx.pl
wget http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
unzip GeoIPCountryCSV.zip
./geo2nginx.pl < GeoIPCountryWhois.csv > geo.conf
mv geo.conf /usr/local/nginx/conf

Replace the nginx.conf with the nginx-geoip.conf from github
restart nginx