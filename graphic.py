import sys
import pydot
from PyQt5.QtGui import QPixmap, QIcon 
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.uic import loadUi
import networkx as nx
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from AVL_Tree import *
from TAS_Tree import *
from ABR_Tree import *
from TAS_tree1 import *
from M_AIRE import *
from BTree import *
import time
import os, subprocess
inlist = []
class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        global b
        b=0
        loadUi("graphic.ui", self) 
        self.abr=ABRTree()
        self.le_data.returnPressed.connect(self.insert)
        self.btn_clear.clicked.connect(self.clear)
        self.bt_add.clicked.connect(self.insert)
        self.btn_remove.clicked.connect(self.remove)
        self.grade_sb.valueChanged.connect(self.grade_changed)
        self.ArbreTypes.currentIndexChanged.connect(self.indexChanged_lambda)
        self.IF.clicked.connect(self.insertf)
        self.SR.clicked.connect(self.deleteR)
        self.OF.clicked.connect(self.open)
        self.find.clicked.connect(self.recherche)
        img_add = QIcon('img/add')
        img_del = QIcon('img/del')
        img_clean = QIcon('img/clean') 
        img_find = QIcon('img/find')
        self.bt_add.setIcon(img_add)
        self.btn_remove.setIcon(img_del)
        self.btn_clear.setIcon(img_clean)
        self.find.setIcon(img_find)
        self.label.hide()
        self.grade_sb.hide()
        self.grade_sb.lineEdit().setReadOnly(True)
        self.SR.hide()
        self.showMaximized()

    def insertf(self):
        self.clear()
        nblist = []
        with open(r"nblist.txt", "r+") as f:
            data = f.readlines() #lire le fichier
            for line in data:
                nblist += line.strip().split(" ") #recuperer la liste de nombres
        try:
            if(b==5):
                for i in range(len(nblist)):
                    self.ma.insert(float(nblist[i]))
                    self.lw_operations.addItem('insertion: %s' %nblist[i])

                self.tree_modified() 
            if(b==4):

                for i in range(len(nblist)):
                    self.btree.insert(float(nblist[i]))
                    self.lw_operations.addItem('insertion: %s' %nblist[i]) 
                self.tree_modified()    
            if(b==1):
                for i in range(len(nblist)):
                    self.avltree.insert(int(nblist[i]))
                   
                    self.lw_operations.addItem('insertion: %s' %nblist[i]) 
                    
                    
                self.tree_modified()

            if(b==0):
                for i in range(len(nblist)):
                    self.abr.insert(int(nblist[i]))
                    self.lw_operations.addItem('insertion: %s' %nblist[i]) 
                self.tree_modified()   
                    
                    
            if(b==2):
                for i in range(len(nblist)):
                    self.tasmin.insert(int(nblist[i]))
                    self.lw_operations.addItem('insertion: %s' %nblist[i]) 
                self.tree_modified()   
                    
                   
            if(b==3):
                for i in range(len(nblist)):
                    self.tasmax.insert(int(nblist[i]))
                    self.lw_operations.addItem('insertion: %s' %nblist[i]) 
                self.tree_modified()   
                    
                    
        except ValueError:
            QMessageBox.information(self, "information", "la valeur entrée est incorrecte")
        finally:
            self.le_data.clear()
        return

    def indexChanged_lambda(self, value):
        global b
        b=value
        self.lw_operations.clear()
        self.tree_lb.clear()
        plt.clf()
        
        if(value==0):
            self.abr=ABRTree()
            self.label.hide()
            self.grade_sb.hide()
            self.SR.hide()
        if(value==1):
            self.avltree=AVLTree()
            self.label.hide()
            self.grade_sb.hide()
            self.SR.hide()
        if(value==2):
            self.tasmin=BinHeap()
            self.label.hide()
            self.grade_sb.hide()
            self.SR.show()
        if(value==3):

            self.tasmax=BinHeap1()
            self.label.hide()
            self.grade_sb.hide()
            self.SR.show()
        if(value==4):
            self.btree=BTree(self.grade_sb.value())
            self.label.show()
            self.grade_sb.show()
            self.grade_sb.setValue(3)
            self.grade_sb.setMaximum(99)
            self.grade_sb.setSingleStep(2)
            self.SR.hide()
        if(value==5):
            self.ma=M_aire(self.grade_sb.value())
            self.label.show()
            self.grade_sb.show()
            self.grade_sb.setValue(3)
            self.grade_sb.setMaximum(100)
            self.grade_sb.setSingleStep(1)
            self.SR.hide()

    def open(self):
        if sys.platform == "win32":
            os.startfile('nblist.txt')
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, 'nblist.txt'])

    def clear(self):
        self.tree_lb.clear()
        self.lw_operations.clear()
        if(b==3):
            self.tasmax=BinHeap1()
        if(b==2):
            self.tasmin=BinHeap()
        if(b==4): 
            self.btree = BTree(self.grade_sb.value())
        if(b==5): 
            self.ma = M_aire(self.grade_sb.value())
        if(b==1):
            self.avltree = AVLTree()
        if(b==0):
            self.abr=ABRTree()
    
    def recherche(self,val):
        try:
            val=int(self.le_data.text())
            w=[]
            r=[]
            if b==0:
                self.abr.recherche(val,w,r)
                if(len(r)!=0):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    self.tree_colorized(w,r)
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    self.tree_colorized(w,r)
                    return False
            if b==1:
                self.avltree.recherche(val,w,r)
                if(len(r)!=0):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    self.tree_colorized(w,r)
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    self.tree_colorized(w,r)
                    return False
            if b==2:
                self.tasmin.recherche(val,w,r)
                if(len(r)!=0):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    self.tree_colorized(w,r)
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    self.tree_colorized(w,r)
                    return False
            if b==3:
                self.tasmax.recherche(val,w,r)
                if(len(r)!=0):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    self.tree_colorized(w,r)
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    self.tree_colorized(w,r)
                    return False
            if b==5:
                if(self.ma.recherche(val)!=None):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    return False
            if b==4:
                if(self.btree.recherche(val)!=None):
                    self.lw_operations.addItem("la valeur "+str(val)+" existe")
                    return True
                else:
                    self.lw_operations.addItem("la valeur "+str(val)+" n'existe pas")
                    return False
        except ValueError:
                QMessageBox.information(self, "information", "la valeur entrée est incorrecte")

    def grade_changed(self, grade):
        if(b==4): 
            self.btree = BTree(grade)
        if(b==5): 
            self.ma = M_aire(grade)
        self.tree_modified()
        self.tree_lb.clear()
        self.lw_operations.clear()

    def insert(self):
        value = self.le_data.text()
        if (self.recherche(value)!=True):
            try:
                if(b==5):
                    self.ma.insert(float(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value)
                if(b==4):

                    self.btree.insert(float(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value)
                if(b==1):
                    
                    self.avltree.insert(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value)   
                if(b==0):
                    self.abr.insert(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value) 
                if(b==2):
                    self.tasmin.insert(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value) 
                if(b==3):
                    self.tasmax.insert(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('insertion: %s' %value) 
            except ValueError:
                QMessageBox.information(self, "information", "la valeur entrée est incorrecte")
        
        self.le_data.clear()

    def remove(self):
        value = self.le_data.text()
        if (self.recherche(value)==True):
            try:
                if(b==5):
                    self.ma.Delete(float(value))
                    self.tree_modified()
                    self.lw_operations.addItem('Suppression: %s' % value)
               
                if(b==1):
                    self.avltree.delete(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('Suppression: %s' % value) 
                if(b==0):
                    self.abr.delete(int(value))
                    self.tree_modified()
                    self.lw_operations.addItem('Suppression: %s' % value)  
                if(b==2): 
                    self.tasmin.delete(int(value))
                    self.lw_operations.addItem('Suppression: %s' % value)
                    self.tree_modified()
                    
                if(b==3):
                    self.tasmax.delete(int(value))
                    self.lw_operations.addItem('Suppression: %s' % value)
                    self.tree_modified()
                    
            except ValueError:
                QMessageBox.information(self, "information", "la valeur entrée est incorrecte")
            
        self.le_data.clear()
        self.le_data.setFocus()
    
    def tree_modified(self):
        graph = pydot.Dot(graph_type='digraph', color="Blue",ratio='fill')
        if(b==5):
            is_empty = self.ma.root is None or not self.ma.root.keys
            idd = 1
            nodes = [] if is_empty else [(self.ma.root, idd)]            
            while nodes:
                parent, iid = nodes.pop(0)
                value = ' | '.join(map(self.to_str, parent.keys))
                dot_parent = pydot.Node(iid, shape='rectangle', label = value)
                graph.add_node(dot_parent)
                for child in [ch for ch in parent.sons if ch is not None]:
                    idd+= 1
                    nodes.append((child, idd))
                    value = '|'.join(map(self.to_str, child.keys))
                    dot_node = pydot.Node(idd, shape='rectangle', label = value)
                    graph.add_node(dot_node)
                    graph.add_edge(pydot.Edge(dot_parent, dot_node))
            if is_empty:
               image = QPixmap()
            else:
                _bytes = graph.create(format='png')
                image = QPixmap()
                image.loadFromData(_bytes)
            self.tree_lb.setPixmap(image)
        if(b==4):
            is_empty = self.btree.root is None or not self.btree.root.keys
            idd = 1
            nodes = [] if is_empty else [(self.btree.root, idd)]
            while nodes:
                parent, iid = nodes.pop(0)
                value = ' | '.join(map(self.to_str, parent.keys))
                dot_parent = pydot.Node(iid, shape='rectangle', label = value)
                graph.add_node(dot_parent)
                for child in [ch for ch in parent.sons if ch is not None]:
                    idd+= 1
                    nodes.append((child, idd))
                    value = '|'.join(map(self.to_str, child.keys))
                    dot_node = pydot.Node(idd, shape='rectangle', label = value)
                    graph.add_node(dot_node)
                    graph.add_edge(pydot.Edge(dot_parent, dot_node))
            if is_empty:
                image = QPixmap()
            else:
                _bytes = graph.create(format='png')
                image = QPixmap()
                image.loadFromData(_bytes)
            self.tree_lb.setPixmap(image)
        if(b==1):
            plt.figure(figsize=(11.29, 5.43), dpi=100)
            G=nx.DiGraph()
            if(self.avltree.node==None ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                is_empty = self.avltree.node.getlefta().node== None and self.avltree.node.getrighta().node== None
                if is_empty:
                    G.add_node(self.avltree.node.key)
                    pass
                else: 
                    k=[]
                    self.avltree.getedges(k)
                    G.add_edges_from(k)
                pos = hierarchy_pos(G,self.avltree.node.key)
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf()
        if(b==0):
            plt.figure(figsize=(11.29, 5.43), dpi=100)
            G=nx.DiGraph()
            if(self.abr.node==None ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                is_empty = self.abr.node.getlefta().node== None and self.abr.node.getrighta().node== None
                if is_empty:
                    G.add_node(self.abr.node.key)
                    pass
                else:  
                    k=[]
                    self.abr.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.abr.node.key)
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf()
        if(b==2):
            plt.figure(figsize=(11.29, 5.43), dpi=100)
            G=nx.DiGraph()
            if(self.tasmin.currentSize==0 ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                if self.tasmin.currentSize==1:
                    G.add_node(self.tasmin.heapList[self.tasmin.currentSize])
                    pass
                else:  
                    k=[]
                    self.tasmin.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.tasmin.heapList[1])
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf() 
        if(b==3):
            plt.figure(figsize=(11.29, 5.43), dpi=100)
            G=nx.DiGraph()
            if(self.tasmax.currentSize==0 ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                if self.tasmax.currentSize==1:
                    G.add_node(self.tasmax.heapList[self.tasmax.currentSize])
                    pass
                else:  
                    k=[]
                    self.tasmax.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.tasmax.heapList[1])
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf()       
    @staticmethod
    def to_str(number):
        if number.is_integer():
            return str(int(number))
        return str(number)

    def deleteR(self):
        if(b==2):
            value=self.tasmin.delMin()
            self.tree_modified()      
        if(b==3):
            value=self.tasmax.delMax()
            self.tree_modified()
        self.lw_operations.addItem('Suppression: %s' % value)

    def tree_colorized(self,w,r):
        
        if(b==1):
            G=nx.DiGraph()
            if(self.avltree.node==None ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                is_empty = self.avltree.node.getlefta().node== None and self.avltree.node.getrighta().node== None
                if is_empty:
                    
                    G.add_node(self.avltree.node.key)
                    pass
                else: 
                    
                    k=[]
                    self.avltree.getedges(k)
                    G.add_edges_from(k)

                pos = hierarchy_pos(G,self.avltree.node.key)
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                nx.draw_networkx_nodes(G, pos,nodelist=w,node_color='r', node_size=1000)
                nx.draw_networkx_nodes(G, pos,nodelist=r,node_color='g', node_size=1000)
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf()
        if(b==0):
            G=nx.DiGraph()
            if(self.abr.node==None ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                is_empty = self.abr.node.getlefta().node== None and self.abr.node.getrighta().node== None
                if is_empty:
                    G.add_node(self.abr.node.key)
                    pass
                else:  
                    k=[]
                    self.abr.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.abr.node.key)
                
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                nx.draw_networkx_nodes(G, pos,nodelist=w,node_color='r', node_size=1000)
            
                
                    
                nx.draw_networkx_nodes(G, pos,nodelist=r,node_color='g', node_size=1000)

                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf()
        if(b==2):
            G=nx.DiGraph()
            if(self.tasmin.currentSize==0 ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                
                if self.tasmin.currentSize==1:
                    G.add_node(self.tasmin.heapList[self.tasmin.currentSize])
                    pass
                else:  
                    k=[]
                    self.tasmin.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.tasmin.heapList[1])
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                nx.draw_networkx_nodes(G, pos,nodelist=w,node_color='r', node_size=1000)
                nx.draw_networkx_nodes(G, pos,nodelist=r,node_color='g', node_size=1000)
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf() 
        if(b==3):
            G=nx.DiGraph()
            if(self.tasmax.currentSize==0 ):
                plt.clf()
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                pass
            else:
                
                if self.tasmax.currentSize==1:
                    G.add_node(self.tasmax.heapList[self.tasmax.currentSize])
                    pass
                else:  
                    k=[]
                    self.tasmax.getedges(k)
                    G.add_edges_from(k) 
                pos = hierarchy_pos(G,self.tasmax.heapList[1])
                nx.draw(G,pos, with_labels=True,node_size=1000, node_color="skyblue", node_shape='o')
                nx.draw_networkx_nodes(G, pos,nodelist=w,node_color='r', node_size=1000)
                nx.draw_networkx_nodes(G, pos,nodelist=r,node_color='g', node_size=1000)
                plt.savefig('Graph', format="PNG")
                image = QPixmap("Graph")          
                self.tree_lb.setPixmap(image)
                plt.clf() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())