#!/usr/bin/env bash
set -e

img_only=0
if [ "x"$2 != "x" ];then
    img_only=1
fi

echo -e "\033[1;31m --> tdl download \033[0m"
if [ $img_only == 0 ];then
    go run main.go dl -f tdl-export-reduced.json -d downloads/$1 --reconnect-timeout 0
else
    go run main.go dl -f tdl-export-reduced.json -d downloads/$1 --reconnect-timeout 0 -i jpg,png
fi

echo -e "\033[1;31m --> add watched \033[0m"
python add_watched.py
