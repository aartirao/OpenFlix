if [[$# -eq 0]]; then 
	echo "No args"
	exit 0
fi
rm /home/ubuntu/video-streaming-server/index/static/images/thumbnails/$1*
cd /usr/local/nginx/Videos/vod && rm $1*
ssh ubuntu@192.168.1.7 'bash -s' < /home/ubuntu/del-there.sh $1
ssh ubuntu@192.168.1.5 'bash -s' < /home/ubuntu/del-there.sh $1

