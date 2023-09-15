#!/usr/bin/env bash

#go run main.go chat export -c $1 -f "Views>200 && Media.Name not endsWith '.jpg'"
go run main.go chat export -c $1 -f "Views>200"
