#!/usr/bin/env bash

IFS_old=$IFS
IFS=$'\n'
go run main.go chat ls > tdl-chatlist
for chat in `cat tdl-chatlist | sed -n "2,$ p"`
do
    id=`echo $chat | awk '{print $1}'`
    modify_time=`ls -l -D "%Y%m%d" downloads | grep "$id" | awk '{print $6}' 2>/dev/null` 
    if [ -z $modify_time ];then
        echo $chat
    else
        now=`date "+%Y%m%d"`
        if [ $now != $modify_time ];then
            echo $chat
        fi
    fi
done
IFS=$IFS_old

echo -e "\033[1;31m --> tdl chat export \033[0m"
#go run main.go chat export -c $1 -f "Views>200 && Media.Name not endsWith '.jpg'"
go run main.go chat export -c $1

echo -e "\033[1;31m --> reduce export \033[0m"
mkdir -p downloads/$1
[ "x$2" == "x" ] && min_reactions=30 || min_reactions=$2
python reduce_export.py $min_reactions

echo -e "\033[1;31m --> print url \033[0m"
python get_url.py $1
find ./downloads -type d -empty -delete
