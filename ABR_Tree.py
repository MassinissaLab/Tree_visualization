class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 
    def getlefta(self):
        return self.left
    def getrighta(self):
        return self.right 

class ABRTree():
    def __init__(self):
        self.node = None 
    def recherche(self,val,w,r):
        if self.node!=None:
            if val==self.node.key:
                r.append(val)
            else:
                w.append(self.node.key)
                if val<self.node.key:                              
                    self.node.left.recherche(val,w,r)
                else:
                    self.node.right.recherche(val,w,r)             
    def insert(self, key):
        tree = self.node
        newnode = Node(key)
        if tree == None:
            self.node = newnode 
            self.node.left = ABRTree() 
            self.node.right = ABRTree()
        elif key < tree.key: 
            self.node.left.insert(key)
        elif key > tree.key: 
            self.node.right.insert(key)

        else: 
            pass
    def getleft(self):
        return self.node.getlefta()
    def getright(self):
        return self.node.getrighta()   
    def delete(self, key):
        if self.node != None: 
            if self.node.key == key: 
                
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None 
                
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None:
                        
                        self.node.key = replacement.key 
                        
                       
                        self.node.right.delete(replacement.key)
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            
        else: 
            return 
    def logical_predecessor(self, node):
       
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
       
        node = node.right.node  
        if node != None: 
            
            while node.left != None:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 
    def getedges(self,k):   
        if self.node==None :
            
            return 1        
        if self.node.left and self.node.getlefta().node!=None:
           
            t=tuple([self.node.key,self.node.getlefta().node.key])
            k.append(t)     
        if self.node.right and self.node.getrighta().node!=None:

            t=tuple([self.node.key,self.node.getrighta().node.key])
            k.append(t)
        self.node.left.getedges(k)
        self.node.right.getedges(k)  




    
