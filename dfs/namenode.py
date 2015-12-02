import os
from math import pow
class Namenode:
    root = "/var/dfs_nm"
    blocksize = 10 * int(pow(2, 10)) #10 KB
    datanodes = []

    #Initializes the namenode and creates nm directory if not exist
    def __init__(self):
        if not (os.path.isdir(self.root) and os.path.exists(self.root)):
            try:
                os.makedirs(self.root)
            except OSError as exception:
                print "Run the script as root"
    
    #filename => array of blocks
    def get(self, filename):
        pass
    
    #filename, filesize => 
    def save(self, file_id, file_size)
        pass
