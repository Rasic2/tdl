IFS_old=$IFS
IFS=$'\n'
for chat in $(cat tdl-chatlist | sed -n "2,$ p"|awk '{print $1}')
do 
    echo $chat 
    ./tdl-export.sh $chat 
done
IFS=$IFS_old
