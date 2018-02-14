#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'user'

import ConfigParser
import os, sys, getopt

DEF_PATH_CONFIG = '/home/user/.ssh/.GIT.CONF'
DEF_PATH_IDRSA = "/home/user/.ssh/id_rsa"
DEF_PATH_IDRSA_PUB = "/home/user/.ssh/id_rsa.pub"
KEY_EMAIL = "email"
KEY_NAME = "NAME"
KEY_PUBKEY = "PUBKEY"
KEY_PRIKEY = "PRIKEY"
KEY_PUBKEY_HASH = "PUBKEY_HASH"
KEY_PRIKEY_HASH = "PRIKEY_HASH"


def add_config2file(name, email, publick_key, private_key):
    config = ConfigParser.ConfigParser()
    config.add_section(email)
    config.set(email, KEY_NAME, name)
    config.set(email, KEY_EMAIL, email)
    key_pub = open(publick_key).read()
    key_pri = open(private_key).read()
    config.set(email, KEY_PUBKEY, key_pub)
    config.set(email, KEY_PUBKEY_HASH, hash(key_pub))
    config.set(email, KEY_PRIKEY, key_pri)
    config.set(email, KEY_PRIKEY_HASH, hash(key_pri))

    # write to file
    config.write(open(DEF_PATH_CONFIG, "a"))


def read_config(section_str):
    config = ConfigParser.ConfigParser()
    config.readfp(open(DEF_PATH_CONFIG))
    name_str = section_str
    email = config.get(section_str, KEY_EMAIL)
    public_key = config.get(section_str, KEY_PUBKEY)
    private_key = config.get(section_str, KEY_PRIKEY)
    return name_str, email, public_key, private_key


# name, email, puk, prk
def write_ssh(str, file):
    try:
        fsock = open(file, "w")
        fsock.write(str)
    except IOError:
        print "The file don't exist, Please double check!"
        exit()
    P = fsock.tell()
    print 'the postion is %d' % (P)
    fsock.close()


def write(info):
    write_ssh(info[2], DEF_PATH_IDRSA_PUB)
    write_ssh(info[3], DEF_PATH_IDRSA)
    re(info[0], info[1])


def re(mail, name):
    fhl = open(DEF_PATH_CONFIG, 'r')
    s = ''
    for line in fhl.readlines():
        if "email = " in line:
            l1 = line.replace(line[12:-1], mail)
            s = s + l1
            continue
        if "name = " in line:
            l2 = line.replace(line[8:-1], name)
            s = s + l2
            continue
        s = s + line
    fhl.close()
    print s
    ove = open(DEF_PATH_CONFIG, 'w')
    ove.write(s)
    ove.close()


def main(name):
    info = read_config(name)
    print info
    write(info)
    print "Successed!"


def get_config_user_list():
    config = ConfigParser.ConfigParser()
    config.readfp(open(DEF_PATH_CONFIG))
    return config.sections()


def list_and_restore_config():
    # except getopt.GetoptError:
    print "Welcome to config list\n" \
          "All of the users follow this:" \
          "\n" \
          ""
    sections = {}
    for index, user in enumerate(get_config_user_list()):
        index += 1
        sections[index] = user
        print "\t", index, " ）\t", user
        # for line_str in open('git.conf', "r"):
    # print line_str,
    selected_index = 0
    while selected_index < 1 or selected_index > sections.__len__():
        try:
            selected_index = input("\ninput your selected num:")
            if selected_index < 1 or selected_index > sections.__len__():
                print "Please reinput correct number index!!!"
            else:
                main(sections[selected_index])

        except:
            print "\n>>>>>>>>>>   Please reinput number to choose!!!   <<<<<<<<<<<"


def usage():
    print '''
    ××××××××××××××××××××××××××××××××××××××××××××××××××

    1、后续功能，添加已经存在的用户更新信息
    2、在恢复的时候根据校验和来检验预先检验是否正确

                                version：0.1
    ××××××××××××××××××××××××××××××××××××××××××××××××××

        0)  -h
            帮助
        1)  -e email
            指定联系人邮箱，姓名由邮箱规则获取
        2） -v private_key_path
            添加私有秘钥路径，配合-v -e使用
        3） -r public_kep_path
            添加共有秘钥路径，配合-v -e使用
        4)  -l
            显示当前配置信息里面的人员列表
        6)  -r
            直接恢复联系人
    '''


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:g:s:r:")
        params = ''
        name = ''
        email = ''
        private_key = ''
        public_key = ''
        restore_name = ''
        for op, value in opts:
            print op, value
            if op == "-l":
                list_and_restore_config();
                # if op == "-n":
            elif op == "-e":
                email = value
                name = value.split('@')[0]
            elif op == "-g":
                public_key = value
            elif op == "-s":
                private_key = value
            elif op == "-r":
                main(value)
                sys.exit()
            elif op == "-h":
                usage()
                sys.exit()
            params = op + params
            if '-e' in params and '-s' in params and '-g' in params:
                if email not in get_config_user_list():
                    add_config2file(name, email, public_key, private_key)
                else:
                    print "email is alread exist, need update?"
                    # todo: update


    except getopt.GetoptError:
        print("getopt error!")
        usage();
        sys.exit(1)
