#!/bin/bash
# Readme: 同步游戏日志到统一地方给YY下载
rsync -avzq --password-file=/etc/rsync_manager_passwd.txt --port=873 /data/goplog/ suyu@10.23.4.141::upload_gamelog/ > /dev/null 2>&