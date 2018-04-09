from subprocess import *

proc=Popen(u'/home/archermind/Desktop/input_string_and_echo.py', stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True)
string='say hi\n'
proc.stdin.write(string)
line=proc.stdout.read()
print(line)
proc.stdout.flush()
