class M_aire:
    class Node:
        #initialisation de noeud 
        def __init__(self):
            self.sons = []
            self.keys = []
        #position d'un valeur dans un neoud 
        def position(self, key):
            b = 0
            try:
                while b <len(self.sons)-1:            
                    if key <= self.keys[b] :  
                        return b
                    else:
                        b+=1

                pass
            except:
                return b

            return len(self.sons)-1
    #inisialisation d'un arbre
    def __init__(self, t):
        self.root = self.Node()
        self.t = t 
    #insertion 
    def _insert(self, key, node):
        #si noeud n'exist pas
        if node is None: return None
        #si c'est un nouveau noeud
        if len(node.sons) == 0:   
            node.sons.append(None)
            node.keys.append(key)
            node.sons.append(None)
            return
        pos = node.position(key)
        # si le noeud et deja exist mais il n'etes pas plein
        if node.sons[pos] is  None and len(node.keys)<self.t-1 :            
            node.keys = node.keys[:pos] + [key] + node.keys[pos:]
            node.sons.append(None)
            return
        #si le noeud racine est plein,on cree un nouveau noeud fils ou on insert dans un noeud fils
        if len(node.keys) ==  self.t - 1  :
            pos=node.position(key)    
            if node.sons[pos] is None :
                n=self.Node()
                self._insert(key,n)
                node.sons[pos]=n
            else:
                self._insert(key,node.sons[pos])    
                return   
    def insert(self, key):
        self._insert(key, self.root)
    def recherche(self ,key):
        return self._recherche(self.root,key)
    def _recherche(self,node,key):
        if node is None or len(node.keys)==0: return None
        pos=node.position(key)
        if(pos<len(node.keys) and node.keys[pos]==key  ):
            return node 
        return self._recherche(node.sons[pos],key)
    def Delete(self,key):
        return self._Delete(self.root,self.root,key)
    def _Delete(self,node,parnode,key):
        if node is None: return None
        pos=node.position(key)
        if(pos<len(node.keys) and node.keys[pos]==key  ):
            #n'pas des fils
            if node.sons[pos] is None and node.sons[pos+1] is None:
                if node is self.root and len(node.keys)==1:
                    node.keys.pop()
                    node.sons.pop()
                    node.sons.pop()
                    return self
                node.keys = node.keys[:pos] + node.keys[pos+1:]
                node.sons.pop(pos) 
                #c'est le dernier key dans le noeud feuille        
                if(len(node.keys)==0):
                    node.sons.pop() 
                    pos1=parnode.position(key)
                    parnode.sons.pop(pos1)
                    parnode.sons.insert(pos1, None)
            #fils droit
            elif node.sons[pos] is None and node.sons[pos+1] is not None :
                #c'est le dernier key dans le noeud 
                if len(node.keys)==1:
                    sc=self.succesor(node.sons[pos+1])
                    self._Delete(node,parnode,sc)
                    node.keys[pos]=sc
                else:
                    if(pos==len(node.keys)-1):
                        node.sons[pos]=node.sons[pos+1]
                    node.sons.pop(pos)
                    node.keys = node.keys[:pos] + node.keys[pos+1:]
            #fils gauche
            elif node.sons[pos+1] is None and node.sons[pos] is not None :
                #c'est le dernier key dans le noeud 
                if len(node.keys)==1:
                    sc=self.succesor(node.sons[pos])
                    self._Delete(node,parnode,sc)
                    node.keys[pos]=sc
                else:
                    if(pos==0):
                        node.sons[pos+1]=node.sons[pos]
                    node.sons.pop(pos)
                    node.keys = node.keys[:pos] + node.keys[pos+1:]
            else :
                sc=self.succesor(node.sons[pos+1])
                self._Delete(node,parnode,sc)
                node.keys[pos]=sc
            return self
        return self._Delete(node.sons[pos],node,key)
    def succesor(self, node):
        if node.sons[0] == None:
            return node.keys[0]
        else:
            return self.succesor(node.sons[0])