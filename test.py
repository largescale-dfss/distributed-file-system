from dfs.namenode import Namenode

nm = Namenode()
nm.save("user/alan/resume/resume.txt", 40000, 1)
nm.get("user/alan/resume/resume.txt",1)
