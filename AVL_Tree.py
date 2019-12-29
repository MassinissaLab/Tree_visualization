
import networkx as nx
import matplotlib.pyplot as plt



class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 
    def getlefta(self):
        return self.left
    def getrighta(self):
        return self.right    



class AVLTree():
    def __init__(self):
        self.node = None 
        self.height = -1  
        self.balance = 0 
        
        

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

                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
           print("Clé [" + str(key) + "] existe dans l'arbre")
            
        self.rebalance()


        
    def rebalance(self):
        ''' 
        Rebalance un sous-arbre particulier
        ''' 
        # on verifie et on m.a.j
        self.update_heights(False)
        self.update_balances(False)
        
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1: #+2
                if self.node.left.balance < 0:  #-1
                    self.node.left.lrotate() #cas rotation gauche droite
                    self.update_heights()
                    self.update_balances()
                self.rrotate()  #+1,0
            
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:#-2
                if self.node.right.balance > 0:  #+1
                    self.node.right.rrotate() # #cas rotation gauche droite
                    self.update_heights()
                    self.update_balances()
                self.lrotate() #-1,0
               
                self.update_heights()
                self.update_balances()
        



    def getleft(self):
        return self.node.getlefta()
    def getright(self):
        return self.node.getrighta()   

            
    def rrotate(self):
        # Rotation simple a droite
        
        R = self.node 
        P = self.node.left.node 
        Q = P.right.node 
        
        self.node = P 
        P.right.node = R
        R.left.node = Q 

    
    def lrotate(self):
        # Rotation simple a gauche
        
        R = self.node 
        P = self.node.right.node 
        Q = P.left.node 
        
        self.node = P
        P.left.node = R 
        R.right.node = Q
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, key):
        
        if self.node != None: 
            if self.node.key == key: 
                 
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # on supprime direct (feuille)
                # a 1 seule fils , on ecrase avec la valeur du fils droit (respectivement gauche)
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # pire des cas : deux fils (gauche et droit)
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  
                         
                        self.node.key = replacement.key 
                        
                        # aprés remplacement. on supprime  
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Retourne le noeud contenant la plus petite valeur du fils gauche
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Retourne le noeud contenant la plus petite valeur du fils droit
        ''' 
        node = node.right.node  
        if node != None:  
            
            while node.left != None:
                
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        


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
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):


    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):


        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


   
