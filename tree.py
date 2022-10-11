tree=[None]*3
def root(n):
    if tree[0]!=None:
        pass
    else:
        tree[0]=n
def Lnode(parent,data):
    tree[(parent*2)+1]=data
def rnode(parent,data):
    tree[(parent*2)+2]=data
root(10)
Lnode(0,30)
rnode(0,100)
for i in tree:
    print(i)
