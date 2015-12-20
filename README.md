# distributed-file-system
Distributed File System

#### Setup  
`from dfs import namenode, datanode`

#### Namenode  
Init  
`nn = Namenode()`  
Save a file  
`nn.save(file_path, file_size, timestamp)`  
Retrieve a file  
`nn.get(file_path, timestamp)`  

#### Datanode  
Init  
`dn = Datanode()`  
Write a datablock  
`dn.write(file_hash, timestamp, data)`  
Read a datablock  
`dn.read(file_hash, timestamp)`  
