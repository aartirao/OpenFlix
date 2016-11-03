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
sudo apt-get install x264 <br>
sudo apt-get install gpac <br>
sudo apt-get install ffmpeg <br> <br>

Nginx-GeoIp module: <br>
sudo add-apt-repository ppa:maxmind/ppa  <br>
sudo apt-get update <br>
sudo apt-get install libmaxminddb0 libmaxminddb-dev mmdb-bin <br>
go to video_streaming_server/nginx/ <br>
git clone https://github.com/leev/ngx_http_geoip2_module.git <br> <br>

TAKE BACKUP OF NGINX CONF <br>
cd nginx-1.8.1/ <br>
sudo apt-get install libgeoip-dev <br>
./configure --with-http_ssl_module --with-http_stub_status_module --with-http_geoip_module --add-module=../nginx-rtmp-module-master <br>
sudo make <br>
sudo make install <br>
replace NGINX.conf with the backup <br>
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz <br>
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz<br>
gzip -d GeoLite2-City.mmdb.gz<br>
gzip -d GeoLite2-Country.mmdb.gz<br>
One method is to use the unzipped files. <br>
Make config changes as mentioned here - https://gist.github.com/kmjones1979/fcabb4731bbf85b9c50189e90d76b1c1 <br>




Another method:
wget https://raw.githubusercontent.com/phusion/nginx/master/contrib/geo2nginx.pl
chmod 755 geo2nginx.pl
wget http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
unzip GeoIPCountryCSV.zip
./geo2nginx.pl < GeoIPCountryWhois.csv > geo.conf
mv geo.conf /usr/local/nginx/conf

Replace the nginx.conf with the nginx-geoip.conf from github
restart nginx