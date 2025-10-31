#!/usr/bin/env bash
set -e

IFS_old=$IFS
IFS=$'\n'
if [ ! -f tdl-chatlist ] || [ $(find tdl-chatlist -mtime +0) ]; then
    go run main.go chat ls > tdl-chatlist
fi
for chat in $(cat tdl-chatlist | sed -n "2,$ p"); do
  id=$(echo $chat | awk '{print $1}')
  # shellcheck disable=SC2010
  modify_time_1=$(ls -l -D "%Y%m%d" downloads | grep "$id" | awk '{print $6}' 2>/dev/null)
  # shellcheck disable=SC2010
  modify_time_2=$(ls -l -D "%Y%m%d" jsons | grep "$id" | awk '{print $6}' 2>/dev/null)
  [ "x$modify_time_2" == "x" ] && modify_time=$modify_time_1 || modify_time=$modify_time_2
  
  if [ -z "$modify_time" ]; then
    echo "$chat"
  else
    # macOS/BSD 日期计算
    seven_days_ago=$(date -v-7d "+%Y%m%d")
    
    # 比较修改时间是否在7天前
    if [ "$modify_time" -lt "$seven_days_ago" ]; then
      echo "$chat"
    fi
  fi
done
IFS=$IFS_old

echo -e "\033[1;31m --> tdl chat export \033[0m"
#go run main.go chat export -c $1 -f "Views>200 && Media.Name not endsWith '.jpg'"
python export.py $1

echo -e "\033[1;31m --> reduce export \033[0m"
mkdir -p downloads/$1
[ "x$2" == "x" ] && min_reactions=30 || min_reactions=$2
python reduce_export.py $min_reactions

echo -e "\033[1;31m --> print url \033[0m"
python get_url.py $1
find ./downloads -type d -empty -delete
