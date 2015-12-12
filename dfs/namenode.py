import os, json
from math import pow, ceil
from collections import OrderedDict
class Namenode:
    root = "/var/dfs_nm"
    blocksize = 15 * int(pow(2, 10)) #15 KB
    datanodes ={('localhost',5000):5, ('localhost',6000):0, ('localhost',7000):1, ('localhost',8000):3}

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
        arr = None
        with open(absPath, 'r') as f:
            list_datanodes = f.read()
            print json.loads(list_datanodes)
            return list_datanodes

    #choose the datanodes with least number of blocks
    def getNewDN(self, numBlocks):
        dnodes = []
        od = OrderedDict(sorted(self.datanodes.items()), key=lambda t: t[1])
        keys = od.keys()
        if (numBlocks > len(self.datanodes)):
            dnodes = keys + keys[:numBlocks-len(keys)]
        else:
            dnodes = keys[:numBlocks]
        self.updateDN(dnodes)
        return dnodes

    #updates the datanodes with numbers of blocks
    def updateDN(self, dnodes):
        for node in dnodes:
            self.datanodes[node] += 1
    
    #filename, filesize => 
    def save(self, file_id, file_size, timestamp):
        numBlocks = int(ceil(float(file_size)/self.blocksize))
        filename = str(file_id) + "@" + str(timestamp)
        absPath = os.path.join(self.root, filename)
        with open(absPath, 'w') as f:
            list_ports = self.getNewDN(numBlocks)
            f.write(json.dumps(list_ports))

