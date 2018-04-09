#!/bin/bash
# 脚本运行后, 直接然后执行
# echo "abc" >> /tmp/testpipe

pipe=/tmp/testpipe

trap "rm -f $pipe" EXIT

if [[ ! -p $pipe ]]; then
#创建命令管道
    mkfifo $pipe
fi

while true
do
#从管道里读取一行
    if read line <$pipe; then
#如果是quit则退出循环
        if [[ "$line" == 'quit' ]]; then
            break
        fi
#输出读取的数据到屏幕
        echo $line
    fi
done

echo "Reader exiting"
