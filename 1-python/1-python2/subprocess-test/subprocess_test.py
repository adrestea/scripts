#
# 使用上次的输出作为下次的输入

import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
s=child1.stdout
# print(s)
child2 = subprocess.Popen(["wc"], stdin=s,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)
