class Datanode:
	root = "/var/dfs_dn"
	
	def __init__(self):
        if not (os.path.isdir(self.root) and os.path.exists(self.root)):
            try:
                os.makedirs(self.root)
            except OSError as exception:
                print "Run the script as root"

	def read(self, data):
		pass

	def write(self, data):
		pass
