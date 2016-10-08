#!/bin/bash

path="/usr/local/ngnix/Videos/vod2/"
filename=$1
input_file=$path$1
output_file="$2.mp4"
output_filename=$path$output_file

input_name=${filename%.*}
#input_name="sample"
inter="intermediate_${input_name}_2400k.264"

x264 --output $inter --fps 24 --preset slow --bitrate 2400 --vbv-maxrate 4800 --vbv-bufsize 9600 --min-keyint 48 --keyint 48 --scenecut 0 --no-scenecut --pass 1 --video-filter "resize:width=1280,height=720" $input_file

MP4Box -add $inter -fps 24 $output_filename

MP4Box -dash 4000 -frag 4000 -rap -segment-name ${output_file%.*}_segment_ $output_filename

rm $inter
rm x264*
