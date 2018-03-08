#!/usr/bin/env bash

trapper () { #建立个函数
  trap ' ' 2 3 20 #忽略CTRL+C CTRL+\ CTRL+Z信号
}

reset;clear #清除屏幕
info="Please input the password you will use later!"
cowsay $info
read mypassword
echo "Screen will locked in 7 seconds!"
sleep 7
clear

#加上这个倒记时的小东东,;)
while : #进入死循环
do
    trapper #调用函数
    printf "\n\n\n\n\n\n\n\n\t\t\tPlease enter unlock code:" | cowsay
    stty -echo  #屏蔽输入的字符
    read input
    case $input in $mypassword)
    printf "\t\t Hello $USER,Today is $(date +%T)\n"
    stty echo
    break ;;  #输入正确,挑出循环回到命令行
    *)echo "Do not check my files,please! See as follows:"
    sleep 3
    clear
    continue ;;  #否则,继续循环
    esac
done