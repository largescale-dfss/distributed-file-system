import os, pickle
from math import pow, ceil
class Namenode:
    root = "/var/dfs_nm"
    blocksize = 15 * int(pow(2, 10)) #10 KB
    datanodes = {5000:0, 6000:0, 7000:0, 8000:0}

    #Initializes the namenode and creates nm directory if not exist
    def __init__(self):
        if not (os.path.isdir(self.root) and os.path.exists(self.root)):
            try:
                os.makedirs(self.root)
            except OSError as exception:
                print "Run the script as root"
    
    #filename => array of blocks
    def get(self, file_id, timestamp):
        filename = str(file_id) + "@" + str(timestamp)
        absPath = os.path.join(self.root, filename)
        with open(absPath, 'r') as f:
            list_ports = pickle.load(f)
            print(list_ports)

    def getNewDN(num):
        datanodes = []

    
    #filename, filesize => 
    def save(self, file_id, file_size, timestamp):
        numBlocks = ceil(float(file_size)/self.blocksize)
        filename = str(file_id) + "@" + str(timestamp)
        absPath = os.path.join(self.root, filename)
        with open(absPath, 'w') as f:
            list_ports = [[5000, 6000],[6000, 5000]]
            pickle.dump(list_ports, f)

