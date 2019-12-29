class BTree:
    class Node:
        # initialisation de noeud
        def __init__(self):
            self.sons = []
            self.keys = []

        # position d'un valeur dans un neoud
        def position(self, key):
            b = 0
            try:
                while b < len(self.sons) - 1:
                    if key <= self.keys[b]:
                        return b
                    else:
                        b += 1

                pass
            except:
                return b

            return len(self.sons) - 1

    def __init__(self, t):
        self.root = self.Node()
        self.t = t

    def _insert(self, key,node,parnode):
        # si noeud n'exist pas
        if node is None: return None
        pos=node.position(key)
        if len(node.sons) == 0 and node is self.root:
            node.sons.append(None)
            node.keys.append(key)
            node.sons.append(None)
            return
        if(node.sons[pos]==None):
            if len(node.keys)< self.t and  node is self.root :
                node.keys = node.keys[:pos] + [key] + node.keys[pos:] 
                node.sons = node.sons[:pos] + [None] + node.sons[pos:]
                if len(node.keys)== self.t:
                    self.split(node,None)
            else:
                if len(node.keys)< self.t-1:             
                    node.keys = node.keys[:pos] + [key] + node.keys[pos:]
                    node.sons = node.sons[:pos] + [None] + node.sons[pos:]
                else:
                    node.keys = node.keys[:pos] + [key] + node.keys[pos:]
                    node.sons = node.sons[:pos] + [None] + node.sons[pos:]
                    self.split(node,parnode)
        else:
            self._insert(key,node.sons[pos],node)
            if len (node.keys)==self.t:
                if node is self.root:
                    self.split(node,None)
                else:
                    self.split(node,parnode)

            return self


    def insert(self, key):
        self._insert(key, self.root,None)
    def split(self,node,parnode):
        mid=(self.t+1)//2
        if parnode is None:
            self.root=self.Node()
            left=self.Node()
            right=self.Node()
            left.keys=node.keys[:mid-1]
            right.keys=node.keys[mid:]
            left.sons=node.sons[:mid]
            right.sons=node.sons[mid:]
            self.root.sons=[left,right]
            self.root.keys = [node.keys[mid-1]]
            return self.root
        else:
            left = self.Node()
            right = self.Node()
            left.keys = node.keys[:mid-1]
            right.keys = node.keys[mid:]
            left.sons = node.sons[:mid]
            right.sons = node.sons[mid:]
            pos=parnode.position(node.keys[mid-1])
            parnode.keys = parnode.keys[:pos] + [ node.keys[mid-1] ] + parnode.keys[pos:]
            parnode.sons = parnode.sons[:pos ] + [left, right] + parnode.sons[pos+1 :]           
    def recherche(self ,key):
        return self._recherche(self.root,key)
    def _recherche(self,node,key):
        if node is None or len(node.keys)==0: return None
        pos=node.position(key)
        if(pos<len(node.keys) and node.keys[pos]==key  ):
            return node
        return self._recherche(node.sons[pos],key) 
    