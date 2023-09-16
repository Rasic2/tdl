#!/usr/bin/env bash

cat tdl-chatlist
echo -e "\033[1;31m --> tdl chat export \033[0m"
#go run main.go chat export -c $1 -f "Views>200 && Media.Name not endsWith '.jpg'"
go run main.go chat export -c $1
echo -e "\033[1;31m --> reduce export \033[0m"
mkdir -p downloads/$1
python reduce_export.py
echo -e "\033[1;31m --> print url \033[0m"
python get_url.py $1
