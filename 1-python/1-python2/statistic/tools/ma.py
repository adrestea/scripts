#!/usr/bin/env python
# -*- coding:utf-8 -.-
import commands
import os

import sys

sys.path.append(r'/home/archermind/workspace/git/1-git-adrestea/scripts/1-python/1-python2/statistic/')
import utils.config as config

# from statistic.utils import config
# print (sys.path)

dst_dir = "/home/archermind/.bin"
config_file = "/home/archermind/.ma/db.ini"
method_mark = "set"
method_display = 'display'
method_goto = 'goto'


def create_symlink(src, prf_fix):
    bin_list = ['m' + chr(i) for i in range(97, 123)]
    bin_list = ['m' + str(i) for i in range(10)]
    # bin_list.remove(prf_fix + 'v')
    # bin_list.remove(prf_fix + 'm')
    bin_list.append('lsa')
    # bin_list += ['cd' + chr(i) for i in range(97, 123)]
    # bin_list += ['cd' + str(i) for i in range(10)]
    if os.path.isfile(src):
        # global dst_dir
        for bin_name in bin_list:
            dst_bin_file = os.path.join(dst_dir, bin_name)
            if not os.path.isfile(dst_bin_file):
                os.symlink(src, dst_bin_file)
                print "link is created: " + bin_name
            else:
                print "link is existed: " + bin_name
        return True
    return False


def run_x(configure, cmd, pwd):
    # print("run_x...")
    method, key = cmd
    if method == method_display:
        display_all(configure)
    elif method == method_mark:
        configure.write_config(key, pwd, "MARK")
    elif method == method_goto:
        path = configure.read_config(key, 'MARK')
        cmd = 'cd ' + "\'" + path + "\'"
        os.system(cmd)


def conversion(origin):
    # print("conversion...")
    command = os.path.basename(origin).split('.')[0]
    val = []
    length = len(list(command))
    if str.startswith(command, "m") and length == 2:
        val = [method_mark, 'mark_' + command]
    elif str.startswith(command, "mcd") and length == 4:
        val = [method_goto, "mark_m" + command[-1]]
    elif str.startswith(command, "ls") and length == 3:
        val = [method_display, None]
    return val


def display_all(configure):
    sections = configure.sections()
    for node in sections:
        i = configure.items(node)
        for key, val in i:
            if "mark_" in key:
                print(key + " :  " + val)


if __name__ == "__main__":
    try:
        origin = sys.argv[0]
        # origin = '/home/archermind/.bin/lsa'
        # origin = '/home/archermind/.bin/mcda'
        # origin = '/home/archermind/.bin/cda'
        # print(origin)
        # pwd = os.getcwd()
        pwd = commands.getoutput('pwd')
        conf = config.Config(config_file)
        if conf.read_config("initial", 'MARK') is None:
            # print('init...')
            if create_symlink(sys.argv[0], "m"):
                print('create symlinks succeeded')
                conf.add_section("MARK")
                conf.write_config('initial', True, 'MARK')

        run_x(conf, conversion(origin), pwd)
    except Exception as e:
        print(e)
