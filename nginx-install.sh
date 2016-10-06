sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev unzip
mkdir nginx
cd nginx
wget http://nginx.org/download/nginx-1.8.1.tar.gz
tar -zxvf nginx-1.8.1.tar.gz
wget https://github.com/arut/nginx-rtmp-module/archive/master.zip
unzip master.zip
cd nginx-1.8.1
./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master
make
sudo make install
