#!/usr/bin/env bash

echo 1

echo 'Auto Video making and upload it to Telegram'

echo 'Creating video ...'

python create.py --mass

echo 'Video Created :)'

echo 'Sending to Telegram ...'

node send.js v output.mp4

echo 'Video sended sucessfully :)'
node send.js a meens.mp3
rm output.mp4
