#coding:utf8 
'''
Created on 2015年4月7日

@author: Administrator
'''

# 过滤JAVA程序中的注释
# 如果字符串中有注释符号的话会有问题，还有代码中包含除号会有问题。

import io
import os
import re


# 改这个目录！！！
top_dir = "/home/user/Desktop/delete_comments";
#匹配java文件的正则表达式,使用python的前缀，就不用考虑转义问题  否则，需要转义的正则表达式是：
# reg = '.*\\.java$'   
reg = r'.*.java$'

# 状态
S_INIT = 0;
S_SLASH = 1;
S_BLOCK_COMMENT = 2;
S_BLOCK_COMMENT_DOT = 3;
S_LINE_COMMENT = 4;
S_STR = 5;
S_STR_ESCAPE = 6;

def trim_dir(path):
  print("目录：" + path);
  for root, dirs, files in os.walk(path):
    for name in files:
      print('name %s ' % name)
      trim_file(os.path.join(root, name))
      
    # for name in dirs:
      # trim_dir(os.path.join(root, name))

def trim_file(path):
  print("文件：" + path);
  #使用正则表达式匹配.java文件
  if re.match(reg , path):
    print("  处理");
  else:
    print("  忽略");
    return;

  bak_file = path + ".bak";
  os.rename(path, bak_file);

  fp_src = open(bak_file);
  fp_dst = open(path, 'w');
  state = S_INIT;
  for line in fp_src.readlines():
    for c in line:
      if state == S_INIT:
        if c == '/':
          state = S_SLASH;
        elif c == '"':
          state = S_STR;
          fp_dst.write(c);
        else:
          fp_dst.write(c);
      elif state == S_SLASH:
        if c == '*':
          state = S_BLOCK_COMMENT;
        elif c == '/':
          state = S_LINE_COMMENT;
        else:
          fp_dst.write('/');
          fp_dst.write(c);
      elif state == S_BLOCK_COMMENT:
        if c == '*':
          state = S_BLOCK_COMMENT_DOT;
      elif state == S_BLOCK_COMMENT_DOT:
        if c == '/':
          state = S_INIT;
        else:
          state = S_BLOCK_COMMENT;
      elif state == S_LINE_COMMENT:
        if c == '\n':
          state = S_INIT;
      elif state == S_STR:
        if c == '\\':
          state = S_STR_ESCAPE;
        elif c == '"':
          state = S_INIT;
        fp_dst.write(c);
      elif state == S_STR_ESCAPE:
        # 这里未完全实现全部序列，如\oNNN \xHH \u1234 \U12345678，但没影响
        state = S_STR; 
        fp_dst.write(c);

  fp_src.close();
  fp_dst.close();

trim_dir(top_dir);

