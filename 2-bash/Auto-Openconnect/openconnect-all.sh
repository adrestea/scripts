#!/bin/bash

line=`cat -n openconnect-all.sh |egrep "#\!/bin/expect$" |awk '{print $1}'`
eval tail -n +$line $0 > .exp
path_openconnect=`which openconnect`
if [ ! -u $path_openconnect ]; then
    echo "---------------------------------"
    echo "|   add openconnect permission. |"
    echo "---------------------------------"
    sudo chmod u+s $pp
fi

dpkg -l |egrep "ii  expect" >> /dev/null 2>&1
if [ ! 0 -eq $? ]; then
    echo "---------------------------------"
    echo "|          install expect.      |"
    echo "---------------------------------"
    sudo apt-get install expect
fi

flag=true

# For handle the interrupt message
trap 'onCtrlC' INT
function onCtrlC () {
    flag=false
    echo "-----set flag false----"
}

# For logs:
{
    echo -n `date "+%Y-%m-%d %H:%M:%S"` >> .logs
    ping hichub.htc.com -i 30 >> .logs
} &
while $flag; do
    echo 'I am working!, flag='$flag
    notify-send "[Auto Connect]: Begin to connect to server."
    /usr/bin/expect .exp
    sleep 5
    if [ ! $flag ]; then
        echo "Interrupt by user."
        break
    fi
done
rm .exp
echo "----------------- script End -----------------"
exit 0


#!/bin/expect

set timeout 30
spawn openconnect https://vpncn.htc.com/amt
expect "Username:"
send "amtuser2\r"
expect "Password:"
send "90gastzb\r"
interact
