#!/bin/bash

state=$(<b64.txt)

for i in {1..50}; do
    state=$(<<<"$state" base64 --decode)
done
echo "$state"