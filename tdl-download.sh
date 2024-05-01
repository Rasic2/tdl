#!/usr/bin/env bash

echo -e "\033[1;31m --> tdl download \033[0m"
go run main.go dl -f tdl-export-reduced.json -d downloads/$1 --reconnect-timeout 0

echo -e "\033[1;31m --> add watched \033[0m"
python add_watched.py
