#!/bin/bash
clear
echo -e "正在更新 Termux 软件包列表，请稍候……\n"
apt update &>/dev/null
echo -e "正在升级 Termux 软件包……这可能需要一些时间\n"
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade >/dev/null
echo -e "请允许存储权限\n"
termux-setup-storage
apt install python --no-install-recommends -y &>/dev/null
echo "请耐心等待"
curl -o installglibc.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installglibc.py && python3 installglibc.py
exit
