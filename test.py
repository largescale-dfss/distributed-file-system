from dfs.namenode import Namenode
from dfs.datanode import Datanode
nn = Namenode()
nn.save("user/alan/resume/resume.txt", 40000, 1)
nn.get("user/alan/resume/resume.txt",1)
#print nn.blocksize
#dn = Datanode()
#dn.write('27d5482eebd075de44389774fce28c69f45c8a75', 10101, "hello world")
#dn.read('27d5482eebd075de44389774fce28c69f45c8a75', 10101)
